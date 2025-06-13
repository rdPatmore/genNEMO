# pyBDY scripts 

A collection of scripts for processing lateral boundary conditions with pyBDY

gen_bdy.slurm
-------------

Batch script for submiting "iter_gen_bdy_[model].sh"

iter_gen_bdy_[model].sh
-----------------------

Iterates over months/years to produce bdy files. Can be run on command line
with `source` or submittied as a batch script with `gen_bdy.slurm`

Edit this file to fit user requirements
