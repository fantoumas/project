# Data clustering | C | 1.7 | S.Chekanov | Perform a cluster analysis using jMinHEP GUI

from java.util import Random 
from jminhep.cluster    import *
from jhplot import *

# create data for analysis 
data = DataHolder("Example")
# fill 3D data with Gaussian random numbers
rand = Random()
for i in range(100):
      a =[]
      a.append( 10*rand.nextGaussian() )
      a.append( 2*rand.nextGaussian()+1 )
      a.append( 10*rand.nextGaussian()+3 )
      data.add( DataPoint(a) )

# start jMinHEP GUI
c1=HCluster(data)
