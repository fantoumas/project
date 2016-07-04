import pyvetmath as vetmath
import math
from ART1 import ART1SizeMissmatch

class Cluster(object):
    def __init__(self, n, clusterID):
        """
            Build a cluster

            @author     Thiago F Pappacena
            @param      integer     n           The dimension of input vector
            @param      mixed       clusterID   The cluster identification
        """
        self.reseted = False
        self.ID = clusterID
        self.n = n
        self.topDownWeights = tuple( [1.0 for i in xrange(0, n)] )
        self.bottomUpWeights = tuple( [1.0/(1+n) for i in xrange(0,n)] )
    # end :: __init__

    
    def getTotalInput(self, input):
        if len(input) != self.n:
            raise ART1SizeMissmatch('Wrong input vector size (%s. Expecting %s)' % (len(input), self.n))

        return sum( [self.bottomUpWeights[i] * input[i] for i in xrange(0, self.n)] )
    # end :: getTotalInput


    def updateWeights(self, input, l):
        self.updateTopDownWeights(input)
        self.updateBottomUpWeights(input, l)
    # end :: updateWeights


    def updateTopDownWeights(self, input):
        self.topDownWeights = input
    # end :: updateTopDownWeights


    def updateBottomUpWeights(self, input, l):
        if len(input) != self.n:
            raise ART1SizeMissmatch('Wrong input vector size (%s. Expecting %s)' % (len(input), self.n))

        inputNorm = sum(input)
        #print "(%s * %s)/(%s - 1 + %s)" % (l, str(input), l, inputNorm)
        self.bottomUpWeights = tuple( [(l*input[i])/(l-1.0 + inputNorm) for i in xrange(0, self.n)] )
    # end :: updateBottomUpWeights


    def isReseted(self):
        return self.reseted
    # end :: isReseted


    def setReseted(self, reseted = True):
        self.reseted = reseted
    # end :: setReseted


    def reset(self):
        self.setReseted(True)
    # end :: reset


    def getTopDownWeights(self):
        return self.topDownWeights
    # end :: getTopDownWeigts


    def getBottomUpWeights(self):
        return self.bottomUpWeights
    # end :: getBottomUpWeights


    def getID(self):
        return self.ID
