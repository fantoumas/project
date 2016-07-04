#!/usr/bin/env python

import pyann.som as som
import random

clusters = [    som.Cluster( (0.2, 0.6, 0.5, 0.9), 1),
                som.Cluster( (0.8, 0.4, 0.7, 0.3), 2) ]

map         = som.Map(clusters)
neigh       = som.RectangularNeighborhood(map, 0)
learnRate   = som.LinearDescendingLearnRate(0.6, 0.5, 1)

net = som.SOM(map, neigh, learnRate)

patterns = [ (1,1,0,0), (0,0,0,1), (1,0,0,0), (0,0,1,1) ]

for iteration in xrange(1, 101):
    for pt in patterns:
        winner = net.classify(pt)
        net.doAjust(pt, iteration)
        if iteration == 1:
            print "\n\n\n Pattern: %s" % (str(pt))
            print "winner: %s" % winner.getID()
    if iteration in [1,2,10,50,100]:
        print "\n\nIteration %d wights" % iteration
        print clusters[0].getWeights()
        print clusters[1].getWeights()
