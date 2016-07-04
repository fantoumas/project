#!/bin/bash

# assume this script in this directory
export JEHEP_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


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


# set jython home
export JYTHON_HOME=$JEHEP_HOME"/lib/jython"
 
################## do not edit ###############################
JAVA_HEAP_SIZE=1024
CLASSPATH=$JEHEP_HOME:$CLASSPATH


# Add in your .jar files first
for i in $JEHEP_HOME/lib/*/*.jar
do
      CLASSPATH="$i":$CLASSPATH
done

LIBJEHEP=$JEHEP_HOME"/lib/native/linux-i586/"
OS=`uname`
arch=`uname -m`


if [ "$OS" = "Darwin" ]; then
  echo "Running on Mac.."
  LIBJEHEP=$JEHEP_HOME"/lib/native/macosx/"
fi

if [ "$OS" == "Linux" ]; then
if  [ $arch = i386 ]; then
            LIBJEHEP=$JEHEP_HOME"/lib/native/linux-i586/"
            echo "Running on Linux i386 .."
     elif [ $arch = "i486" ]; then
            LIBJEHEP=$JEHEP_HOME"/lib/native/linux-i586/"
            echo "Running on Linux i486 .."
     elif [ $arch = "i586" ]; then
            LIBJEHEP=$JEHEP_HOME"/lib/native/linux-i586/"
            echo "Running on Linux i586 .."          
     elif [ $arch = "i686" ]; then
            LIBJEHEP=$JEHEP_HOME"/lib/native/linux-i586/"
            echo "Running on Linux i686 .."
     elif [ $arch = "x86_64" ]; then
            LIBJEHEP=$JEHEP_HOME"/lib/native/linux-amd64/"
            echo "Running on Linux x86_64 .."
     else
        echo "Unsupported Architecture"
fi
fi

# some computers may run 32 bit java even on 64 bit
if [ $arch = "x86_64" ]; then
  $_java -d64 -version > /tmp/log_jhepwork 2>&1
  javacheck=`cat /tmp/log_jhepwork`
  if `echo ${javacheck} | grep "not supported" 1>/dev/null 2>&1`
  then
    LIBJEHEP=$JEHEP_HOME"/lib/native/linux-i586/"
    echo "Running a 32-bit JVM "
  else
    echo "Running a 64-bit JVM " 
fi
fi

# Add in your .jar files first
for i in $LIBJEHEP/*.jar
do
      CLASSPATH=$CLASSPATH:$i
done




# convert the unix path to windows
if [ "$OSTYPE" = "cygwin32" ] || [ "$OSTYPE" = "cygwin" ] ; then
   CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
fi

OPTJJ="-Dlog4j.configuration=$JEHEP_HOME/log4j.properties -Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.NoOpLog"

$_java -mx${JAVA_HEAP_SIZE}m -cp $CLASSPATH $OPTJJ -Dpython.home=${JYTHON_HOME} -Djehep.home=$JEHEP_HOME jport.Main $1 &
