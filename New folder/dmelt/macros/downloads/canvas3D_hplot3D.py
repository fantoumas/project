# Plots/3D | C | 1.7 | S.Chekanov | HPlot3D canvas for functions and histograms in 3D 

from java.awt import Color,Font
from java.util import Random
from jhplot import F2D,H2D,HPlot3D

c1  = HPlot3D("Canvas",600,900, 2,3)
c1.visible(1)
c1.setGTitle("HPlot3D canvas tests")
rand =Random()

h1=H2D("My 2D Test1",30,-4.5, 4.5, 30, -4.0, 4.0)
h2=H2D("My 2D Test2",30,-4.5, 4.5, 30, -4.0, 4.0)
h3=H2D("My 2D Test3",10,-4.5, 4.5, 10, -4.0, 4.0)
f1=F2D("cos(x*y)*(x*x-y*y)", -2.0, 2.0, -2.0, 2.0)
f2=F2D("5*exp(-(x*x+y*y))", -2.0, 5.0, -2.0, 5.0)
f3=F2D("sin(4*x*y)", -2.0, 2.0, -2.0, 2.0)
f4=F2D("x^3-3*x-3*y^2", -2.0, 2.0, -2.0, 2.0)


for i in range(1000): 
       h1.fill(rand.nextGaussian(),0.5*rand.nextGaussian())
       h2.fill(1.0+0.5*rand.nextGaussian(),-2.0+0.5*rand.nextGaussian())

c1.cd(1,1)
c1.draw(h1,h2)
c1.setScaling(8)
c1.setRotationAngle(10)
c1.update()

c1.cd(2,1)
c1.setAutoRange()
c1.draw(f1)

c1.cd(1,2)
c1.setScaling(8)
c1.setRotationAngle(40)
c1.setAutoRange()
c1.draw(h1)


c1.cd(2,2)
c1.setAutoRange()
c1.setAxesFontColor(Color.blue)
c1.setColorMode(4)
c1.setScaling(8)
c1.setElevationAngle(30)
c1.setRotationAngle(35)
c1.draw(f3)

c1.cd(1,3)
c1.setAutoRange()
c1.setLabelFontColor(Color.red)
c1.setScaling(8)
c1.setRotationAngle(40)
c1.draw(f3,f2)

c1.cd(2,3)
c1.setAutoRange()
c1.setColorMode(1)
c1.setScaling(8)
c1.setElevationAngle(30)
c1.setRotationAngle(35)
c1.draw(f4)


# c1.clearAll()
# c1.update()
# export to some image (png,eps,pdf,jpeg...)
# c1.export(Editor.DocMasterName()+".png")
