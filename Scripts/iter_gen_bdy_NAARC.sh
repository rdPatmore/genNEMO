
source set_up.sh

bdy_list=("VERIFY_NAARC")
year=1850

for bdy in ${bdy_list[@]}; do
    echo $bdy
    path="/home/users/ryapat30/NOC/genNEMO/INPUT/${bdy}/"
    cd $path
    echo "$year"
    year_p1=$(date --date "$year-01-01 +1 year" "+%Y")
    echo "$year_p1"
    
    cat namelist.template \
        | sed "s,__YEAR0__,$year,g" \
        | sed "s,__YEAR1__,$year,g" \
        > namelist.bdy
    cat "src_data.template" \
        | sed "s,__YEAR__,$year,g" \
        | sed "s,__YEAR_p1__,$year_p1,g" \
        > src_data.ncml
    
    pybdy -s namelist.bdy
done
