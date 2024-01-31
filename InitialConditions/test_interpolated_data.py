import xarray as xr
import matplotlib.pyplot as plt

cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
da = xr.open_dataset("glosea_ini_20040101_votemper.nc").votemper
cfg = xr.open_dataset(cfg_fn).squeeze()
tmask = cfg.tmask
bottom_level = cfg.bottom_level

print (da)
print (cfg.gdept_0)
da_masked = da.where(tmask == 1)
da_masked = da_masked.where(da_masked.deptht < cfg.gdept_0[bottom_level])
print (da_masked)

fig, axs = plt.subplots(2)
axs[0].pcolor(da_masked.isel(z=0))
axs[1].pcolor(da_masked.isel(y=500))
plt.savefig("masked_glosea_test")
