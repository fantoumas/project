from pyann.mlp.neuron   import InputNeuron
from pyann.mlp.layer    import Layer

class InputLayer(Layer):
    """
        Class to define a Input layer

        @author     Thiago F pappacena
    """

    def __init__(self, units):
        """
            Build the Layer

            @author     Thiago F Pappacena
            @param      integer     units   The number of units in this layer
        """
        Layer.__init__(self, [InputNeuron() for i in range(units)])
    # end :: __init__


    def setInput(self, input):
        """
            Connect the input tuple to each neuron in this layer

            @author     Thiago F Pappacena
            @param      tuple   input   The input to this layer
            @return     void
        """
        for i in range(len(input)):
            self.units[i].setInput(input[i])
    # end :: setInput


    def getSkel(self):
        """

        """
        return self.__class__(len(self.units))
    # end :: getSkel


# end :: InputLayer
