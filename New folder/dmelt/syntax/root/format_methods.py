#!/usr/local/bin/python
import sys
import os
import fileinput
import string
from  sets import Set

# make python faster
try:
  print "####  import psyco module! ##### "
  import psyco
  psyco.full()
except ImportError:
     pass


methods = Set();


if len(sys.argv)<2:
   print "usage: format.py <input file>"
   print "produced output is <input file>.out"
else:
   myfile=sys.argv[1]
#  myfile = raw_input("Please enter file name: ")
# do check 
   try:
     fi = open(myfile, 'r')
     fi.close()
   except IOError:
        print 'Can\'t open file for reading.'
        sys.exit(0)

   print "File opened ",  myfile
   fi = open(myfile+".out", 'w')
   for line in fileinput.input([myfile]):


       line = line.lstrip();

#  remove everything after (
       lineno1=string.find(line, "(")
       line1=line[0:lineno1]
       line=line1;

# split 
       words = string.split(line," ")

# reverse 
       words.reverse()

# first word
       line=words[0];
       line = line.lstrip();

# first character
       first=line[0:1]; 

# second
       second=line[1:2];

#
       leno2=string.find(line, ">")

#
       leno3=string.find(line, ".")

#
       leno4=string.find(line, ":")

#
       leno5=string.find(line, "_")

#
       leno6=string.find(line, "/")

#
       leno7=string.find(line, "#")

#
       leno8=string.find(line, "+")

#
       leno9=string.find(line, "*")


       if (first.isupper() and second.islower() and leno2 == -1 and leno3 == -1 and leno4 == -1 and  leno5 == -1 and leno6 == -1 and leno7 == -1 and leno8 == -1 and leno9 == -1 and first !="T") :
#        line="   cxxKeywords.add(\""+line+"\",Token.KEYWORD2);"+"\n"
        line=line+"\n"

        # end  to set
        methods.add(line);


# fill file 
#        fi.write( line );
# close file    
   print "Set is done!"
#   fi.close()


# sort it and make a file 
for k in sorted(set(methods)):
         fi.write( k );
print "file closed", myfile+".out"
fi.close()


# f = open(myfile, 'r')    # Returns a file object
# line = f.readline()    # Invokes readline() method on file
# while line:
#    print line,    # trailing ',' omits newline character
#    line = f.readline()
# f.close()
