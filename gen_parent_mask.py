import xarray as xr
import numpy as np
from sklearn.neighbors import BallTree

def get_subdom_corner_latlon(lat_bounds, lon_bounds, mod_lat, mod_lon):
    #lat = ds_mod_grid.gphit.where(ds_mod_grid.bottom_level>0)
    #lon = ds_mod_grid.glamt.where(ds_mod_grid.bottom_level>0)
    model_points = list( zip( mod_lat.values.flatten(), mod_lon.values.flatten() ) )
    corner_points   = list( zip( lat_bounds, lon_bounds ) )
    print (corner_points)

    bt = BallTree( np.deg2rad(model_points), metric='haversine' )
    dist, mod_idx = bt.query( np.deg2rad(corner_points) )

    #dist = dist * EARTH_RADIUS
    y_points, x_points = np.unravel_index(mod_idx, mod_lat.shape)
    print (y_points)

    return y_points, x_points

# Put in json file
data_path = "/gws/nopw/j04/jmmp/MASS/GloSea6/AMMregion/"
path_in_t = data_path + "19921130T0000Z_mersea.grid_T.nc"
path_in_u = data_path + "19921130T0000Z_mersea.grid_U.nc"
path_in_v = data_path + "19921130T0000Z_mersea.grid_V.nc"
# Put in json file
var_t_name = "votemper"
var_u_name = "vozocrtx"
var_v_name = "vomecrty"
# Put in json file
lat_bounds = np.array( [ 68, 68,  38, 38 ] ) #AMM7
lon_bounds = np.array( [-28, 19, -28, 19 ] ) #AMM7
# Put in json file
mask_save_path = "parent_mask.nc"
coord_save_path = "parent_coords.nc"

ds_t = xr.open_dataset( path_in_t ).isel(time_counter=slice(0,1))
ds_u = xr.open_dataset( path_in_u ).isel(time_counter=slice(0,1))
ds_v = xr.open_dataset( path_in_v ).isel(time_counter=slice(0,1))

mod_lat_t = ds_t.nav_lat.load()
mod_lon_t = ds_t.nav_lon.load()

#y_points, x_points = get_subdom_corner_latlon(
#    lat_bounds, lon_bounds, mod_lat_t, mod_lon_t
#)
# probably want to save these points to a json file
#y_slice = slice( y_points.min(), y_points.max() )
#x_slice = slice( x_points.min(), x_points.max() )

#var_subset_t = ds_t[var_t_name][:, :, y_slice, x_slice].values
var_subset_t = ds_t[var_t_name]
mask_t = np.full(ds_t[var_t_name].shape, False, dtype=bool)
#mask_t[:, :, y_slice, x_slice] = ~np.isnan( var_subset_t )
mask_t = ~np.isnan( var_subset_t )

#var_subset_v = ds_v[var_v_name][:, :, y_slice, x_slice].values
var_subset_v = ds_v[var_v_name]
mask_v = np.full(ds_v[var_v_name].shape, False, dtype=bool)
#mask_v[:, :, y_slice, x_slice] = ~np.isnan( var_subset_v )
mask_v = ~np.isnan( var_subset_v )

#var_subset_u = ds_u[var_u_name][:, :, y_slice, x_slice].values
var_subset_u = ds_u[var_u_name]
mask_u = np.full(ds_u[var_u_name].shape, False, dtype=bool)
#mask_u[:, :, y_slice, x_slice] = ~np.isnan( var_subset_u )
mask_u = ~np.isnan( var_subset_u )

mask_t = mask_t.rename(dict(deptht="depth"))
mask_v = mask_v.rename(dict(depthv="depth"))
mask_u = mask_u.rename(dict(depthu="depth"))

ds_mask_out = xr.Dataset()
ds_mask_out["tmask"] = xr.DataArray(mask_t, dims=["time_counter","depth","y","x"])
ds_mask_out["vmask"] = xr.DataArray(mask_v, dims=["time_counter","depth","y","x"])
ds_mask_out["umask"] = xr.DataArray(mask_u, dims=["time_counter","depth","y","x"])
ds_mask_out.load()

ds_mask_out.to_netcdf( mask_save_path )

# =============================================================================
# Now create the coordinates file
# =============================================================================

ds_coord_out = xr.Dataset()
ds_coord_out["glamt"] = ds_t.nav_lon.reset_coords(drop=True)
ds_coord_out["glamv"] = ds_v.nav_lon.reset_coords(drop=True)
ds_coord_out["glamu"] = ds_u.nav_lon.reset_coords(drop=True)
ds_coord_out["gphit"] = ds_t.nav_lat.reset_coords(drop=True)
ds_coord_out["gphiv"] = ds_v.nav_lat.reset_coords(drop=True)
ds_coord_out["gphiu"] = ds_u.nav_lat.reset_coords(drop=True)
ds_coord_out = ds_coord_out.expand_dims( dim="t", axis=0 ) 
ds_coord_out["depth"] = xr.DataArray(ds_t.deptht.values, dims=["depth"])
#ds_coord_out["time"] = xr.DataArray(ds_t.time_centered.values, dims=["t"])
ds_coord_out.to_netcdf( coord_save_path )






