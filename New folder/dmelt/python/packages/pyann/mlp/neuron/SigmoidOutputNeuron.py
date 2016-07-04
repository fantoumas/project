from pyann.mlp.neuron import OutputNeuron
import math

class SigmoidOutputNeuron(OutputNeuron):

    def __init__(self, minValue = 0.0, maxValue = 1.0):
        """
            Build this neuron

            @author     Thiago F Pappacena
            @param      float   minValue    The minimum output for this neuron
            @param      float   maxValue    The maximum output for this neuron
        """
        super(SigmoidOutputNeuron, self).__init__()
        self.minValue = minValue
        self.maxValue = maxValue
        self.sigmoid_Y = self.maxValue - self.minValue
        self.sigmoid_N = -1.0 * self.minValue
    # end :: __init__


    def applyOutputFunction(self, value):
        """
            Apply a function to the input value.

            @author     Thiago F Pappacena
            @param      float   value   The input value for the neuron
            @return     float   The output
        """
        sigmoidValue = 1 / (1 + math.exp(-1.0 * value) )
        return self.sigmoid_Y * sigmoidValue - self.sigmoid_N
    # end :: applyOutputFunction


    def applyOutputDerivativeFunction(self, value):
        """
            Apply the derivative function to the input value

            @author     Thiago F Pappacena
            @param      float   value   The input value for the neuron
            @return     float   The output
        """
        fv = self.applyOutputFunction(value)
        #sigmoidDerivativeValue = fv * (1 - fv)
        return ((self.sigmoid_N + fv) * (self.sigmoid_Y - self.sigmoid_N - fv)) / self.sigmoid_Y
    # end :: applyOutputDerivativeFunction

    def getSkel(self):
        """

        """
        return self.__class__(minValue = self.minValue, maxValue = self.maxValue)
    # end :: getSkel

# end :: SigmoidOutputNeuron
