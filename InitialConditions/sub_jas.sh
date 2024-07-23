#!/bin/bash 

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --threads-per-core=1 

#SBATCH --partition=high-mem
#SBATCH -o %j.out 
#SBATCH -e %j.err
#SBATCH --time=02:00:00
#SBATCH --mem=100G

# executable 
#python -u calc_mld.py
conda activate coast

python -u calc_ini_ts.py
