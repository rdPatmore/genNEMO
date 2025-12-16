path="/gws/ssde/j25a/verify_oce/NEMO/Preprocessing/LBC/OCE/MES_clean3/"
dst="/work/n02/n02/shared/VERIFY/FORCING/BDY/MES_clean3/"
year=1850

for grid in {U,V,T}; do
  for m in {02..12}; do
     echo $m
     scp ${path}GloSat_NAARC_MES_bdy${grid}_y${year}m${m}.nc archer30:${dst}
  done
done
#for grid in {T,}; do
#  for m in {01,}; do
#     echo $m
#     scp ${path}ICE/GloSat_NAARC_bdy${grid}_y${year}m${m}.nc archer30:${dst}/GloSat_NAARC_bdyI_y${year}m${m}.nc
#  done
#done
#scp ${path}coor* archer30:${dst}
#scp ${path}ICE/coor* archer30:${dst}ICE/
