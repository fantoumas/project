#!/bin/bash

echo "run jHepWork file in batch mode without the editor"
echo "TYPE: a_run.sh <file>.py"

 
# set here home directory where the jehep.jar file is located 
JHPLOT_HOME="../../../jehep"


FILE=$1

################## do not edit ###############################
JAVA_HEAP_SIZE=128


CLASSPATH="."


# Add in your .jar files first
for i in $JHPLOT_HOME/lib/*.jar
do
      CLASSPATH=$CLASSPATH:"$i"
done

 # Add in your .jar files first
for i in $JHPLOT_HOME/lib/*/*.jar
do
      CLASSPATH=$CLASSPATH:"$i"
done


# convert the unix path to windows
if [ "$OSTYPE" = "cygwin32" ] || [ "$OSTYPE" = "cygwin" ] ; then
   CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
fi


# run file
java -Dpython.home="$JYTHON_HOME" -classpath "$CLASSPATH" \
                           org.python.util.jython $FILE
