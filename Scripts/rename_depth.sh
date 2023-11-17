for file in ../OUTPUT/*T_y2004m01*; do  ncrename -v deptht,gdept $file; done
for file in ../OUTPUT/*U_y2004m01*; do  ncrename -v depthu,gdepu $file; done
for file in ../OUTPUT/*V_y2004m01*; do  ncrename -v depthv,gdepv $file; done
