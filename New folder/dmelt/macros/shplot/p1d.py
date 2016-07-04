from jhplot  import P1D





def _getnew(t1, t2, what):
     	"""Build a title after operation"""

        className  = t2.__class__.__name__
     
        title=t1.getTitle()
        if  className =='p1d':
    	   title="("+t1.getTitle()+") " + what+" "+t2.getTitle()
        else: 
           title="("+t1.getTitle()+") " + what+" "+str(t2)
    
    	return title

"""
A data holder to keep data in X and Y (with 8 errors).
All operatons like +,-,*,/ only involve operations on  Y component
with proper error propogation (assuming no correlations
between 2 data holders).
See P1D java class for more options.
S.Chekanov (ANL)

"""



__author__  = 'S.Chekanov"'
__version__ = 1.0


class p1d(P1D):

    __shallow=0     # defaul is not shallow 
    __title="not set"

    def __init__(self,title=None,shallow=None,other=None):
          
    
              
              if shallow != None:
              	              self.__shallow=shallow
              	              
              
              if title != None:
              	              self.__title=title              
               	              
              	              
              className  = other.__class__.__name__
              #print "Other=", className
               
              if  other == None:
                  P1D.__init__(self,self.__title) 
              else:
              	  P1D.__init__(self,self.__title,self.__shallow,other)
              	  self.setTitle(self.__title)
 
    def __del__(self):
        """clear"""
        self.clear()
    
    def __add__(self, x):
    	"""Add 2 P1D objects"""
    	_w='+'
        self = self.oper(x,_w)
        return p1d(_getnew(self, x, _w),self.__shallow,self)

    def __sub__(self, x):
    	"""Subtract 2 P1D"""
    	_w='-'
        self = self.oper(x,_w)
        return p1d(_getnew(self, x, _w),self.__shallow,self)
        
    def __mul__(self, x):
    	"""multiply 2 P1D or scale by a scale factor"""
        className  = x.__class__.__name__
        _w='*'
         
        if  className =='p1d':
             # print 'multiply objects'
              self = self.oper(x,_w)
        else:
             # print 'scale objects scale='+str(x)    
             self = self.operScale(1,x)
             
        return p1d(_getnew(self, x, _w),self.__shallow,self)


    def __div__(self, x):
        """divide 2 P1D or scale by 1/scale"""
        
        className  = x.__class__.__name__
        _w='/'
         
        if  className =='p1d':
             # print 'divide objects'
              self = self.oper(x,_w)
        else:
             # print 'scale objects scale='+str(x)    
             self = self.operScale(1,1.0/x)
             
        return p1d(_getnew(self, x, _w),self.__shallow,self)
  
    def copy(self):
        """ Copy """
        return p1d(self.getTitle(),self.__shallow,self)  
    
    def __merge__(self,x):
        """ Merge 2 P1D """
        self=self.merge(x)
        return p1d(_getnew(self, x, ' merged'),self.__shallow,self)  
    
    def range(self,ix,iy):
        """ Get subrange in index """   
        self=self.range(ix,iy)
        return p1d(self.getTitle()+' in range',self.__shallow,self)
    
    def range(self,min,max):
        """ Get range """
        self=self.range(min,max)
        return p1d(self.getTitle()+' in range',self.__shallow,self)


if __name__ == '__main__':


    p1=p1d("test")
    p1.add(2,2)
    p1.add(4,8)
    print "title=",p1.getTitle()
