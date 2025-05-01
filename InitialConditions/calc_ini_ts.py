import xarray as xr
from scipy.interpolate import griddata
from scipy.interpolate import NearestNDInterpolator
import numpy as np
import matplotlib.pyplot as plt
from dask.diagnostics import ProgressBar

def dep_interpolate_lev(ds, cfg, lev, var):
    src_lon =  ds.nav_lon.values.flatten()
    src_lat =  ds.nav_lat.values.flatten()
    src_dep =  ds.deptht.values.flatten()
    
    points = (src_lon, src_lat)
    values = (ds[var].isel(deptht=lev).values.flatten())
    
    tgt_lon =  cfg.nav_lon
    tgt_lat =  cfg.nav_lat
    
    target = (tgt_lon, tgt_lat)
    
    n_grid = griddata(points, values, target, method='nearest')

    return n_grid

def dep_nd_interpolate_lev(ds, cfg, lev, var):
    values = (ds[var].isel(deptht=lev).values.flatten())

    src_lon =  ds.nav_lon.values.flatten()
    src_lat =  ds.nav_lat.values.flatten()
    src_lon = src_lon[~np.isnan(values)]
    src_lat = src_lat[~np.isnan(values)]
    points = list(zip(src_lon, src_lat))
    values = values[~np.isnan(values)]
    tgt_lon =  cfg.nav_lon
    tgt_lat =  cfg.nav_lat
  
    # test if layer is full of nan values
    if values.size > 0:
        #
        interp = NearestNDInterpolator(points, values)
        n_grid = interp(tgt_lon, tgt_lat)
        return n_grid

def dep_3d_interpolate_lev(da, cfg, save=False, load=False, chunks=-1):

    # set src coords as 3d
    src_lon_3d, src_dep_3d = xr.broadcast(da.nav_lon, da.deptht)
    src_lat_3d, src_dep_3d = xr.broadcast(da.nav_lat, da.deptht)

    # flatten input
    values = da.stack(z=["x","y","deptht"])

    # set dst coords as 3d
    tgt_lon, tgt_dep = xr.broadcast(cfg.nav_lon, cfg.gdept_0)
    tgt_lat, tgt_dep = xr.broadcast(cfg.nav_lat, cfg.gdept_0)

    index = ~np.isnan(values).compute()
    values = values[index]
    if load:
        dst_path = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/'
        points = xr.open_dataarray(dst_path + "pre_interp_ds_tmp_points.nc",
                                   chunks=chunks)
    else:
        src_lon = src_lon_3d.stack(z=["x","y","deptht"])
        src_lat = src_lat_3d.stack(z=["x","y","deptht"])
        src_dep = src_dep_3d.stack(z=["x","y","deptht"])

        src_lon = src_lon[index].expand_dims(var_dim=["x"])
        src_lat = src_lat[index].expand_dims(var_dim=["y"])
        src_dep = src_dep[index].expand_dims(var_dim=["z"])

        points = xr.concat([src_dep,src_lat,src_lon],dim="var_dim")
        points = points.reset_index("z")

    # save inputs
    if save:
        with ProgressBar():
            dst_path = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/'
            points.to_netcdf(dst_path + "pre_interp_ds_tmp_points.nc")
        print ("SAVED")
    with ProgressBar():
        points = points.load()
        values = values.load()

    # interpolate
    interp = NearestNDInterpolator(points.T, values)
    print ("done interpolator")
    n_grid = xr.apply_ufunc(interp, tgt_dep, tgt_lat, tgt_lon,
                            dask="parallelized")
    print ("done ngrid")

    return n_grid

def check_depths(cfg):
    '''
    check for gdept_0 and, if absent, create
    '''

    depth_dim = set(["nav_lev","z"]).intersection(set(cfg.dims))
    if 'gdept_0' not in list(cfg.keys()):
        print (cfg)
        cfg['gdept_0'] = cfg.e3t_0.cumsum(dim=depth_dim)
    
        with ProgressBar():
            cfg.to_netcdf("NAARC_cfg.nc")

    return cfg

