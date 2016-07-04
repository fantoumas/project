#  Statistics | C | 1.7 | S.Chekanov | Verious random distributions 

from java.awt import Color
from jhplot import *
from cern.jet.random.engine import *
from cern.jet.random import *


# build a singleton
c1=HPlot("Canvas",650,500,3,2)
c1.visible()
c1.setAutoRange()
c1.setGTitle("Random Distributions")

engine = MersenneTwister()
Events=5000

c1.cd(1,1)
r=Gamma(1,0.5,engine)
h1=H1D("Gamma",25,0,10)
h1.setFill(1)
h1.setFillColor(Color.red)
w=1.0/(Events*h1.getBinSize())
for i in range(Events):
   h1.fill(r.nextDouble(),w)
c1.draw(h1)

c1.cd(2,1)
c1.setAutoRange()
r=Binomial(10,0.5,engine)
h1=H1D("Binominal",20,0,10)
h1.setFill(1)
h1.setFillColor(Color.blue)
w=1.0/(Events*h1.getBinSize())
for i in range(Events):
   h1.fill(r.nextDouble(),w)
c1.draw(h1)

c1.cd(3,1)
c1.setAutoRange()
r=Poisson(5,engine)
h1=H1D("Poisson",20,0,10)
h1.setFill(1)
h1.setFillColor(Color.green)
w=1.0/(Events*h1.getBinSize())
for i in range(Events):
   h1.fill(r.nextDouble(),w)
c1.draw(h1)

c1.cd(1,2)
c1.setAutoRange()
r=StudentT(5,engine)
h1=H1D("Student",20,0,5)
h1.setFill(1)
h1.setFillColor(Color.green)
w=1.0/(Events*h1.getBinSize())
for i in range(Events):
   h1.fill(r.nextDouble(),w)
c1.draw(h1)

c1.cd(2,2)
c1.setAutoRange()
r=NegativeBinomial(10,0.5,engine)
h1=H1D("NBD",30,0,30)
h1.setFill(1)
h1.setFillColor(Color.red)
w=1.0/(Events*h1.getBinSize())
for i in range(Events):
   h1.fill(r.nextDouble(),w)
c1.draw(h1)

c1.cd(3,2)
c1.setAutoRange()
r=Logarithmic(0.5,engine)
h1=H1D("Logarithmic",20,0,10)
h1.setFill(1)
h1.setFillColor(Color.blue)
w=1.0/(Events*h1.getBinSize())
for i in range(Events):
   h1.fill(r.nextDouble(),w)
c1.draw(h1)





