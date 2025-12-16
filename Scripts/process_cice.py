import xarray as xr
from dask.diagnostics import ProgressBar

path_in = "/gws/nopw/j04/glosat/production/UKESM/raw/u-ck651/18500101T0000Z/"
fn_in = "cice_ck651i_1m_18500101-18500201.nc"
path_out = "/gws/nopw/j04/verify_oce/NEMO/Preprocessing/LBC/ICE_src/"
fn_out = fn_in

ice = xr.open_dataset(path_in + fn_in, chunks=-1)

drop_list = list(ice.data_vars.keys())
for var in ["aice","hi","hs"]:
    drop_list.remove(var)
ice = ice.drop(drop_list)

#ice['longitude'] = ice.TLON - 180
#ice['latitude'] = ice.TLAT

with ProgressBar():
    ice.to_netcdf(path_out + fn_out)
