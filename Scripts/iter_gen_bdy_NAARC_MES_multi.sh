
bdy_list=("VERIFY_NAARC_MES")

for year in {1967..1969}; do
   echo $year
   for bdy in ${bdy_list[@]}; do
       echo $bdy
       sbatch gen_bdy.slurm $year $bdy	
   done
done
