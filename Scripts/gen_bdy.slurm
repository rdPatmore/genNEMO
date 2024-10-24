#!/bin/bash

#SBATCH --partition=short-serial
#SBATCH --mem=64GB
#SBATCH --time=06:00:00                    

./iter_gen_bdy.sh
