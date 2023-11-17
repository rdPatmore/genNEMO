import xarray as xr

cfg_path = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
mask = xr.open_dataset(cfg_path).top_level.squeeze()
mask.name = 'mask'

# 0 is land 
# 1 is ocean
# -1 is edge of domain

# make mask for bdy (pyBdy searches for boundary between -1 and 1)
mask.loc[0] = -1
mask.loc[-1] = -1
#mask.loc[:,-1] = -1
mask.loc[:,0] = -1

mask.to_netcdf('bdy_msk.nc')
