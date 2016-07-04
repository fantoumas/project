from pyann.mlp.neuron   import OutputNeuron
from pyann.mlp.layer    import Layer

class OutputLayer(Layer):
    """
        Class to define a Output layer

        @author     Thiago F pappacena
    """

    def __init__(self, units):
        """
            Build the Layer

            @author     Thiago F Pappacena
            @param      integer     units   The number of units in this layer
        """
        Layer.__init__(self, [OutputNeuron() for i in range(units)])
    # end :: __init__


    def setBackwardActivations(self, values):
        """
            Defines the backward activation for each neuron in this layer

            @author     Thiago F Pappacena
            @param      tuple   values  The list of backward activation float values
            @return     void
        """
        for i in range(len(self)):
            self[i].setBackwardActivation(values[i])
    # end :: setBackwardActivations


    def getSkel(self):
        """

        """
        return self.__class__(len(self.units))
    # end :: getSkel


# end :: OutputLayer
