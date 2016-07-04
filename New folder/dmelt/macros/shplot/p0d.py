from jhplot  import P0D





def _getnew(t1, t2, what):
     	"""Build a title after operation"""

        className  = t2.__class__.__name__
     
        title=t1.getTitle()
        if  className =='p0d':
    	   title="("+t1.getTitle()+") " + what+" "+t2.getTitle()
        else: 
           title="("+t1.getTitle()+") " + what+" "+str(t2)
    
    	return title

"""

A one-dimensional array.
The constructor: 
p0d() - default title, shallow copies for operations (i.e.
no new objects are created for +,-,*,-)

p0d(title) -  new title,shallow copies for operations

p0d(title,0) -  new title, new object copies for operations.
p0d(title,1) -  new title, shallow copies  for operations.

S.Chekanov (ANL)

"""



__author__  = 'S.Chekanov"'
__version__ = 1.0


class p0d(P0D):

    __shallow=1     # defaul is shallow
    __title="not set"

    def __init__(self,title=None,shallow=None,other=None):
          
    
              
              if shallow != None:
              	              self.__shallow=shallow
              	              
              
              if title != None:
              	              self.__title=title              
               	              
              	              
              className  = other.__class__.__name__
              #print "Other=", className
               
              if  other == None:
                  P0D.__init__(self,self.__title) 
              else:
              	  P0D.__init__(self,title,self.__shallow,other)
              	   
     
     
    
    
    def __add__(self, x):
    	"""Add 2 P0D objects"""
    	_w='+'
        self = self.oper(x,_w)
        return p0d(_getnew(self, x, _w),self.__shallow,self)
    
    def __sub__(self, x):
    	"""Subtract 2 P0D"""
    	_w='-'
        self = self.oper(x,_w)
        return p0d(_getnew(self, x, _w),self.__shallow,self)
        
    def __mul__(self, x):
    	"""multiply 2 P0D or scale by a scale factor"""
        className  = x.__class__.__name__
        _w='*'
         
        if  className =='p0d':
             # print 'multiply objects'
              self = self.oper(x,_w)
        else:
             # print 'scale objects scale='+str(x)    
             self = self.operScale(x)
             
        return p0d(_getnew(self, x, _w),self.__shallow,self)


    def __div__(self, x):
        """divide 2 P0D or scale by 1/scale"""
        
        className  = x.__class__.__name__
        _w='/'
         
        if  className =='p0d':
             # print 'divide objects'
              self = self.oper(x,_w)
        else:
             # print 'scale objects scale='+str(x)    
             self = self.operScale(1.0/x)
             
        return p0d(_getnew(self, x, _w),self.__shallow,self)
  
    def copy(self):
        """ Copy """
        return p0d(self.getTitle(),self.__shallow,self)  
    
    def __merge__(self,x):
        """ Merge 2 P0D """
        self=self.merge(x)
        return p0d(_getnew(self, x, ' merged'),self.__shallow,self)  
   

    def __del__(self):
        """clear"""
        self.clear()
 
    def range(self,ix,iy):
        """ Get subrange in index """   
        self=self.range(ix,iy)
        return p0d(self.getTitle()+' in range',self.__shallow,self)
    
    def range(self,min,max):
        """ Get range """
        self=self.range(min,max)
        return p0d(self.getTitle()+' in range',self.__shallow,self)


if __name__ == '__main__':


    p1=p0d("test")
    p1.add(2)
    p1.add(4)
    print "title=",p1.getTitle()
    
    p2=p0d("new")
    p2.add(8)
    p2.add(5)
    print "title=",p2.getTitle()
    
    p3=p2*2
    print "title=",p3.getTitle()
