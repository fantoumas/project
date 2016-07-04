from pyann.mlp import Synapse

class SynapseLayer(object):
    """
        A synapse layer between two neuron layers

        This object holds the references to both layers
        and a matrix of synapses that owns the
        weigths between each neuron connection

        @author     Thiago F Pappacena
    """

    def __init__(self, inputLayer, outputLayer):
        """
            Build a synapse layer with it's matrix of weights

            @author     Thiago F Pappacena
            @param      object      inputLayer      The input layer
            @param      object      outputLayer     The destination layer
        """
        self.inputLayer = inputLayer
        self.outputLayer = outputLayer
        self.connectionsMatrix = []
        self.__connectLayers()
    # end :: __init__


    def getConnectionsMatrix(self):
        """
            Returns the matrix of Synapses in this Layer

            @author     Thiago F Pappacena
            @param      void    void
            @param      tuple   The list of lists of Synapse objects
        """
        return self.connectionsMatrix
    # end :: getConnectionsMatrix


    def setConnectionsWeights(self, newWeights):
        """
            Defines the connections weights

            @author     Thiago F Pappacena
            @param      tuple   newWeights      The matrix of new weights
            @return     void
        """
        matrix = self.connectionsMatrix
        assert len(matrix) == len(newWeights), 'Dimension missmatch in setConnectionsWeights! %s | %s' % (len(matrix), len(newWeights))

        for line, lineWeights in zip(matrix, newWeights):
            assert len(line) == len(lineWeights)-1, 'Dimension missmatch in setConnectionsWeights!'

            # set bias
            line[0].getOutputNeuron().setBias(lineWeights[0])
            lineWeights = lineWeights[1:]

            # set synapses weights
            for syn, synWeight in zip(line, lineWeights):
                syn.setWeight(synWeight)

    # end :: setConnectionsWeights


    def getConnectionsWeights(self):
        """
            Get the connections weights matrix

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The connection matrix
        """
        return tuple(tuple([x[0].getOutputNeuron().getBias()] + [y.getWeight() for y in x]) for x in self.connectionsMatrix)
    # end :: getConnectionsWeights


    def __connectUnits(self, unitIn, unitOut):
        """
            Build a Synapse connection between two neurons

            @author     Thiago F Pappacena
            @param      object  unitIn      The input neuron
            @param      object  unitOut     The output neuron
            @return     object  A Synapse object between both units
        """
        return Synapse(unitIn, unitOut)
    # end :: __connectUnits


    def __connectLayers(self):
        """
            Connect the units in each layer

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        self.connectionsMatrix = []
        self.inputLayer.setNextLayer(self)
        self.outputLayer.setPreviousLayer(self)

        # build the matrix of synapses
        for o in range(len(self.outputLayer)):
            self.connectionsMatrix.append([])
            outUnit = self.outputLayer[o]

            for i in range(len(self.inputLayer)):
                inUnit = self.inputLayer[i]
                synapse = self.__connectUnits(inUnit, outUnit)
                self.connectionsMatrix[o].append(synapse)
    # end :: __connectLayers


    def getInputLayer(self):
        """
            Returns the input layer for this SynapseLayer

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The Layer object connected to this SynapseLayer
        """
        return self.inputLayer
    # end :: getInputLayer


    def getOutputLayer(self):
        """
            Returns the output layer for this SynapseLayer

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The Layer object connected to this SynapseLayer
        """
        return self.outputLayer
    # end :: getOutputLayer


    def sendForward(self):
        """
            Get the output from self.inputLayer and feedforward the 
            self.outputLayer, making it active

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        #input = self.inputLayer.getOutput() # get the output from previous layer
        for o in range(len(self.outputLayer)):
            for i in range(len(self.inputLayer)):
                self.connectionsMatrix[o][i].activate() # activate every synapse

        for unit in self.outputLayer:
            unit.activate()
    # end :: sendForward


    def sendBackward(self):
        """
            Backpropagate values from output to input Layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        for o in range(len(self.outputLayer)):
            for i in range(len(self.inputLayer)):
                self.connectionsMatrix[o][i].backwardActivate()
        for unit in self.inputLayer:
            unit.backwardActivate()
        #print self.inputLayer.getBackwardOutput()
        #raw_input()
    # end :: sendBackward

    
    def clear(self):
        """
            Clear all activations for synapses in this layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        tuple( tuple(inp.clear() for inp in outp) for outp in self.connectionsMatrix )
    # end :: clear

# end :: SynapseLayer
