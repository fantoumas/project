class F2Layer(object):
    
    def __init__(self, m, d, learnRate):
        self.m = m
        self.d = d
        self.learnRate = learnRate

    def selectWinner(self, input):
        raise NotImplementedException('')

    def doFastLearningUpdates(self, f1):
        raise NotImplementedException('')

    def resetWinner(self):
        raise NotImplementedException('')

    def unresetAllNodes(self):
        raise NotImplementedException('')

    def createNode(self, node):
        raise NotImplementedException('')

    def getOutput(self):
        raise NotImplementedException('')

    def getWinner(self):
        raise NotImplementedException('')

    def hasNotResetedNode(self):
        raise NotImplementedException('')

    def getNextNotResetedNode(self):
        raise NotImplementedException('')

    def getNode(self, position):
        raise NotImplementedException('')
