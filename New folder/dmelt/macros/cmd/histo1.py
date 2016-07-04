#  H1D histogram. Example  I
# S.Chekanov


from java.awt import Color
from java.util import Random
from jhplot  import HPlot,H1D,HLabel


c1 = HPlot("Canvas",600,400)  
c1.setGTitle("Global labels: F_{2} ,  x_{&gamma;}  #bar{p}p F_{2}^{c#bar{c}}"); #put title
c1.visible(1)
c1.setAutoRange()



h1 = H1D("Simple1",20, -2.0, 2.0)
rand = Random()
# fill histogram
for i in range(100):
      h1.fill(rand.nextGaussian())      


c1.draw(h1)
h1.setPenWidthErr(2)
c1.setNameX("Xaxis")
c1.setNameY("Yaxis")
c1.setName("Canvas title")
c1.drawStatBox(h1)


# set HLabel in the normilised coordinate system
lab=HLabel("HLabel in NDC", 0.15, 0.7, "NDC")
lab.setColor(Color.blue)
c1.add(lab)




c1.update()
