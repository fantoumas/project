from pyann.mlp import InputSizeMissmatch
from pyann.mlp.neuron import Neuron
import math

class SigmoidNeuron(Neuron):
    """
        A neuron unit

        @author     Thiago F Pappacena
    """

    def __init__(self, minValue = 0.0, maxValue = 1.0):
        """
            Build a neuron

            @author     Thiago F Pappacena
            @param      float   minValue    The minimum output for this neuron
            @param      float   maxValue    The maximum output for this neuron
        """
        super(SigmoidNeuron, self).__init__()

        # The above values are used to adapt the sigmoid function.
        # Using this values in activation and in derivative function,
        # this neuron can map any real value in interval [minValue, maxValue]
        self.minValue = minValue
        self.maxValue = maxValue
        self.sigmoid_Y = self.maxValue - self.minValue
        self.sigmoid_N = -1.0 * self.minValue
    # end :: __init__


    def applyOutputFunction(self, value):
        """
            Apply the sigmoid function to the input value.

            @author     Thiago F Pappacena
            @param      float   value   The input value for the neuron
            @return     float   The output
        """
        sigmoidValue = 1 / (1 + math.exp(-1.0 * value) )
        return self.sigmoid_Y * sigmoidValue - self.sigmoid_N
    # end :: applyOutputFunction


    def applyOutputDerivativeFunction(self, value):
        """
            (abstract) Apply the derivative function to the input value

            This function must be implemented in subclasses fo Neuron

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

# end :: SigmoidNeuron
