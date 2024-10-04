import xarray as xr
from dask.diagnostics import ProgressBar

def set_cori(base):
    path = "/gws/nopw/j04/chamfer/AMM15_C09p2_CHAMFER/"
    domcfg = xr.open_dataset(path + base + ".nc",  chunks="auto")
    
    # set coriolis to zero
    domcfg["ff_t"] = domcfg.ff_t * 0.0
    domcfg["ff_f"] = domcfg.ff_f * 0.0
    
    # save
    with ProgressBar():
        domcfg.to_netcdf(path + base + "_no_cori.nc")

def set_coords(base):
    path = "/gws/nopw/j04/chamfer/AMM15_C09p2_CHAMFER/"
    domcfg = xr.open_dataset(path + base + "_no_cori.nc", chunks="auto")

    # change from sco to zps
    domcfg["ln_sco"] = 0
    domcfg["ln_zps"] = 1
    
    # save
    with ProgressBar():
        domcfg.to_netcdf(path + base + "_no_cori_zps.nc")

base = "CO7_EXACT_CFG_FILE"
#set_cori(base)
set_coords(base)
