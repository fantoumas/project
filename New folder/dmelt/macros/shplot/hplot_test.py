# test hplot instance
from java.awt import Color
from java.util import Random
from shplot import *

# build a canvas
c1=hplot("scripting",1,2)
c1.visible()
c1.auto()

# define histograms
h1=h1d("histogram1",200,-4,4)
h2=h1d("histogram2",200,-4,4)
h1.setFill(1)
h1.setColor(Color.red)

rand = Random()
# fill histogram
for i in range(500):
      h1.fill(rand.nextGaussian())
      h2.fill(0.2*rand.nextGaussian())


c1.draw(h1)
h3=h1+h2
h3.setColor(Color.green)
# plot 2 histograms
c1+h3+h2


c1.cd(1,2)
c1.auto()
h13=h3*h2

# add to the plot 2 histograms:
c1+h13+h1*100
