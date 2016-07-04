#!/bin/bash

args=$# 
if [ $args == 0  ]
then
   echo "did not specify input file!"
   exit 1;
fi
CURRENT_DIR=`pwd`

for i in $CURRENT_DIR/lib/*/*.jar
do
      CLASSPATH=$CLASSPATH:"$i"
done

CP=$CP:$CLASSPATH
java -classpath "$CP" $1 
