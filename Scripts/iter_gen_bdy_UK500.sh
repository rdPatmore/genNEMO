
source set_up.sh

bdy_list=("CHAMFER_AMM15_to_UK500_clean")
year=1996

for bdy in ${bdy_list[@]}; do
    echo $bdy
    path="/home/users/ryapat30/NOC/genNEMO/INPUT/${bdy}/"
    cd $path
    for month in {01..12}; do
        echo "$year-$month"
	month_p1=$(date --date "$year-$month-01 +1 month" "+%m")
	year_p1=$(date --date "$year-$month-01 +1 month" "+%Y")
        echo "$year_p1-$month_p1"
	
        cat namelist.template \
            | sed "s,__MONTH0__,$month,g" \
            | sed "s,__MONTH1__,$month,g" \
            | sed "s,__YEAR0__,$year,g" \
            | sed "s,__YEAR1__,$year,g" \
            > namelist.bdy
        cat "src_data.template" \
            | sed "s,__YEAR__,$year,g" \
            | sed "s,__YEAR_p1__,$year_p1,g" \
            | sed "s,__MONTH__,$month,g" \
            | sed "s,__MONTH_p1__,$month_p1,g" \
            > src_data.ncml
    
        pybdy -s namelist.bdy
    done
done
