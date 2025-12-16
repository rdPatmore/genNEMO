import matplotlib.pyplot as plt
import xarray as xr

path = "/gws/ssde/j25a/verify_oce/NEMO/Preprocessing/LBC/OCE/"
coord = "MES_clean3"
coord = "ZPS"

fig, axs = plt.subplots(2, figsize=(10,4))
#a = xr.open_dataset("/gws/nopw/j04/jmmp/ryapat/CHAMFER/GLOSEA6_atlantic/AMM15_bdyT_y2019m04.nc", chunks="auto").votemper
#b = xr.open_dataset("/gws/nopw/j04/jmmp/ryapat/CHAMFER/GLOSEA6_atlantic/AMM15_bdyT_y2021m04.nc", chunks="auto").votemper
a = xr.open_dataset(path + coord + "/GloSat_NAARC_bdyT_y1850m01.nc", chunks="auto").sossheig
b = xr.open_dataset(path + coord + "/GloSat_NAARC_bdyU_y1850m01.nc", chunks="auto")

a = a.isel(xb=slice(-5000,-1)).squeeze()
b = b.isel(xb=slice(-5000,-1)).squeeze()
#a = a.isel(xb=2000).squeeze()
#a = a.isel(time_counter=20)
#b = b.isel(time_counter=20)
print (a)

#p = axs[0].pcolor(a, vmin=-10,vmax=20)
p = axs[0].plot(a)
p = axs[1].pcolor(b.gdept, b.vomecrtx, vmin=-0.5,vmax=0.5, cmap=plt.cm.RdBu_r)
p = axs[1].plot(b)
#p = plt.plot(a)
plt.colorbar(p)
plt.show()
#plt.savefig("bathy_test.png")
