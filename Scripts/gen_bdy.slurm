#!/bin/bash

#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --mem=500G
#SBATCH --time=12:00:00                    
#SBATCH --account=verify_oce

#JVM="jre-11"
#JVM="jre-1.8.0-openjdk"
#export JAVA_HOME=/usr/lib/jvm/$JVM/
#ls /usr/lib/jvm

./iter_gen_bdy_NAARC.sh
