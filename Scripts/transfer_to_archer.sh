path="/gws/nopw/j04/jmmp/ryapat/CHAMFER/GLOSEA6"
year=2023

for grid in {U,V,T}; do
  for m in {01..12}; do
     echo $m
     scp ${path}_atlantic/AMM15_bdy${grid}_y${year}m${m}.nc archer01:/work/n01/n01/shared/CO_AMM15/CHAMFER/BDY/Atlantic/AMM15_bdy${grid}_y${year}m${m}.nc
     scp ${path}_baltic/AMM15_bdy${grid}_y${year}m${m}.nc archer01:/work/n01/n01/shared/CO_AMM15/CHAMFER/BDY/Baltic/AMM15_baltic_bdy_${grid}_y${year}m${m}.nc
  done
done
#rsync -vvv --progress -h ../InitialConditions/glosea*.nc archer01:/work/n01/n01/ryapat01/NEMO/nemo_4.0.4_CO9_tides/cfgs/CO9_AMM15_15c/EXP_FORCE_GLOSEA6/
#scp ../OUTPUT/GLOSEA6_atlantic_alt/coor* archer01:/work/n01/n01/shared/CO_AMM15/CHAMFER/BDY/AtlanticAlt/
