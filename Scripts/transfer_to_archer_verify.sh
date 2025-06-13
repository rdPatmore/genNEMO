path="/gws/nopw/j04/verify_oce/NEMO/Preprocessing/LBC/"
dst="/work/n02/n02/ryapat30/nemo/nemo_4.2.3/cfgs/NAARC/EXP_minimal/FORCING/"
year=1850

for grid in {U,V,T}; do
  for m in {01,}; do
     echo $m
     scp -v ${path}GloSat_NAARC_bdy${grid}_y${year}m${m}.nc archer30:${dst}
  done
done
scp ${path}coor* archer30:${dst}
