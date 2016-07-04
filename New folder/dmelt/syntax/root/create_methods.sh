#!/bin/sh
# run this script to get all the methods/functions
# run in in the root main directory
DIR=`pwd`


args=$#           # Number of args passed.

if [ $args == 0  ]
then
   echo "did not specify ROOT source directory!"
   exit 1;
fi

SDIR=$1

cd $SDIR

echo "directory to open $SDIR"
# get all clusses 
rm -f $DIR"/methods.d"
rm -f $DIR"/methods.d.out"
grep -i -h -r '(' $SDIR  > $DIR"/methods.d"
cd $DIR

# format
./format_methods.py methods.d
mv -f methods.d.out  methods.d
echo "final file is methods.d is done!" 
