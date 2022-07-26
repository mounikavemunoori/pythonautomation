#!/bin/sh

echo "Hello world"
ls
VAR1=docker ps
echo $VAR1
BASEPATH=$(pwd)
echo $BASEPATH

SUBFOLD1=${BASEPATH%%/}/xlread1.xlsx
SUBFOLD2=${BASEPATH%%/}/subFold2

echo $SUBFOLD1
python getContainerID.py

