import xarray as xr
import matplotlib.pyplot as plt

cfg_fn = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
da = xr.open_dataset("glosea_ini_20040101_vosaline.nc").vosaline
da = da.rename({"deptht":"z"})
cfg = xr.open_dataset(cfg_fn).squeeze()
tmask = cfg.tmask
bottom_level = cfg.bottom_level

da_masked = da.where(tmask == 1)
da_masked = da_masked.where(da_masked.z < cfg.gdept_0[bottom_level])

fig, axs = plt.subplots(2)
da_z0 = da_masked.isel(z=0)
da_y500 = da_masked.isel(y=500)
axs[0].pcolor(da_z0.nav_lon, da_z0.nav_lat, da_z0, shading="nearest")
axs[1].pcolor(da_y500.nav_lon, da_y500.z, da_y500, shading="nearest")
axs[1].invert_yaxis()
plt.savefig("masked_glosea_test")