def interp_var(var, src_fn, cfg_fn, dst_fn):
    '''
    Interpolate source gridded model output to target nemo grid 

    This code uses nearest neighbour interpolation to fill bathymetric
    discrepancies.
    '''
    
    # This is to ignore variable incompatible with chunking such as object dtype
    # WARNING: not very flexible and my break code
    drop_vars = list(xr.open_dataset(src_fn, chunks=-1).keys())
    drop_vars.remove(var)
    drop_vars = drop_vars + ["time_centered"]

    # open datasets
    chunks = dict(x=100,y=100)
    da = xr.open_dataset(src_fn, chunks=chunks, drop_variables=drop_vars
                        )[var].squeeze()

    # interpolate
    tgt_cfg = xr.open_dataset(cfg_fn, chunks=chunks).squeeze()
    tgt_cfg = check_depths(tgt_cfg)
    da_n = dep_3d_interpolate_lev( da, tgt_cfg)

    # set coordinates
    coords=dict(deptht=(['y','x','deptht'], tgt_cfg.gdept_0.data),
                nav_lat=(['y','x'], tgt_cfg.nav_lat.data),
                nav_lon=(['y','x'], tgt_cfg.nav_lon.data)
               )

    da_n = da_n.assign_coords(
           dict(nav_lat=(['y','x'], tgt_cfg.nav_lat.data),
                nav_lon=(['y','x'], tgt_cfg.nav_lon.data)))

    da_n.name = var
    print (da_n)

    # save
    with ProgressBar():
        da_n.to_netcdf(dst_fn)

def interpolate_glosea6_to_co9(var, y='1993', m='01', d='01',
                               domcfg='GEG_SF12.nc'):
    ''' interpolate glosea6 data to co9 target grid '''

    # set file paths
    cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/' + domcfg
    src_path = '/gws/nopw/j04/jmmp/MASS/GloSea6/Daily/'
    src_fn = src_path + 'glosea6_grid_T_' + y + m + d + '.nc'
    dst_fn = 'glosea_ini_' + y + m + d + '_' + \
              domcfg.replace('.nc','') + '_'  + var + '.nc'

    # interpolate
    interp_var(var, src_fn, cfg_fn, dst_fn)

def flood_gosi8(var, y='1850', m='01', d='01'):
    ''' take UKESM historical glosat and flood to gosi8 grid '''

    # set file paths
    dst_path = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/'
    cfg_fn = dst_path + '/NAARC/NAARC_cfg.nc'
    src_path = '/gws/nopw/j04/glosat/production/UKESM/raw/u-ck651/18500101T0000Z/'
    src_fn = src_path + 'nemo_ck651o_1m_18500101-18500201_grid-T.nc'
    dst_path = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/'
    dst_fn = dst_path + 'glosat_ukesm_to_gosi8_' + var + '.nc'

    # interpolate
    interp_var(var, src_fn, cfg_fn, dst_fn)

#def create_glosat_tsd_interpolation_files():
#    """
#    NAARC does interpolation on the fly
#    """
#
#    src_path = '/gws/nopw/j04/glosat/production/UKESM/raw/u-ck651/18500101T0000Z/'
#    src_fn = src_path + 'nemo_ck651o_1m_18500101-18500201_grid-T.nc'
#    drop_vars=["time_centered_bounds","time_centered","time_counter"]
#    da = xr.open_dataset(src_fn, chunks="auto", drop_variables=drop_vars
#                       ).squeeze()
#    mask = xr.where(da.zfull<10000,1,0)
#    mask.name="mask"
#    with ProgressBar():
#        mask.to_netcdf("gosi9_mask.nc")
#        da.zfull.to_netcdf("gosi9_depth.nc")
#        da.thetao.to_netcdf("gosi9_temp.nc")
#        da.thetao.to_netcdf("gosi9_salt.nc")

def create_uniform_forcing():
    cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    cfg = xr.open_dataset(cfg_fn)

    uniform_t = xr.full_like(cfg.tmask, 5).squeeze()
    uniform_t.name = 'tn'
    uniform_s = xr.full_like(cfg.tmask, 35).squeeze()
    uniform_s.name = 'sn'

    uniform_t.to_netcdf("amm15_uniform_t.nc")
    uniform_s.to_netcdf("amm15_uniform_s.nc")

def create_uniform_forcing_masked():
    cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    cfg = xr.open_dataset(cfg_fn)

    uniform_t = xr.where(cfg.tmask == 1, 5, np.nan).squeeze()
    uniform_t.name = 'tn'
    uniform_s = xr.where(cfg.tmask == 1, 35, np.nan).squeeze()
    uniform_s.name = 'sn'

    uniform_t.to_netcdf("amm15_uniform_t_masked.nc")
    uniform_s.to_netcdf("amm15_uniform_s_masked.nc")
 
if __name__ == '__main__':
    #interpolate_glosea6_to_co9('vosaline', domcfg='CO7_EXACT_CFG_FILE.nc')
    #flood_gosi8('thetao', y='1850', m='01', d='01')
    flood_gosi8('so', y='1850', m='01', d='01')
    #create_glosat_tsd_interpolation_files()
    #interpolate_glosea6_to_co9('votemper', domcfg='CO7_EXACT_CFG_FILE.nc')
