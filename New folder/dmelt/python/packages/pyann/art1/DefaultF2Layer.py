from F2Layer import F2Layer

class DefaultF2Layer(F2Layer):
    
    def __init__(self, l, clusters):
        """
            Build an F2 layer

            @author     Thiago F Pappacena
            @param      float       l           The L (node's weights update) parameter
            @param      list        clusters    The list of clusters in this layer
        """
        F2Layer.__init__(self, l, clusters)
        self.winner = None
    # end :: __init__


    def selectWinner(self, input):
        nodesInputs = {}
        self.clusters.reverse()
        [nodesInputs.update({node.getTotalInput(input): node}) for node in self.clusters if not node.isReseted()]
        self.clusters.reverse()

        if not len(nodesInputs.keys()): # there are not unreseted nodes
            return None

        biggerInput = max(nodesInputs.keys())
        #print "bigger input: %s" % biggerInput

        self.winner = nodesInputs[biggerInput]
        return self.winner
    # end :: selectWinner


    def updateWinner(self, input):
        if self.winner is not None:
            self.winner.updateWeights(input, self.l)
        #print "Botom up weights: %s" % [i.getBottomUpWeights() for i in self.clusters]
        #print "Top down weights: %s" % [i.getTopDownWeights() for i in self.clusters]
    # end :: updateWinner


    def resetWinner(self):
        self.winner.reset()
    # end :: resetWinner


    def clear(self):
        F2Layer.clear(self)
        self.winner = None
        [node.setReseted(False) for node in self.clusters]
    # end :: clear
