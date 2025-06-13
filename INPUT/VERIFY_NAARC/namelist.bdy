!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
!! NEMO/OPA  : namelist for BDY generation tool
!!
!!             User inputs for generating open boundary conditions
!!             employed by the BDY module in NEMO. Boundary data
!!             can be set up for v3.2 NEMO and above.
!!
!!             More info here.....
!!
!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

!------------------------------------------------------------------------------
!   vertical coordinate
!------------------------------------------------------------------------------
   ln_zco      = .false.   !  z-coordinate - full    steps   (T/F)
   ln_zps      = .true.    !  z-coordinate - partial steps   (T/F)
   ln_sco      = .false.   !  s- or hybrid z-s-coordinate    (T/F)
   rn_hmin     =   -10     !  min depth of the ocean (>0) or
                           !  min number of ocean level (<0)

!------------------------------------------------------------------------------
!   s-coordinate or hybrid z-s-coordinate
!------------------------------------------------------------------------------
   rn_sbot_min =   10.     !  minimum depth of s-bottom surface (>0) (m)
   rn_sbot_max = 7000.     !  maximum depth of s-bottom surface
                           !  (= ocean depth) (>0) (m)
   ln_s_sigma  = .false.   !  hybrid s-sigma coordinates
   rn_hc       =  150.0    !  critical depth with s-sigma

!------------------------------------------------------------------------------
!  grid information
!------------------------------------------------------------------------------
   sn_src_hgr = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/UKESM/domcfg_UKESM1p1_gdept.nc'
   sn_src_zgr = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/UKESM/domcfg_UKESM1p1_gdept.nc
   sn_dst_hgr = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/NAARC/domain_cfg_zps_gdept.nc'
   sn_dst_zgr = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/NAARC/domain_cfg_zps_gdept.nc'
   !sn_src_msk =  '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/UKESM/domcfg_UKESM1p1_gdept.nc' ! has no t,u,v mask
   !sn_src_msk =  '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/UKESM/parent_mask_verify.nc'
   sn_src_msk =  '/gws/nopw/j04/jmmp/jmmp_collab/eORCA025/mesh_mask_eORCA1-GO6.nc'
   sn_bathy   = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/DOM/NAARC/Bathymetry.nc'

!   sn_src_hgr = 'domcfg_UKESM1p1_gdept.nc'
!   sn_src_zgr = 'domcfg_UKESM1p1_gdept.nc
!   sn_dst_hgr = 'domain_cfg_zps_gdept.nc'
!   sn_dst_zgr = 'domain_cfg_zps_gdept.nc'
!   sn_src_msk =  'mesh_mask_eORCA1-GO6.nc'
!   sn_bathy   = 'Bathymetry.nc'

   sn_nme_map = 'grid_name_map.json'     ! json file mapping variable names to netcdf vars

!------------------------------------------------------------------------------
!  I/O
!------------------------------------------------------------------------------
   sn_src_dir = 'src_data.ncml' ! src_files
   sn_dst_dir = '/gws/nopw/j04/verify_oce/NEMO/Preprocessing/LBC/'
   !sn_dst_dir = '.'
   sn_fn      = 'GloSat_NAARC'       ! prefix for output files
   nn_fv      = -1e20                !  set fill value for output files
   nn_src_time_adj = 0               ! src time adjustment
   sn_dst_metainfo = 'GloSat-NAARC'


!------------------------------------------------------------------------------
!  unstructured open boundaries                         

!------------------------------------------------------------------------------
!  unstructured open boundaries
!------------------------------------------------------------------------------
    ln_coords_file = .true.               !  =T : produce bdy coordinates files
    cn_coords_file = 'coordinates.bdy.nc' !  name of bdy coordinates files
                                          !  (if ln_coords_file=.TRUE.)
    ln_mask_file   = .true.              !  =T : read mask from file
    cn_mask_file   = 'bdy_msk_verify.nc' ! name or mask file
                                          !  (if ln_mask_file=.TRUE.)
    ln_dyn2d       = .true.               !  boundary conditions for
                                          !  barotropic fields
    ln_dyn3d       = .true.              !  boundary conditions for
                                          !  baroclinic velocities
    ln_tra         = .true.               !  boundary conditions for T and S
    ln_ice         = .false.              !  ice boundary condition
    ln_zinterp     = .true.               !  vertical interpolation
    nn_rimwidth    = 10                    !  width of the relaxation zone

!------------------------------------------------------------------------------
!  unstructured open boundaries tidal parameters
!------------------------------------------------------------------------------
    ln_tide        = .false.              !  =T : produce bdy tidal conditions
    sn_tide_model  = 'FES2014'            !  Name of tidal model. Accepts FES2014, TPXO7p2, or TPXO9v5
    clname(1)      = 'M2'                 !  constituent name
    clname(2)      = 'S2'
    clname(3)      = 'K2'
    clname(4)      = 'O1'
    clname(5)      = 'P1'
    clname(6)      = 'Q1'
    clname(7)      = 'M4'
    ln_trans       = .true.               !  interpolate transport rather than
                                          !  velocities
	! location of TPXO7.2 data
	sn_tide_grid_7p2   = './inputs/tpxo7.2/grid_tpxo7.2.nc'
	sn_tide_h          = './inputs/tpxo7.2/h_tpxo7.2.nc'
	sn_tide_u          = './inputs/tpxo7.2/u_tpxo7.2.nc'
	! location of TPXO9v5 data: single constituents per file
	sn_tide_grid_9p5   = './inputs/TPXO9_atlas_v5_nc/grid_tpxo9_atlas_30_v5.nc'
	sn_tide_dir        = './inputs/TPXO9_atlas_v5_nc/'
	! location of FES2014 data
	sn_tide_fes        = './inputs/FES2014/'

!------------------------------------------------------------------------------
!  Time information for output
!-----------------------------------------------------------------------------
    sn_date_start   = '1850-01-01'    !  dst output date start YYYY-MM-DD
    sn_date_end     = '1850-02-01'    !  dst output date end YYYY-MM-DD
    sn_dst_calendar = 'gregorian'     !  output calendar format
    sn_date_origin  = '1800-01-01'    !  reference for time counter YYYY-MM-DD
    ln_time_interpolation = .false. !  set to false to use parent
                                   !  calender for monthly frequency only

!    nn_year_000     = 1850           !  year start
!    nn_year_end     = 1850           !  year end
!    nn_month_000    = 1     !  month start (default = 1 is years>1)
!    nn_month_end    = 1     !  month end (default = 12 is years>1)
!    sn_dst_calendar = 'gregorian' !  output calendar format
!    nn_base_year    = 1800           !  base year for time counter
!    ln_time_interpolation = .false. !  set to false to use parent frequency and calender
                                   !  for monthly only

!------------------------------------------------------------------------------
!  Additional parameters
!------------------------------------------------------------------------------
    nn_wei  = 1                   !  smoothing filter weights
    rn_r0   = 0.041666666         !  decorrelation distance use in gauss
                                  !  smoothing onto dst points. Need to
                                  !  make this a funct. of dlon
    sn_history  = 'Benchmarking test case'
                                  !  history for netcdf file
    ln_nemo3p4  = .true.          !  else presume v3.2 or v3.3
    nn_alpha    = 0               !  Euler rotation angle
    nn_beta     = 0               !  Euler rotation angle
    nn_gamma    = 0               !  Euler rotation angle
	rn_mask_max_depth = 100.0     !  Maximum depth to be ignored for the mask
	rn_mask_shelfbreak_dist = 20000.0 !  Distance from the shelf break
