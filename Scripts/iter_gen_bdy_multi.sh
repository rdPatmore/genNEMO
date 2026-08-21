
bdy_list=("VERIFY_GSR36_ZPS")

for year in {1850,}; do
   echo $year
   for bdy in ${bdy_list[@]}; do
       echo $bdy
       sbatch gen_bdy.slurm $year $bdy	
   done
done
