#!/bin/sh
# run this script to get all the methods/functions
# run in in the root main directory
DIR=`pwd`

rm -f allroot.d
# get all clusses 
cd $ROOTSYS/include/
ls -1 *.h  > $DIR"/classes.d" 
cd $DIR

# format
./format_classes.py classes.d
mv -f classes.d.out    classes.d
echo "final file is classes.d is done!" 
