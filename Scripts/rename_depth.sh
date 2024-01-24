for file in ../OUTPUT/GLOSEA6/*T_y2004m01*; do  ncrename -v deptht,gdept $file; done
for file in ../OUTPUT/GLOSEA6/*U_y2004m01*; do  ncrename -v depthu,gdepu $file; done
for file in ../OUTPUT/GLOSEA6/*V_y2004m01*; do  ncrename -v depthv,gdepv $file; done
