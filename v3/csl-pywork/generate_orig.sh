#!/bin/bash
# generate (update or initialize) orig/xxx.txt
#  usage: sh generate_orig.sh <dict> <parent-dir>
#  The files are put into <parent-dir>.
#  Copies file from csl-orig repository
if [ -z "$1" ] || [ -z "$2" ]
  then
   echo "usage:  sh generate_orig.sh <dict> <parent-dir>"
   echo "Example: sh generate_orig.sh acc tempparent/acc"
   echo "Example: sh generate_orig.sh acc ../../ACCScan/2020"
   exit 1
  else
    dict=${1^^} # Uppercase
    outdir=$2
fi

dictlo=${dict,,} # Lowercase
dictup=${dict^^} # Uppercase

python3 generate.py "$dict" inventory_orig.txt _ '../csl-orig/${dictlo}' $outdir

