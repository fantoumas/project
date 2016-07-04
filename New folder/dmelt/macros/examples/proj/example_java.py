# Jython glue file to call java classes.

import jreload;
def xp(name): 
   return os.path.join(sys.prefix, SetEnv.ProjDir+SetEnv.fSep+name)

X=jreload.makeLoadSet('X',[xp('.'),xp('classes.jar')])
from X import example2
# print dir(example2)
from X.example2 import *
jreload.reload(X) 


# call Java class Calc from example2
a=Calc()
b=a.doSomething()
print "output from class Calc=\n",b
