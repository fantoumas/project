from F1Layer import F1Layer

class DefaultF1Layer(F1Layer):

    def __init__(self):
        self.x = None
    # end :: __init__


    def getOutput(self, input, F2NodeTopDownWeights = None):
        if F2NodeTopDownWeights is None:    # first iteraction. No F2 node selected
            self.x = input
        else:
            self.x = tuple([input[i] * F2NodeTopDownWeights[i] for i in xrange(0, len(input))])
        return self.x
    # end :: getOutput


    def clear(self):
        self.x = None
    # end :: clear

# end :: F1Layer
