import xarray as xr
from scipy.interpolate import griddata
from scipy.interpolate import NearestNDInterpolator
import numpy as np
import matplotlib.pyplot as plt


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

def dep_3d_interpolate_lev(da, cfg):
    src_lon_3d = np.broadcast_to(da.nav_lon.data, da.shape)
    src_lat_3d = np.broadcast_to(da.nav_lat.data, da.shape)
    da_t = da.transpose("x","y","deptht")
    src_dep_3d = np.transpose(np.broadcast_to(da_t.deptht.data, da_t.shape))

    tgt_lon =  np.broadcast_to(cfg.nav_lon.data, cfg.gdept_0.shape)
    tgt_lat =  np.broadcast_to(cfg.nav_lat.data, cfg.gdept_0.shape)
    tgt_dep =  cfg.gdept_0.data

    # flatten input
    values = da.values.flatten()
    src_lon = src_lon_3d.flatten()
    src_lat = src_lat_3d.flatten()
    src_dep = src_dep_3d.flatten()

    src_lon = src_lon[~np.isnan(values)]
    src_lat = src_lat[~np.isnan(values)]
    src_dep = src_dep[~np.isnan(values)]
    points = list(zip(src_dep, src_lat, src_lon))
    values = values[~np.isnan(values)]

    interp = NearestNDInterpolator(points, values)
    n_grid = interp(tgt_dep, tgt_lat, tgt_lon)
    return n_grid

def interp_var(var):
    # start year and month
    d = '01'
    m = '01'
    y = '2004'
    
    cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    path = '/gws/nopw/j04/jmmp/MASS/GloSea6/Daily/'
    fn = 'glosea6_grid_T_' + y + m + d + '.nc'
    
    da = xr.open_dataset(path + fn)[var].squeeze()
    cfg = xr.open_dataset(cfg_fn).squeeze()
    #da = da.isel(deptht=slice(None,5))
    #cfg = cfg.isel(z=slice(None,5))
    ds_levs = []
    da_n = dep_3d_interpolate_lev(da, cfg)
    ##print (da_n.shape)
    #for lev in range(ds.deptht.size):
    #    interpolated_lev = dep_nd_interpolate_lev(ds, cfg, lev, var)
    #    if interpolated_lev is not None:
    #        ds_levs.append(interpolated_lev)
    #        print (lev)
    #
    #
    #ds_n = np.array(ds_levs)
    #
    #deptht_3d = np.broadcast_to(
    #                   ds.deptht.isel(deptht=slice(None, ds_n.shape[0])).data,
    #                    ds_n.shape[::-1])
    coords=dict(deptht=(['deptht'], cfg.gdept_1d.data),
                nav_lat=(['y','x'], cfg.nav_lat.data),
                nav_lon=(['y','x'], cfg.nav_lon.data)
               )

    da_n = xr.DataArray(data=da_n, coords=coords,
                        dims=('deptht','y','x'), name=var)
    print (da_n)
    
    #print (ds_n)
    #print (ds_n.deptht)
    #print (cfg.gdept_0)
    #ds_n = ds_n.interp(deptht=cfg.gdept_0.values)
    #ds_n[-1] = ds_n[-3]
    #ds_n[-2] = ds_n[-3]


    print ("done")
    da_n.to_netcdf('glosea_ini_' + y + m + d + '_'  + var + '.nc')

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
 
#interp_var('vosaline')
interp_var('votemper')
