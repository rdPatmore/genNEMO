import xarray as xr

bathy = xr.open_dataset('/gws/nopw/j04/jmmp/public/AMM15/AMM15_BATHY/ADD_NICO_BALTIC_BDY_RIM_SMOOTH_BDY_COPY_CUTAMM15_CORRECTED_EXPANDED_MERGE_GEBCO_DEEP_TO_200-100_EMODNET_TO_10-5_GEBCO_TO_COAST_amm15.bathydepth.co7.cs3x.cs20.nc')

dom_cfg = xr.open_dataset('/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc')
print (dom_cfg)
bathy = bathy.rename({'lon':'x','lat':'y'})
bathy['nav_lon'] = dom_cfg.nav_lon
bathy['nav_lat'] = dom_cfg.nav_lat
print (bathy)

bathy.to_netcdf('AMM15_P2.0_bathy.nc')
