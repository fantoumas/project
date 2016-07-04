@echo off

REM ==================================
REM Batch for starting DataMelt on Windows
REM ==================================

REM ==================================
REM SET JEHEP_HOME TO THE INSTALLATION DIRECTORY 
REM The default is the current directory
REM If you install in in some other location, set it like this 
REM set JEHEP_HOME=C:\DataMelt-1.0\DataMelt


REM current directory
set JEHEP_HOME=.
set JEHEP_HOME_PATH=%CD%
set JYTHON_HOME=%JEHEP_HOME%\lib\jython
echo Current directory %JEHEP_HOME_PATH%


set MAX_JAVA_MEMORY=1024

set CMD_LINE_ARGS=
:args
if "%1"=="" goto start
set CMD_LINE_ARGS=%CMD_LINE_ARGS% %1
shift
goto args
echo ARGS: %CMD_LINE_ARGS%

:start
set JEHEP_JAR=%JEHEP_HOME%
set JEHEP_CLASSPATH=
if exist %JEHEP_JAR% set JEHEP_CLASSPATH=%JEHEP_JAR%

REM take first the main class
set LOCALCLASSPATH=%JEHEP_CLASSPATH%


REM link  LIBRARIES in lib directory
for %%i in ("%JEHEP_HOME%\lib\jehep\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM JYTHON LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\dmisc\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM JYTHON LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\jython\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM FREEHEP LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\freehep\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM JNUMERIC LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\system\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM USER LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\user\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\native\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\update\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\math\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\image\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\nnet\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\physics\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\astro\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\finance\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i
REM UPDATE LIBRARIES
for %%i in ("%JEHEP_HOME%\lib\dbases\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i


SET LIBJEHEP=%JEHEP_HOME%\lib\native\windows-i586

IF EXIST "%programfiles(x86)%" (GOTO 64-Bit) ELSE (GOTO 32-Bit)
:32-Bit
 SET LIBJEHEP=%JEHEP_HOME%\lib\native\windows-i586
 ECHO 32-Bit O/S detected
GOTO END
:64-Bit
  SET LIBJEHEP=%JEHEP_HOME%\lib\native\windows-amd64
  ECHO 64-Bit O/S detected
GOTO END
:END

REM UPDATE NATIVE LIBRARIES
for %%i in ("%LIBJEHEP%\*.jar") do call "%JEHEP_HOME%\lcp.bat" %%i


SET OPTJJ=-Djava.library.path=%LIBJEHEP%
SET OPTJJJ=-Dlog4j.configuration=%JEHEP_HOME%\log4j.properties 
SET OPTJJJ2=-Dorg.apache.commons.logging.Log=org.apache.commons.logging.impl.NoOpLog
 

REM TAKE ALL
set CLASSPATH=%LOCALCLASSPATH%
set LOCALCLASSPATH=

REM pause

ECHO Run file in batch mode ..
REM  java -mx%MAX_JAVA_MEMORY%m -classpath %CLASSPATH% %OPTJJ% %OPTJJJ% %OPTJJJ2% -Djehep.home=%JEHEP_HOME% jehep.utils.RunScript %CMD_LINE_ARGS%
java -classpath %CLASSPATH% %OPTJJ% %OPTJJJ% %OPTJJJ2% -Djehep.home=%JEHEP_HOME% jehep.utils.RunScript %CMD_LINE_ARGS%

