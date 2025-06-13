year=2019
path="/gws/nopw/j04/jmmp/ryapat/CHAMFER/GLOSEA6"
for file in ${path}_atlantic/*T_y${year}*; do  ncrename -v deptht,gdept $file; done
echo "done 1"
for file in ${path}_atlantic/*U_y${year}*; do  ncrename -v depthu,gdepu $file; done
echo done 2
for file in ${path}_atlantic/*V_y${year}*; do  ncrename -v depthv,gdepv $file; done
echo done 3
for file in ${path}_baltic/*T_y${year}*; do  ncrename -v deptht,gdept $file; done
echo done 4
for file in ${path}_baltic/*U_y${year}*; do  ncrename -v depthu,gdepu $file; done
echo done 5
for file in ${path}_baltic/*V_y${year}*; do  ncrename -v depthv,gdepv $file; done
echo done 6
