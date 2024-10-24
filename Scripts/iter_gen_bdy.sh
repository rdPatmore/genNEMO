
source set_up.sh

bdy="GLOSEA6_atlantic"
#bdy="GLOSEA6_baltic"
path="../INPUT/${bdy}/"
cd $path
year=2001

for month in {01..12}; do
        echo "$year-$month"
        cat namelist_AMM15.template \
            | sed "s,__MONTH0__,$month,g" \
            | sed "s,__MONTH1__,$month,g" \
            | sed "s,__YEAR0__,$year,g" \
            | sed "s,__YEAR1__,$year,g" \
            > namelist_AMM15.bdy
        cat "GloSea6.template" \
            | sed "s,__YEAR__,$year,g" \
            > GloSea6.ncml
    
        pybdy -s namelist_AMM15.bdy
done
