import xarray as xr
from scipy.interpolate import griddata
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

def interp_var(var):
    # start year and month
    d = '01'
    m = '01'
    y = '2004'
    
    cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    path = '/gws/nopw/j04/jmmp/MASS/GloSea6/Daily/'
    fn = 'glosea6_grid_T_' + y + m + d + '.nc'
    
    ds = xr.open_dataset(path + fn)
    print (ds)
    cfg = xr.open_dataset(cfg_fn)
    print (' ')
    print (' ')
    print (' ')
    print (cfg)
    print (dkjffg)
    ds_levs = []
    for lev in range(ds.deptht.size):
        ds_levs.append(dep_interpolate_lev(ds, cfg, lev, var))
        print (lev)
    
    
    ds_n = np.array(ds_levs)
    
    coords=dict(deptht=(['deptht'], ds.deptht.values))
    ds_n = xr.DataArray(data=ds_n, coords=coords,
                        dims=('deptht','y','x'), name=var)
    
    ds_n = ds_n.interp(deptht=cfg.gdept_1d).isel(t=0)
    ds_n = ds_n.fillna(ds_n.mean())
    ds_n.to_netcdf('glosea_ini_' + y + m + d + '_'  + var + '.nc')

def create_uniform_forcing():
    cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    cfg = xr.open_dataset(cfg_fn)

    uniform_t = xr.full_like(cfg.tmask, 5).squeeze()
    uniform_t.name = 'tn'
    uniform_s = xr.full_like(cfg.tmask, 35).squeeze()
    uniform_s.name = 'sn'

    uniform_t.to_netcdf("amm15_uniform_t.nc")
    uniform_s.to_netcdf("amm15_uniform_s.nc")
 
create_uniform_forcing()
