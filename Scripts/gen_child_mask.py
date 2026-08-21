import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

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

def gsr36():
    """ 
    Create mask that defines location of bdy forcing for GSR36
    """

    root = '/gws/ssde/j25a/verify_oce/NEMO/'
    path = root + 'Preprocessing/DOM/GSR36/'

    # get cfg
    cfg_path = path + '1_domain_cfg.nc'
    mask = xr.open_dataset(cfg_path).top_level.squeeze()
    mask.name = 'mask'
    
    # 0 is land 
    # 1 is ocean
    # -1 is edge of domain
    
    # make mask for bdy (pyBdy searches for boundary between -1 and 1)
    mask.loc[0,:] = -1
    mask.loc[-1,:] = -1
    mask.loc[:,-1] = -1
    mask.loc[:,0] = -1
    
    mask.to_netcdf('bdy_msk_gsr36.nc')


def adjust_NAARC(coord="mes"):
    
    # path 
    root = '/gws/nopw/j04/verify_oce/NEMO/'
    root = '/gws/nopw/j04/cis_collapse/Users/ryapat30/'
    path = root + 'Preprocessing/DOM/NAARC/'

    # get cfg
    cfg_path = path + 'domain_cfg_mes.nc'
    cfg = xr.open_dataset(cfg_path, chunks=-1).squeeze()
    top_lev = cfg.top_level.load()

    # get mask
    msk_path = path + 'bdy_msk_pybdy.nc'
    msk = xr.load_dataarray(msk_path)

    fig, axs = plt.subplots(1,4, figsize=(10,4))
    p=axs[0].pcolormesh(msk)
    msk = xr.where((msk == 0) & (top_lev == 1),  -1, top_lev)
    axs[1].pcolormesh(msk)

    # remove black sea extension
    msk_cut = msk[2660:2790,3765:3933]
    msk[2660:2790,3765:3933] = xr.where(msk_cut == -1, 0, msk_cut)

    if coord == "mes":
        # remove great lakes
        msk_cut = msk[2600:2770,2300:2550]
        msk[2600:2770,2300:2550] = xr.where(msk_cut == -1, 0, msk_cut)

        # remove caspian sea 
        msk_cut = msk[2520:2838,3980:4107]
        msk[2520:2838,3980:4107] = xr.where(msk_cut == -1, 0, msk_cut)

        # remove afrian lake (niasu? Victoria?)
        msk_cut = msk[1950:2100,3820:3870]
        msk[1950:2100,3820:3870] = xr.where(msk_cut == -1, 0, msk_cut)
        
    axs[2].pcolormesh(msk)

    # set north fold and closed sea to land
    msk[-1] = 0

    axs[3].pcolormesh(msk)
    plt.colorbar(p)
    #plt.show()

    msk.name = 'mask'


    msk.to_netcdf(path + 'bdy_msk_mes_verify.nc')

def adjust_NAARC_ice():

    # path 
    path = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/NAARC/'

    # get mask
    msk_path = path + 'bdy_msk_verify.nc'
    msk = xr.load_dataarray(msk_path, drop_variables=["x","y"])
    
    # set atlantic into out of bounds
    msk[:,2000:] = xr.where(msk[:,2000:] == 1, -1, msk[:,2000:])

    # cut boundaries
    # pybdy needs dst grid to be smaller than parent if not cyclic data
    #msk = msk[10:-10,10:-10]

    # set north fold
    msk[-1] = 0

    msk.to_netcdf(path + 'bdy_msk_verify_ice.nc')

def find_diff_in_zps_and_mes():
    """
    plot difference between the zps and mes masks
    """

    root = '/gws/nopw/j04/cis_collapse/Users/ryapat30/'
    path = root + 'Preprocessing/DOM/NAARC/'
    mes = xr.open_dataarray(path + "bdy_msk_mes_verify.nc")
    zps = xr.open_dataarray(path + "bdy_msk_verify.nc")

    diff = mes - zps

    print (diff.sum().values)
    fig, axs = plt.subplots(3)
    axs[0].pcolormesh(mes)
    axs[1].pcolormesh(zps)
    axs[2].pcolormesh(diff)
    plt.show()
    
#find_diff_in_zps_and_mes()
#adjust_NAARC()
gsr36()
