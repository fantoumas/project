# Plots/2D | P | 1.0 | S.Chekanov |  Two charts based on the HChart

"""
This example shows 2 functions and data sets:
$$
2*x*cos(x)
$$

and

$$
0.2*x*x*sin(x)
$$
"""


from java.awt import Color
from java.awt import Font
from java.util import Random
from math  import *
from jhplot import *

c1 = HChart("Canvas",600,400, 2, 1)
c1.setGTitle("Functions and points")
c1.visible()


c1.cd(1,1)
c1.setName("XY example")
c1.setNameX("weeks")
c1.setNameY("density")
p1= P1D("test 1")
p2= P1D("test 2")

# fill
rand = Random() 
for i in range(10):
      x=4.0*i # x-value
      p1.add(i*4, 10.0*rand.nextGaussian());
      p2.add(i*2, 5.0*rand.nextGaussian());  

c1.add(p1)
c1.add(p2)
c1.update()


# new plot
c1.cd(2,1)
c1.setNameX("")
c1.setNameY("Numbers")
c1.setName("Function example")
f1=F1D("2*x*cos(x)",0,100)
f2=F1D("0.2*x*x*sin(x)",0,100)
f1.setColor(Color.red)
c1.add(f1) 
c1.add(f2) 
c1.update()


# export to some image (png,eps,pdf,jpeg...)
# c1.export(Editor.DocMasterName()+".png")

