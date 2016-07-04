# test hplot instance
import shplot
from java.awt import Color
from java.util import Random
from shplot import *

print shplot.__doc__

# build a canvas
c1=hplot("scripting",1,2)
c1.visible()
c1.auto()

# define histograms
h1=h1d("h1",100,-3,3)
h2=h1d("h2",100,-3,3)
h3=h1d("h3",100,-3,3)

print type(h3)
javaObject=h3
objectClass      = javaObject.class
objectClassName  = javaObject.__class__.__name__
objectSuperClass = javaObject.class.superclass

print objectSuperClass.__name__
print javaObject.class.superclass
print javaObject.class

interfaces       = javaObject.class.interfaces
superClasses     = javaObject.__class__.__bases__
attributes       = javaObject.class.__dict__.items()
methods          = javaObject.class.getMethods()



rand = Random()
# fill histogram
for i in range(1000):
      h1.fill(rand.nextGaussian())
      h2.fill(0.6*rand.nextGaussian()+2)
      if i<400:
            h3.fill(0.5*rand.nextGaussian()+1.0)    
 

h12=h1+h2

# h1.setFill(1)
h1.setColor(Color.red)
# h1.setFillColor(Color.red)
h12.setFill(0)
h12.setColor(Color.blue)

c1.draw(h1)
c1.draw(h2)
c1.draw(h12+h3)

# scale
scaled=h1*2.5
scaled.setColor(Color.gray)
c1.draw(scaled)

# new plot
c1.cd(1,2)
c1.auto()
h13=h1+h3
h13.setColor(Color.blue)
h113=h1-h3
h113.setColor(Color.yellow)
c1.draw(h113)
c1.draw(h1)
c1.draw(h13)
# c1.draw(h113)
