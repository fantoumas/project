"""
Interface function to Jaida IFunction
This allows you to define your custom functions as:

from ifunc import *

class cmt(ifunc):
   def value(self, v):
      d=self.p[0]*v[0]*v[0]+self.p[1]
      return d
 
p=cmt('test',['x'],['a','b']) 
# p=cmt('test',1,2) 
print p.dimension() 
print p.numberOfParameters()
print p.parameterNames()
print p.variableNames() 
print p.variableName(0)
# p.setParameter('par0', 10) 
p.setParameters([20,30])
print p.value([30])


S.Chekanov (ANL)
"""

from hep.aida.ref.function import AbstractIFunction

class ifunc(AbstractIFunction):
   "Interface function to Jaida IFunction" 
   def __init__(self):
      AbstractIFunction.__init__(self)
   def __init__(self,title,names,pars):
      AbstractIFunction.__init__(self,title,names,pars)
      self.p=self.parameters()
   def __init__(self,title,dimension, number_param):
      AbstractIFunction.__init__(self,title,dimension,number_param) 
      self.p=self.parameters() 
   def value(self, v):
      return 0.0
