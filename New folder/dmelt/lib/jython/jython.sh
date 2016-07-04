#!/bin/bash

REQUIRED_VERSION=7
VER=`java -version 2>&1 | grep "java version" | awk '{print $3}' | tr -d \" | awk '{split($0, array, ".")} END{print array[2]}'`


# check java version
if [[ $VER -lt $REQUIRED_VERSION ]]; then
    echo "-> Detected java version $VER"
    echo "-> Java version is lower than required  1.$REQUIRED_VERSION"
    echo "-> Consider using jHepWork 3.4 compiled using  Java 1.6. Exit now!"
    exit;
fi



# set here home directory where the jehep.jar file is located 
# JEHEP_HOME=`pwd`
export JEHEP_HOME=../


export JYTHON_HOME=`pwd`
 
################## do not edit ###############################
JAVA_HEAP_SIZE=512
CLASSPATH=$JEHEP_HOME:$CLASSPATH


# Add in your .jar files first
for i in $JEHEP_HOME/*/*.jar
do
      CLASSPATH="$i":$CLASSPATH
done



OPTJJ="-Djava.library.path=$LIBJEHEP"
java -mx${JAVA_HEAP_SIZE}m -cp $CLASSPATH $OPTJJ -Dpython.home=${JYTHON_HOME} \
     org.python.util.jython
