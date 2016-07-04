from jhplot  import HPlot,H1D,P1D


"""

Build  the main HPlot canvas
S.Chekanov (ANL)

"""

__author__  = 'S.Chekanov"'
__version__ = 1.0

__all__ = ['cd', 'draw', 'range', 'auto', 'clear']

class hplot(HPlot):

    def __init__(self,title,n1,n2):
        """ build a canvas """
        #self.j = HPlot(title,600,400,n1,n2)       
        HPlot.__init__(self,title,600,400,n1,n2) 

    def show(self):
    	"""Show a canvas"""    
        self.visible()
        self.setAutoRange()

    def __del__(self):
    	"""remove"""
        self.close()
   
 
    def __str__(self, x):
         return self.getTitle() 

    def __add__(self, x):
    	"""add a data object to the canvas and show it"""
        self.draw(x)
        return self 
         
    def range(self, xmin, xmax, ymin, ymax):
    	 """Set range in Xmin,Xmax,Ymin,Ymax"""
         self.j.setAutoRange(0)
         self.j.setRange(xmin, xmax, ymin, ymax)
         return self
                   
    def auto(self):
    	 """Set autorange"""
         self.setAutoRange(1)
        

if __name__ == '__main__':
   """ TEST PROGRAM """
   from shplot import h1

   c1=hplot("scripting",1,2)
   c1.visible()
   h1=h1d("histogram1",200,-5,5)
   h2=h1d("ham2",200,-5,5)
   h1.j.setFill(1)
   h1.j.setColor(Color.red)
   rand = Random()
   # fill histogram
   for i in range(500):
      h1.j.fill(rand.nextGaussian())
      h2.j.fill(0.2*rand.nextGaussian())

   # add 2 histograms
   h1=h1+h2
   # show 2
   c1+h1+h2

   # scale by factor 2
   h1=h1*2
   c1.cd(1,2)
   # c1.draw(h1)
   c1+h1


