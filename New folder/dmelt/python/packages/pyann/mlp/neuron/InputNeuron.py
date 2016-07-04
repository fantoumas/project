from pyann.mlp.neuron   import Neuron
from pyann.mlp          import LayerUseException

class InputNeuron(Neuron):

    def __init__(self):
        """
            Build this InputNeuron

            @author     Thiago F Pappacena
            @param      void    void
        """
        super(InputNeuron, self).__init__()
        self.input = ()
        self.bias = 0
    # end :: __init__


    def activate(self):
        """
            Blocking the use of activate method for InputNeuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        raise LayerUseException('You cannot activate a InputNeuron. Use setInput method instead')
    # end :: activate


    def getOutput(self):
        """
            Get the output from this neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The neuron output
        """
        return self.input
    # end :: getOutput


    def setInput(self, input):
        """
            Defines the input value for this neuron

            @author     Thiago F Pappacena
            @param      float   input   The input value
            @return     void
        """
        self.actualInputSum = input
        self.input = input
    # end :: setInput

# end :: InputNeuron
