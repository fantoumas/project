# DMelt Jython example
# See http://jwork.org/dmelt/ 

from java.awt import Color,Font
from jhplot  import * 
from jhplot.shapes  import *

c1 = HPlot("Canvas",600,400)
c1.setGTitle("Title");
c1.visible()
c1.setAutoRange()
