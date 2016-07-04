#!/bin/bash
# A batch script to run DataMelt without IDE
# DataMelt project: http://jwork.org/dmelt/
# Created by S.Chekanov (science@jwork.org)

# assume DataMelt in the current directory.
export SCAVIS_DIR=../../


args=$#
if [ $args == 0  ]
then
   echo "You did not specify a jython input file!"
   echo "This script runs DataMelt file in batch mode without the IDE editor"
   echo "TYPE: dmelt_batch.sh <file>.py <arguments>"
   exit 1;
fi

JAVA_HEAP_SIZE=1024


# set here home directory where the jehep.jar file is located 
JEHEP_HOME=${SCAVIS_DIR}

arguments="$@"

if which java >/dev/null; then
    _java=java
elif [[ -n "$JAVA_HOME" ]] && [[ -x "$JAVA_HOME/bin/java" ]];  then
    _java="$JAVA_HOME/bin/java"
else
    echo "No java detected! Please install it from https://java.com/download"; exit 0
fi

if [[ "$_java" ]]; then
    version=$("$_java" -version 2>&1 | awk -F '"' '/version/ {print $2}')
    if [[ "$version" < "1.7" ]]; then
        echo "Java version is less than 1.7. Please update it."; exit 0;
    fi
fi

JEHEP_FILE="$JEHEP_HOME"/dmelt.jar
if [ ! -f $FILE ];
then
   echo "DataMelt cannot be detected. Please change the variable SCAVIS_DIR to DataMelt location (with dmelt.jar)"
fi


################## do not edit ###############################
CLASSPATH="."
for i in ${JEHEP_HOME}/lib/*/*.jar
do
      CLASSPATH=$CLASSPATH:"$i"
done

JYTHON_HOME=${JEHEP_HOME}"/lib/jython"
CP=${JYTHON_HOME}"/jython.jar"
if [ ! -z "$CLASSPATH" ]
then
  CP=$CP:$CLASSPATH
fi

OPTJJ="-Dlog4j.configuration=$JEHEP_HOME/log4j.properties -Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.NoOpLog"


$_java  -mx${JAVA_HEAP_SIZE}m  -classpath "$CP" $OPTJJ -Dpython.home=${JYTHON_HOME} \
                     org.python.util.jython ${arguments}

