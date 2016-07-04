# test p0d instance

from java.awt import Color
from shplot import *
import shplot

print shplot.__doc__
print dir()

# build a canvas
c1=hplot("scripting",1,2)
c1.visible()
c1.auto()

# define histograms
p1=p0d('p1',0)
p1.randomNormal(100, 1.0, 1.0)

# show as a histogram in 100 bins
c1+p1.getH1D(20)

# show second as red histogram
p2=p0d('p2',0)
p2.randomNormal(100, 4.0, 1.0)
h2=p2.getH1D(20)
h2.setColor(Color.red)
c1+h2

# show it 
# p1.toTable()

# show it 
# p2.toTable()

p3=p1+p2

# look at table: 
# p3.toTable()

h3=p3.getH1D(20)
h3.setColor(Color.blue)
c1+h3

c1.cd(1,2)
c1.auto()
# multiplications
p4=p1*2
p5=p1*p2
c1+p4.getH1D(20)+p5.getH1D(20)

print p1.getTitle()," has ",p1.size()

p6=p1.merge(p2)
print p6.getTitle()," has ",p6.size()
# scale and plot
p7=p6*3
c1+p7.getH1D(20)


# make a copy
p8=p2.copy()

# scale
p8=p8*2.0
h8=p8.getH1D(50)
h8.setColor(Color.blue)
c1+h8
