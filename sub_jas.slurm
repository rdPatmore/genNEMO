#!/bin/bash 

#SBATCH --partition=short-serial
#SBATCH -o %j.out 
#SBATCH -e %j.err
#SBATCH --time=01:00:00
#SBATCH --mem=64000

# load pybdy env and java
source Scripts/set_up.sh

# executable 
pybdy -s namelist_AMM15.bdy 

