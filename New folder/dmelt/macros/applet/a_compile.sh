#!/bin/bash

args=$# 
if [ $args == 0  ]
then
   echo "did not specify input file!"
   exit 1;
fi

for i in lib/*/*.jar
do
      CLASSPATH=$CLASSPATH:"$i"
done

CP=$CP:$CLASSPATH
javac -classpath "$CP" $1

echo "File $1 compiled!" 
