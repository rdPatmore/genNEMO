
source set_up.sh

bdy_list=("GLOSEA6_atlantic" "GLOSEA6_baltic")
year=2023

for bdy in ${bdy_list[@]}; do
    echo $bdy
    path="/home/users/ryapat30/NOC/genNEMO/INPUT/${bdy}/"
    cd $path
    for month in {01..12}; do
        echo "$year-$month"
        cat namelist.template \
            | sed "s,__MONTH0__,$month,g" \
            | sed "s,__MONTH1__,$month,g" \
            | sed "s,__YEAR0__,$year,g" \
            | sed "s,__YEAR1__,$year,g" \
            > namelist.bdy
        cat "src_data.template" \
            | sed "s,__YEAR__,$year,g" \
            | sed "s,__MONTH__,$month,g" \
            > src_data.ncml
    
        pybdy -s namelist.bdy
    done
done
