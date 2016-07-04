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

p0=pnd("Example of PND")
p0.add([1,3,5])
p0.add([6,1,7])
p0.add([6,2,6,19])
p0.add([4,19,5,20,200])
p0.add([2,5,1,20,201])
p0.add([5,2,20,20,220])
p0.add([6,2,8,20,221])

p1=pnd("Example of PND")
p1.add([1,3,5])
p1.add([6,1,7])
p1.add([6,2,6,19])
p1.add([4,19,5,20,200])
p1.add([2,5,1,20,201])
p1.add([5,2,20,20,220])
p1.add([6,2,8,20,221])


p2=p1+p0

print p0.toString()

# get second column
p00=p0.getColumn(2)


# print column
print p00.toString()
# make histogram from 2nd row
c1.draw(p00.getH1D(100))


