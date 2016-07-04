from F2Layer import F2Layer
from Cluster import Cluster
import pyvetmath as vetmath

class DefaultF2Layer(F2Layer):
    
    def __init__(self, m, d, learnRate, clusters, debug = True):
        F2Layer.__init__(self, m, d, learnRate)
        self.clusters = clusters
        self.winner = None
        self.debug = debug
    # end :: __init__

    def dump(self, title, vector):
        if self.debug:
            print "%s ~> %s" % (title, vector)


    def selectWinner(self, input):

        tmp = {}
        self.clusters.reverse()
        [tmp.update({node.getTotalInput(input): node}) for node in self.clusters if not node.isReseted()]  # get all nodes' output and use them as indexes
        self.clusters.reverse()

        if not len(tmp.keys()):     # there are not unreseted nodes
            return None

        self.dump('\nF2 inputs\n', tmp)
        # get the bigger index:
        biggerInput = max(tmp.keys())
        #print biggerInput

        winnerNode = tmp[ biggerInput ]
        self.winner = winnerNode

        return self.winner
    # end :: selectWinner

            

    def doFastLearningUpdates(self, f1):
        self.winner.ajustWeights(f1.getU())
    # end :: doFastLearningUpdates


    def resetWinner(self):
        self.winner.setReseted()
    # end :: resetWinner


    def unresetAllNodes(self):
        self.winner = None
        [x.setReseted(False) for x in self.clusters]
    # end :: unresetAllNodes


    def createNode(self, inputVector):
        c = Cluster(self.m, self.d, self.learnRate, max([i.getID() for i in self.clusters]) + 1, self.clusters[0].debug)
        self.clusters.append(c)
        c.setTopDownWeights(inputVector)
        return c
    # end :: createNode


    def getOutput(self):
        if self.winner is not None and not self.winner.isReseted():
            return winner.getTotalOutput()

        return vetmath.makeEmptyVector(self.m)
    # end :: getOutput


    def getWinner(self):
        return self.winner
    # end :: getWinner


    def setWinner(self, winner):
        self.winner = winner


    def getNextNotResetedNode(self):
        for i in self.clusters:
            if not i.isReseted():
                return i
        return None
    # end :: getNextNotResetedNode
    

    def hasNotResetedNode(self):
        return self.getNextNotResetedNode() is not None
    # end :: hasNotResetedNode


    def getNode(self, position):
        return self.cluster[position]
    # end :: getNode
