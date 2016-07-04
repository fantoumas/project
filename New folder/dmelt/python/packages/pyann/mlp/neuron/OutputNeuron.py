from pyann.mlp.neuron import Neuron

class OutputNeuron(Neuron):


    def setBackwardActivation(self, value):
        """
            Defines the backward activation for this output neuron

            @author     Thiago F Pappacena
            @param      float   value   The backward activation
            @return     void
        """
        self.actualBackwardActivation = value
    # end :: setBackwardActivation


# end :: OutputNeuron
