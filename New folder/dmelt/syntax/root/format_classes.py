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
# ...your code here...



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

# move to unicode 
#     line.unicode(line)
#     line=line.encode('utf8')

# replace 
      old_text=".h"
      new_text="" 
      line=line.replace( old_text, new_text)

      old_text="\n"
      new_text=""
      line=line.replace( old_text, new_text)

      line = line.lstrip();


#      line="  cxxKeywords.add(\""+line+"\",Token.KEYWORD1);"+"\n" 
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
