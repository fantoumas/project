class F1Layer(object):
    def __init__(self, m, a, b, d, threshold):
        """
            Build a F1Layer

            @author     Thiago F Pappacena
            @param      double      The 'a' ART2 parameter
            @param      double      The 'b' ART2 parameter
            @param      double      The 'd' ART2 parameter
            @param      double      The teta threshold
        """
        self.m = m
        self.a = a
        self.b = b
        self.d = d
        self.threshold = threshold
    # end :: __init__


    def clearActivations(self):
        raise NotImplementedException('')

    def getOutput(self, input, f2output):
        raise NotImplementedException('')

    def setP(self, input):
        raise NotImplementedException('')

    def doFastLearningUpdates(self, f2layer = None):
        raise NotImplementedException('')
# end :: F1Layer
