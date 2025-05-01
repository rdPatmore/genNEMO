#!/bin/bash 

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --threads-per-core=1 

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH -o %j.out 
#SBATCH -e %j.err
#SBATCH --time=12:00:00
#SBATCH --mem=300G
#SBATCH --account=jmmp

# executable 
#python -u calc_mld.py
conda activate generic

python -u calc_ini_ts.py
