import matplotlib.pyplot as plt
import xarray as xr

a = xr.open_dataset("/gws/nopw/j04/verify_oce/NEMO/Preprocessing/LBC/GloSat_NAARC_bdyT_y1850m01.nc", chunks="auto").vosaline

a = a.isel(xb=slice(0,5000)).squeeze()
#a = a.isel(xb=2000).squeeze()
print (a)

p = plt.pcolor(a, vmin=-10,vmax=10)
#p = plt.plot(a)
plt.colorbar()
plt.show()
#plt.savefig("bathy_test.png")
