#!/usr/bin/env python

from pyann.art1 import *

f1 = DefaultF1Layer()
f2 = DefaultF2Layer(2, [Cluster(4, id) for id in xrange(1,4)])
orientSys = OrientSystem(0.4)

net = ART1(f1, f2, orientSys)



patterns = [(1,1,0,0), (0,0,0,1), (1,0,0,0), (0,0,1,1)]

for i in xrange(0,3):
    i = patterns[i]
    print "\n\nPattern %s" % str(i)
    print "Cluster#%d" % (net.classify(i).getID())

orientSys.rho = 0.7
print "\n\nPattern %s" % str(patterns[3])
print "Cluster#%d" % (net.classify(patterns[3]).getID())
