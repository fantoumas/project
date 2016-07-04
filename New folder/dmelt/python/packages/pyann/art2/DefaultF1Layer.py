import pyvetmath as vetmath
from F1Layer import F1Layer
from ART2 import ART2SizeMissmatchException

class DefaultF1Layer(F1Layer):

    def __init__(self, m, a, b, d, threshold, fastLearningCycles, debug = True):
        """

        """
        F1Layer.__init__(self, m, a, b, d, threshold)
        self.debug = debug
        self.fastLearningCycles = fastLearningCycles
        self.clearActivations()
    # end :: __init__


    def clearActivations(self):
        self.input = []
        self.p = []
        self.q = []
        self.u = []
        self.v = []
        self.w = []
        self.x = []
    # end :: clearActivations


    def getOutput(self, input, f2output):
        """

        """
        if len(input) != len(f2output):
            raise ART2SizeMissmatchException('Inputs to F1 Layer have not same dimensions')

        
        self.input = input
        self.initUnits()

        self.setU()
        self.setW()
        self.setQ()
        self.setX()
        self.setP()
        self.setV()

        self.setUAgain()
        self.setWAgain()
        self.setPAgain()
        self.setXAgain()
        self.setQAgain()
        self.setVAgain()

        return self.p
    # end :: getOutput

    def initUnits(self):
        emptyVector = vetmath.makeEmptyVector(self.m)
        self.p = emptyVector[:]
        self.q = emptyVector[:]
        self.u = emptyVector[:]
        self.v = emptyVector[:]
        self.w = emptyVector[:]
        self.x = emptyVector[:]
    # end :: initUnits

    
    def dump(self, title, vector):
        if self.debug:
            print "%s ~> %s" % (title, vector)

    def setW(self):
        self.w = self.input[:]
        self.dump('w', self.w)

    def setWAgain(self):
        self.w = tuple([self.input[i] + self.a * self.u[i] for i in xrange(0, len(self.input))])
        self.dump('w again', self.w)

    def setX(self):
        self.x = vetmath.normalize( self.input, e = 0.00000000001 )
        self.dump('x', self.x)

    def setXAgain(self):
        self.x = vetmath.normalize( self.w, e = 0.00000000001 )
        self.dump('x again', self.x)
        
    def setV(self):
        self.v = vetmath.applyThreshold( self.x, self.threshold )
        self.dump('v', self.v)

    def setVAgain(self):
        fX = vetmath.applyThreshold( self.x, self.threshold )
        fQ = vetmath.applyThreshold( self.q, self.threshold )
        self.v = tuple([x[0] + self.b * x[1] for x in zip(fX, fQ)])
        self.dump('v again', self.v)

    def setU(self):
        self.u = tuple( [0 for i in xrange(0, len(self.input))] )
        self.dump('u', self.u)

    def setUAgain(self):
        self.u = vetmath.normalize( self.v, e = 0.00000000001 )
        self.dump('u again', self.u)

    def setP(self):
        self.p = vetmath.makeEmptyVector(self.m)
        self.dump('p', self.p)

    def setPAgain(self):
        self.p = self.u[:]
        self.dump('p again', self.p)

    def setPWithWinnerNode(self, winnerNode):
        winnerTopDownW = winnerNode.getTopDownWeights()
        self.p = tuple([self.u[i] + self.d * winnerTopDownW[i] for i in xrange(0, len(winnerTopDownW))])
        self.dump('p again', self.p)

    def setQ(self):
        self.q = vetmath.makeEmptyVector(self.m)
        self.dump('q', self.q)

    def setQAgain(self):
        self.q = vetmath.normalize(self.p, e = 0.00000000001)
        self.dump('q again', self.q)

    def getU(self):
        return self.u

    def getP(self):
        return self.p

    def doFastLearningUpdates(self, f2):
        self.setWAgain()
        self.setXAgain()
        self.setQAgain()
        self.setVAgain()
        for i in xrange(0, self.fastLearningCycles):
            f2.doFastLearningUpdates( self )
            self.setUAgain()
            self.setWAgain()
            self.setPWithWinnerNode(f2.getWinner())
            self.setXAgain()
            self.setQAgain()
            self.setVAgain()

