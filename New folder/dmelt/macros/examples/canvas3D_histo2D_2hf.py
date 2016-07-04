# 3D Plots | C | 1.7 | S.Chekanov | 3D histogram (H2D) and a 3D (F2D) function overlyed on HPlot3D
 
from jhplot  import HPlot3D,H2D,F2D
from java.util import Random 

c1 = HPlot3D("Canvas",600,400)
c1.setGTitle("F2D and H2D objects")
c1.setTextBottom("Global X")
c1.setTextLeft("Global Y")


c1.setNameX("X")
c1.setNameY("Y")

c1.setColorMode(4)
c1.visible(1)

h1 = H2D("My 2D Test 1",30,-3.0, 3.0, 30, -3.0, 3.0)
f1 = F2D("8*(x*x+y*y)", -3.0, 3.0, -3.0, 5.0)
rand = Random()
for i in range(1000):
               h1.fill(0.4*rand.nextGaussian(),rand.nextGaussian())
c1.draw(h1,f1)

# export to some image (png,eps,pdf,jpeg...)
# c1.export(Editor.DocMasterName()+".svg")
c1.export("image.pdf")
c1.export("image.eps")

