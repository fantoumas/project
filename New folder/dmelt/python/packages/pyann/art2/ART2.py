import F1Layer
import F2Layer
import OrientationalSubsys

class ART2(object):

    """
    def __init__(   self, 
                    m = None, 
                    numberOfF2Nodes = None, 
                    d = None,
                    threshold = None,
                    a = None,
                    b = None,
                    rho = None,
                    c = None,
                    learnRate = None,
                    fastLearningCycles = None):
        self.d = d
        self.m = m
        self.threshold = threshold
        self.rho = rho
        self.c = c
        self.learnRate = learnRate
        self.fastLearningCycles = fastLearningCycles

        self.f1 = F1Layer( a = a, b = b, d = d, threshold = threshold, m = m)
        self.f2 = F2Layer( numberOfF2Nodes, d = d, learnRate = learnRate, fastLearningCycles = fastLearningCycles )
        self.orientSys = OrientationalSubsystem( c = c, rho = rho, m = m, d = d)
    # end :: __init__
    """

    def __init__(self, f1, f2, orientSys):
        self.f1 = f1
        self.f2 = f2
        self.orientSys = orientSys


    def setF1Layer(self, f1):
        self.f1 = f1

    def setF2Layer(self, f2):
        self.f2 = f2

    def setOrientSys(self, orientSys):
        self.orientSys = orientSys

    def getF1Layer(self):
        return self.f1

    def getF2Layer(self):
        return self.f2

    def getOrientSys(self):
        return self.orientSys


    def classify(self, input):
        """

        """

        self.f2.unresetAllNodes()
        self.f1.clearActivations()

        hasNotResetedNode = True

        # election
        while True:
            f1Output = self.f1.getOutput( input, self.f2.getOutput() )  # activate F1Layer
            winner = self.f2.selectWinner( f1Output )                   # choose a winner
            winnerTopDownW = winner.getTopDownWeights()                 # get that winner top-down weights

            self.f1.setPWithWinnerNode( winner )                              # set P unit

            # check for reset
            if not self.orientSys.triggerReset( self.f1.getU(), self.f1.getP() ):  # if not reseted
                break                                                               # stop... F2Layer node found
            else:                                                                   # reset triggered
                winner.reset()                                                      # reset this unit

            hasNotResetedNode = self.f2.hasNotResetedNode()
            if not hasNotResetedNode:     # all nodes were reseted
                break                     # stop the loop

        if not hasNotResetedNode:
            self.f2.setWinner( self.f2.createNode(input) )  # create a new one

        self.f1.doFastLearningUpdates(self.f2)
        #self.f2.doFastLearningUpdates(self.f1)

        # fast-learn to implement in winner.learn:
        #self.f1.setWAgain()
        #self.f1.setXAgain()
        #self.f1.setQAgain()
        #self.f1.setVAgain()
        #for i in xrange(0, self.fastLearningCycles):
        #    winner.ajustWeights( self.f1.getU() )
        #    self.f1.setUAgain()
        #    self.f1.setWAgain()
        #    self.f1.setP(winnerTopDownW)
        #    self.f1.setXAgain()
        #    self.f1.setQAgain()
        #    self.f1.setVAgain()

        return winner
    # end :: classify



class ART2Exception(Exception):
    pass

class ART2SizeMissmatchException(ART2Exception):
    pass

class ART2InvalidIntialization(ART2Exception):
    pass
