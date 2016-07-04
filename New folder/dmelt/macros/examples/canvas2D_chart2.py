# 2D Plots |  C | 1.7 | S.Chekanov | Charts based on the HChart

from java.awt import Color
from java.awt import Font
from java.util import Random
from jhplot  import *
from math  import * 

c1 = HChart("Canvas",600,400, 2, 1)
c1.setGTitle("Chart examples")
c1.visible()


# new plot
c1.cd(1,1)
c1.setChartLine()
c1.setName("Line example")
c1.valueLine(1.0, "First", "category1");
c1.valueLine(2.0, "First", "category2");
c1.valueLine(10.0, "First", "category3");
c1.valueLine(8.0, "First", "category3");

c1.valueLine(3.0, "Second", "category1");
c1.valueLine(2.8, "Second", "category2");
c1.valueLine(4.0, "Second", "category3");
c1.valueLine(1.0, "Second", "category3");
c1.update()



# new plot. Fill a  histogram
h1=H1D("histogram",20,-2,2) 
h1.setFillColor(Color.blue)
rand = Random()
for i in range(1000):
	h1.fill(rand.nextGaussian())

c1.cd(2,1)
c1.setName("Histogram example")
c1.setRange(0,-2,2)
c1.setRange(1,0,100)
c1.add(h1)
c1.update()



c1.export("a.pdf")
# export to some image (png,eps,pdf,jpeg...)
# c1.export(Editor.DocMasterName()+".png")


