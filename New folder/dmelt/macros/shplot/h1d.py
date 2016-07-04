from jhplot  import H1D




def _getnew(t1, t2, what):
     	"""Build a title after operation"""

        className  = t2.__class__.__name__
     
        title=t1.getTitle()
        if  className =='h1d':
    	   title="("+t1.getTitle()+") " + what+" "+t2.getTitle()
        else: 
           title="("+t1.getTitle()+") " + what+" "+str(t2)
    
    	return title




"""

Jython main class to build a histogram
S.Chekanov (ANL)

"""
class h1d(H1D):


    def __init__(self,title=None,bins=None,min=0,max=1):
              """ build a histogram """      

        
              className  = bins.__class__.__name__  

              if title != None:
                              self.__title=title
 
              if  className == 'int':
                  H1D.__init__(self,self.__title,bins,min,max) 
              else:
                  H1D.__init__(self,self.__title,bins)
              	   
    
              
    def __str__(self, x):
        return self 
  
  
    def java(self):
        """ Return java superclass instance"""
        return self.class.superclass
   
  
 
    def __add__(self, x):
    	"Add 2 histograms"
    	_w='+'
        self = self.oper(x,_w)
        return  h1d(_getnew(self, x, _w),self)
   
    def __sub__(self, x):
    	"Subtract 2 histograms"
    	_w='-'
        self = self.oper(x,_w)
        return h1d(_getnew(self, x, _w),self)
        
    def __mul__(self, x):
        "Multiply 2 histograms or scale by a number"
        
        _w='*'
        className  = x.__class__.__name__
        s=self.getTitle()
        # print className
        # if not isinstance(x,int):
        #              print 'not integer', type(x)

        if  className =='h1d':
              # print 'multiply objects'
              self = self.oper(x,s,_w)
        else:
             # print 'scale objects scale='+str(x)
             self = self.operScale(s,x)
       
        return h1d(_getnew(self, x, _w),self)
  
    def __div__(self, x):
        "Divide 2 histograms or divide by a number"
        
        _w='/'
        className  = x.__class__.__name__
        s=self.getTitle()
        
        if  className =='h1d':
              # print 'multiply objects'
              self = self.oper(x,s,_w)
        else:
             # print 'scale objects scale='+str(x)
             self= self.operScale(s,1.0/x)

        return h1d(_getnew(self, x, _w),self)

   
    
    
    
    
if __name__ == '__main__':

    
    p1=h1d("test",20,0.0,200)
    print "title=",p1.getTitle()
    
    p2=h1d("new",20,0.0,200)
    print "title=",p2.getTitle()
    
    p3=p1*p2
    print "title=",p3.getTitle()

