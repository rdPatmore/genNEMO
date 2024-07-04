import xarray as xr
from dask.diagnostics import ProgressBar

def set_cori():
    path = "/gws/nopw/j04/chamfer/AMM15_C09p2_CHAMFER/"
    domcfg = xr.open_dataset(path + "GEG_SF12.nc",  chunks=dict(z=1))
    
    # set coriolis to zero
    domcfg["ff_t"] = domcfg.ff_t * 0.0
    domcfg["ff_f"] = domcfg.ff_f * 0.0
    
    # save
    with ProgressBar():
        domcfg.to_netcdf(path + "GEG_SF12_no_cori.nc")

def set_coords():
    path = "/gws/nopw/j04/chamfer/AMM15_C09p2_CHAMFER/"
    domcfg = xr.open_dataset(path + "GEG_SF12_no_cori.nc", chunks="auto")

    # change from sco to zps
    domcfg["ln_sco"] = 0
    domcfg["ln_zps"] = 1
    
    # save
    with ProgressBar():
        domcfg.to_netcdf(path + "GEG_SF12_no_cori_zps.nc")

set_coords()
