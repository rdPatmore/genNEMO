import xarray as xr

""" 
For creating a the parent coordinates file.

Note: this is not a good as a domain_cfg as nav_lon/nav_lat is not
the same as glam*, phi*
"""

source = '/gws/nopw/j04/jmmp/MASS/GloSea6/Daily/'
ds_t = xr.open_dataset(source + 'glosea6_grid_T_20041231.nc')
ds_u = xr.open_dataset(source + 'glosea6_grid_U_20041231.nc')
ds_v = xr.open_dataset(source + 'glosea6_grid_V_20041231.nc')

ds_coord_out = xr.Dataset()
ds_coord_out["glamt"] = ds_t.nav_lon.reset_coords(drop=True)
ds_coord_out["glamv"] = ds_v.nav_lon.reset_coords(drop=True)
ds_coord_out["glamu"] = ds_u.nav_lon.reset_coords(drop=True)
ds_coord_out["gphit"] = ds_t.nav_lat.reset_coords(drop=True)
ds_coord_out["gphiv"] = ds_v.nav_lat.reset_coords(drop=True)
ds_coord_out["gphiu"] = ds_u.nav_lat.reset_coords(drop=True)
ds_coord_out = ds_coord_out.expand_dims( dim="t", axis=0 )
ds_coord_out["gdept"] = xr.DataArray(ds_t.deptht.values, dims=["depth"])
ds_coord_out["gdepu"] = xr.DataArray(ds_u.depthu.values, dims=["depth"])
ds_coord_out["gdepv"] = xr.DataArray(ds_v.depthv.values, dims=["depth"])
print (ds_coord_out)
ds_coord_out["e3t"] = xr.DataArray(ds_t.e3t.values, dims=["depth", "x", "y"])
ds_coord_out["e3u"] = xr.DataArray(ds_u.e3u.values, dims=["depth", "x", "y"])
ds_coord_out["e3v"] = xr.DataArray(ds_v.e3v.values, dims=["depth", "x", "y"])
ds_coord_out = ds_coord_out.squeeze()
print ('')
print ('')
print (ds_t.time_centered)
print ('')
print ('')
#ds_coord_out["time"] = xr.DataArray(ds_t.time_centered.values, dims=["t"])
ds_coord_out.to_netcdf('parent_coords.nc')
