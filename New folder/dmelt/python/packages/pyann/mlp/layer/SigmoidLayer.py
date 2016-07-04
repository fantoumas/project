from pyann.mlp          import InputSizeMissmatch
from pyann.mlp.neuron   import SigmoidNeuron
from pyann.mlp.layer    import Layer

class SigmoidLayer(Layer):
    """
        Abstract class to define a Layer in
        MLP network

        @author     Thiago F pappacena
    """

    def __init__(self, units, minValue = 0.0, maxValue = 1.0):
        """
            Build a Layer

            @author     Thiago F Pappacena
            @param      integer     units   The number of units in this layer
            @param      float   minValue    The minimum output for this neuron
            @param      float   maxValue    The maximum output for this neuron
        """
        Layer.__init__(self, [SigmoidNeuron(minValue = minValue, maxValue = maxValue) for i in range(units)])
        self.minValue = minValue
        self.maxValue = maxValue
    # end :: __init__

    def getSkel(self):
        """

        """
        return self.__class__(len(self.units), minValue = self.minValue, maxValue = self.maxValue)
    # end :: getSkel

# end :: SigmoidLayer
