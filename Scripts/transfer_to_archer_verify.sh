#path="/gws/ssde/j25a/verify_oce/NEMO/Preprocessing/LBC/OCE/MES_clean3/"
#dst="/work/n02/n02/shared/VERIFY/FORCING/BDY/MES_clean3/Transient/"
path="/gws/ssde/j25a/verify_oce/NEMO/Preprocessing/LBC/OCE/ZPS/"
dst="/work/n02/n02/shared/VERIFY/FORCING/BDY/zlevel/"

for grid in {U,V,T}; do
  for y in {1860..1869}; do
    for m in {01..12}; do
      echo $m
      #scp ${path}GloSat_NAARC_bdy${grid}_y${y}m${m}.nc archer30:${dst}
      scp ${path}GloSat_NAARC_bdy${grid}_y${y}m${m}.nc archer30:${dst}
    done
  done
done

#path="/gws/ssde/j25a/verify_oce/NEMO/Preprocessing/LBC/"
#for grid in {T,}; do
#  for y in {1860..1869}; do
#    for m in {01..12}; do
#      echo $m
#      scp ${path}ICE/GloSat_NAARC_bdy${grid}_y${y}m${m}.nc archer30:${dst}/GloSat_NAARC_bdyI_y${y}m${m}.nc
#    done
#  done
#done

#scp ${path}coor* archer30:${dst}
#scp ${path}ICE/coor* archer30:${dst}ICE/
