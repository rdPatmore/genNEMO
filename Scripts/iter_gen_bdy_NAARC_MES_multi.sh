
bdy_list=("VERIFY_NAARC_ICE")

for year in {1962,}; do
   echo $year
   for bdy in ${bdy_list[@]}; do
       echo $bdy
       sbatch gen_bdy.slurm $year $bdy	
   done
done
