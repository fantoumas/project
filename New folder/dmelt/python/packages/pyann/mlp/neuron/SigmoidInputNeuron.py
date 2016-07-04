from pyann.mlp.neuron import InputNeuron
import math

class SigmoidInputNeuron(InputNeuron):

    def __init__(self, minValue = 0.0, maxValue = 1.0):
        """
            Build this neuron

            @author     Thiago F Pappacena
            @param      float   minValue    The minimum output for this neuron
            @param      float   maxValue    The maximum output for this neuron
        """
        super(SigmoidInputNeuron, self).__init__()
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
        return 1 / (1 + math.e ** (-1.0 * value) )
        #return math.tanh(value)
    # end :: applyOutputFunction


    def applyOutputDerivativeFunction(self, value):
        """
            (abstract) Apply the derivative function to the input value

            This function must be implemented in subclasses fo Neuron

            @author     Thiago F Pappacena
            @param      float   value   The input value for the neuron
            @return     float   The output
        """
        return value * (1 - value)
        #return 1 - (math.tanh(value)**2)
    # end :: applyOutputDerivativeFunction


    def getSkel(self):
        """

        """
        return self.__class__(minValue = self.minValue, maxValue = self.maxValue)
    # end :: getSkel

# end :: SigmoidInputNeuron
