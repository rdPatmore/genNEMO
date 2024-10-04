year=1995
path="/gws/nopw/j04/jmmp/ryapat/CHAMFER/GLOSEA6"
for file in ${path}_atlantic/*T_y${year}*; do  ncrename -v deptht,gdept $file; done
for file in ${path}_atlantic/*U_y${year}*; do  ncrename -v depthu,gdepu $file; done
for file in ${path}_atlantic/*V_y${year}*; do  ncrename -v depthv,gdepv $file; done
for file in ${path}_baltic/*T_y${year}*; do  ncrename -v deptht,gdept $file; done
for file in ${path}_baltic/*U_y${year}*; do  ncrename -v depthu,gdepu $file; done
for file in ${path}_baltic/*V_y${year}*; do  ncrename -v depthv,gdepv $file; done
