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
p1=p1d('p1')
p1.add(8,10,2)
p1.add(20,20,4)
p1.add(30,16,3)
p1.add(40,10,2)
# show as a histogram in 100 bins
c1+p1

# show second as red histogram
p2=p1d('p2')
p2.add(8,20,5)
p2.add(20,23,7)
p2.add(30,19,4)
p2.add(40,17,1)
p2.setColor(Color.red)
c1+p2

# show it 
# p1.toTable()

# show it 
# p2.toTable()

p3=p1+p2
# p3.setTitle("OK")
# look at table: 
# p3.toTable()

c1+p3

c1.cd(1,2)
c1.auto()
# multiplications
p4=p1*2
p5=p1/p2

# plot 2 P1Ds
c1+p4+p5
print p1.getTitle()," has ",p1.size()

p6=p1.merge(p2)
p6.setTitle("merged")
print p6.getTitle()," has ",p6.size()

# scale and plot
c1+p6*2

# make a copy
p8=p2.copy()
p8.setTitle("copied")
# scale
p8=p8*2.0
p8.setColor(Color.blue)
c1+p8
