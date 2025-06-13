import xarray as xr
import numpy as np

def atlantic():
    """ 
    Create mask that defines location of bdy forcing in the atlantic sector 
    """

    cfg_path = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    mask = xr.open_dataset(cfg_path).top_level.squeeze()
    mask.name = 'mask'
    
    # 0 is land 
    # 1 is ocean
    # -1 is edge of domain
    
    # make mask for bdy (pyBdy searches for boundary between -1 and 1)
    mask.loc[0] = -1
    mask.loc[-1] = -1
    #mask.loc[:,-1] = -1
    mask.loc[:,0] = -1
    
    mask.to_netcdf('bdy_msk_atlantic.nc')

def baltic():
    """ 
    Create mask that defines location of bdy forcing in the baltic sector 
    """

    cfg_path = '/gws/nopw/j04/jmmp/public/AMM15/DOMAIN_CFG/GEG_SF12.nc'
    mask = xr.open_dataset(cfg_path).top_level.squeeze()
    mask.name = 'mask'
    
    # 0 is land 
    # 1 is ocean
    # -1 is edge of domain
    
    # make mask for bdy (pyBdy searches for boundary between -1 and 1)
    mask.loc[:,-1] = -1
    
    mask.to_netcdf('bdy_msk_baltic.nc')

def adjust_NAARC():
    
    # path 
    path = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/NAARC/'

    # get cfg
    cfg_path = path + 'domain_cfg_zps.nc'
    cfg = xr.open_dataset(cfg_path, chunks=-1).squeeze()
    top_lev = cfg.top_level.load()

    # get mask
    msk_path = path + 'bdy_msk_pybdy.nc'
    msk = xr.load_dataarray(msk_path)
    import matplotlib.pyplot as plt

    msk = xr.where((msk == 0) & (top_lev == 1),  -1, top_lev)
    msk_cut = msk[2660:2790,3765:3933]
    msk[2660:2790,3765:3933] = xr.where(msk_cut == -1, 0, msk_cut)

    # set north fold and closed sea to land
    msk[-1] = 0


    p=plt.pcolor(msk)
    plt.colorbar(p)
    plt.show()
    msk.name = 'mask'

    print (msk)

    msk.to_netcdf(path + 'bdy_msk_verify.nc')
    
adjust_NAARC()
