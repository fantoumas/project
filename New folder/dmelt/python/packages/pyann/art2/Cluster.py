import pyvetmath as vetmath
import math

class Cluster(object):
    
    def __init__(self, m, d, learnRate, id, debug = True):
        self.m = m
        self.d = d
        self.id = id
        self.reseted = False
        self.learnRate = learnRate
        self.debug = debug

        self.topDownWeights  = vetmath.makeEmptyVector(self.m)
        self.bottomUpWeights = [1/( (1 - self.d) * math.sqrt(self.m) ) for i in xrange(0, self.m)]
    # end :: __init__

    def dump(self, title, vector):
        if self.debug:
            print "%s ~> %s" % (title, vector)


    def getTotalOutput(self):
        if self.isReseted():
            return vetmath.makeEmptyVector(self.m)
        return tuple( [self.d * x for x in self.topDownWeights] )
    # end :: getTotalOutput
    

    def getTotalInput(self, input):
        if len(input) != self.m:
            raise ART2SizeMissmatch('%s %s' % (len(input), self.m))

        return sum( [input[i] * self.bottomUpWeights[i] for i in xrange(0, self.m)] )
    # end :: getTotalInput
    

    def ajustTopDown(self, u):
        if not self.isReseted():
            self.topDownWeights = tuple([self.learnRate * self.d * u[i] + (1 + self.learnRate * self.d * (self.d-1)) * self.topDownWeights[i] for i in xrange(0, self.m)])
            self.dump('ajusted TopDown', self.topDownWeights)
    # end :: ajustTopDown


    def ajustBottomUp(self, u):
        if not self.isReseted():
            self.bottomUpWeights = tuple([self.learnRate * self.d * u[i] + (1 + self.learnRate * self.d * (self.d - 1)) * self.bottomUpWeights[i] for i in xrange(0, self.m)])
            self.dump('ajusted BottomUp', self.bottomUpWeights)
    # end :: ajustBottomUp


    def ajustWeights(self, u):
        self.ajustTopDown(u)
        self.ajustBottomUp(u)
    # end :: ajustWeights


    def isReseted(self):
        return self.reseted

    def reset(self):
        self.setReseted(True)

    def setReseted(self, reseted = True):
        self.reseted = reseted

    def getID(self):
        return self.id

    def getBottomUpWeights(self):
        return self.bottomUpWeights

    def getTopDownWeights(self):
        return self.topDownWeights

    def setTopDownWeights(self, weights):
        self.topDownWeights = weights

    def setBottomUpWeights(self, weights):
        self.bottomUpWeights = bottomUpWeights
