from pyann.mlp.layer    import SynapseLayer, InputLayer, OutputLayer, SigmoidLayer, SigmoidInputLayer, SigmoidOutputLayer
from pyann.mlp          import WrongLayersOrganization
from copy import copy

class Network(object):
    """
        A MLP neural network itself :)

        @author     Thiago F Pappacena
    """

    def __init__(self, layers):
        """
            Build a network with the given layers

            @author     Thiago F Pappacena
            @param      tuple   layers  A tuple of Layer objects
        """
        if not isinstance(layers[0], InputLayer):
            raise WrongLayersOrganization('First layer is not a valid InputLayer')
        if not isinstance(layers[-1], OutputLayer):
            raise WrongLayersOrganization('Last layer is not a valid OutputLayer')

        # build network architeture
        self.inputLayer = layers[0]
        self.outputLayer = layers[-1]
        self.layers = layers
        self.hiddenLayers = layers[1:-1]
        self.synapseLayers = []
        for i in range(len(layers)):
            layer = layers[i]
            if isinstance(layer, OutputLayer):
                break
            nextLayer = layers[i+1]
            synLayer = SynapseLayer(layer, nextLayer)
            self.synapseLayers.append(synLayer)
    # end :: __init__


    @classmethod
    def fromWeightMatrix(self, matrix, layers = None):
        """
            Build a network based on the 3D-matrix of synapse layers' weights

            @author     Thiago F Pappacena
            @param      tuple   matrix      The 3D matrix of weights
            @param      tuple   layers      The tuple of layer classes to be used in network architecture
            @return     object  The Network object
        """
        assert not layers or len(matrix) -1 == len(layers), 'Layer types and connection matrix length missmatch'
        assert not layers or issubclass(layers[0], InputLayer), 'First item of "layers" parameter must be a InputLayer subclass'
        assert not layers or issubclass(layers[-1], OutputLayer), 'Last item of "layers" parameter must be a OutputLayer subclass'

        synLayerCount = len(matrix)
        assert synLayerCount >= 1, 'You can only build Networks with layers :P'

        hiddenLayersCount = synLayerCount - 1

        inputLayerSize = len(matrix[0][0]) - 1
        outputLayerSize = len(matrix[-1])

        if layers:  # if layer types are defined,
            inputLayer = layers[0]( inputLayerSize )
            outputLayer = layers[-1]( outputLayerSize )
        else:       # otherwise, use default Sigmoid type
            inputLayer = SigmoidInputLayer(inputLayerSize)
            outputLayer = SigmoidOutputLayer(outputLayerSize)

        netlayers = [inputLayer]

        for i in range(1, hiddenLayersCount + 1):
            layerSize = len(matrix[i][0]) - 1
            if layers and layers[i]:
                layer = layers[i](layerSize)
            else:
                layer = SigmoidLayer(layerSize)
            netlayers.append(layer)

        netlayers.append(outputLayer)

        net = Network(netlayers)
        net.setWeightMatrix(matrix)

        return net
    # end :: fromWeightMatrix


    def getOutput(self, input):
        """
            Get the response from network for a given input, keeping the synapse activations

            Use this method for implementing training algorithms, where you need
            to keep activations after fetching results from network. To clear that
            activations after, use cleanActivations() method. If you are not planning
            to use the activations and only want to get the response from network,
            use the classify() method

            @author     Thiago F Pappacena
            @param      tuple   input   The input tuple
            @return     tuple   The output from the network
        """
        self.inputLayer.setInput(input)
        for synlayer in self.synapseLayers:
            synlayer.sendForward()

        """
        print 'input: %s' % list(self.inputLayer.getOutput())
        print '---'
        for i in self.hiddenLayers:
            print 'hidden bias:'
            for n in i:
                print '%s -> %s' % (n, n.bias)
            for out in i.getPreviousLayer().connectionsMatrix:
                for inp in out:
                    print 'hidden syn (%s->%s) weight %s | activ %s' % (inp.inputNeuron, inp.outputNeuron, inp.weight, inp.actualActivation)
            for n in i:
                print 'neuron info %s: input = %s, activation = %s, output = %s' % (n, n.getActualInputSum(), n.actualActivation, n.getOutput())
        print '---'
        print 'output bias'
        for n in self.outputLayer:
            print '%s -> %s' % (n, n.bias)
        for out in self.outputLayer.getPreviousLayer().connectionsMatrix:
            for inp in out:
                print 'output syn %s weight %s' % (inp, inp.weight)
        for n in self.outputLayer:
            print 'neuron info %s: input = %s, activation = %s, output = %s' % (n, n.getActualInputSum(), n.actualActivation, n.getOutput())
        print 'output: %s' % list(self.outputLayer.getOutput())
        raw_input()
        """
        
        return self.outputLayer.getOutput()
    # end :: getOutput

    
    def classify(self, input):
        """
            Classify the input pattern, clearing all activations after

            @author     Thiago F Pappacena
            @param      tuple   input   The input pattern
            @return     tuple   The output response from the net
        """
        self.clearActivations()
        out = self.getOutput(input)
        self.clearActivations()
        return out
    # end :: classify


    def getSynapseLayers(self):
        """
            Returns the synapse layers in this network

            @author     Thiago F Pappacena
            @param      void    void
            @return     list    The list of SynapseLayer
        """
        return self.synapseLayers
    # end :: getSynapseLayers


    def getLayers(self):
        """
            Returns the list of layers in this network

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The list of layers
        """
        return self.layers
    # end :: getLayers


    def getInputLayer(self):
        """
            Returns the input layer for this Network

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The input Layer object
        """
        return self.inputLayer
    # end :: getInputLayer


    def getOutputLayer(self):
        """
            Returns the output layer for this Network

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The output Layer object
        """
        return self.outputLayer
    # end :: getOutputLayer


    def getHiddenLayers(self):
        """
            Returns the hidden layers for this Network

            @author     Thiago F Pappacena
            @param      void    void
            @return     list    The list of hidden Layers object
        """
        return self.hiddenLayers
    # end :: getHiddenLayers


    def getWeightMatrix(self):
        """
            Returns the weights of synapses as a tuple of tuples

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The weights
        """
        ret = []
        for lay in self.synapseLayers:
            ret.append(lay.getConnectionsWeights())
        return tuple(ret)
    # end :: getWeightMatrix


    def setWeightMatrix(self, matrix3d):
        """
            Sets the weight of each synapse

            @author     Thiago F Pappacena
            @param      tuple   matrix  The tuple of tuples matrix of weights
            @return     void
        """
        assert len(self.synapseLayers) == len(matrix3d), 'Number of dimentions of given matrix do not match the number of synapse layers'

        for lay, layWeights in zip(self.synapseLayers, matrix3d):
            lay.setConnectionsWeights(layWeights)
    # end :: setWeightMatrix


    def getDimension(self):
        """
            Returns a tuple of layers with it's neuron's copy, representing
            the dimensions of this network
            
            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The tuple of layer's copy
        """
        #layers = tuple(copy(lay) for lay in self.layers)
        #for lay in layers:
        #    lay.disconnect()
        #    units = [copy(unit) for unit in lay.getUnits()]
        #    for u in units:
        #        u.disconnect()
        #    lay.setUnits(units)
        #return layers
        #return [lay.getSkel() for lay in self.layers]
        return self.layers
    # end :: getDimension


    def planify(self):
        """
            Returns the matrix weights as a single-dimension tuple of values

            This might be usefull to use as genes of a chromossome in
            genetic algoritms or to store in a database, for example.

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   All weights in this net
        """
        matrix = self.getWeightMatrix()
        ret = []
        for layerWeights in matrix:
            for outNeuron in layerWeights:
                ret += outNeuron
        return ret
    # end :: planify


    def setPlanifiedWeightMatrix(self, planifiedWeights):
        """
            Set the weights of this net based on the unidimensionified weights

            @author     Thiago F Pappacena
            @param      tuple   planifiedWeights    The list of weights
            @return     void
        """
        assert len(planifiedWeights) == len(self.planify()), 'Given planified weights do not match the length of net planified weights'

        unplanify = lambda line, lines, columns: tuple(line[ i*columns : i*columns + columns ] for i in xrange(lines))
        
        start = 0
        for synLay in self.getSynapseLayers():
            inpLen = len(synLay.getOutputLayer())
            outLen = len(synLay.getInputLayer())
            end = start + (inpLen * (outLen + 1))

            matrix = unplanify(planifiedWeights[start:end], inpLen, outLen+1)
            synLay.setConnectionsWeights(matrix)
            start = end
    # end :: setPlanifiedWeights


    @classmethod
    def fromDimension(cls, dimensions):
        """
            Build a new network based on the given dimensions

            @author     Thiago F Pappacena
            @param      tuple   dimensions  The same return of getDimension() method
            @return     object  The new network
        """
        return cls(tuple(lay.getSkel() for lay in dimensions))
    # end :: fromDimension

    
    def copyStructure(self):
        """
            Builds a new network with the same structure as this one

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  A new Network object
        """
        return self.fromDimension( self.getDimension() )
    # end :: copyStructure


    @classmethod
    def fromPlanifiedWeights(cls, dimensions, planifiedWeights):
        """
            Build a Network based on it's dimensions tuple.

            @author     Thiago F Pappacena
            @param      tuple   dimensions          The same return of getDimension() method
            @param      list    planifiedWeights    The list of weights, as returned by planify() method
            @return     object  The network
        """
        net = cls.fromDimension(dimensions)
        net.setPlanifiedWeightMatrix(planifiedWeights)

        return net
    # end :: fromPlanifiedWeights

    
    def clearActivations(self):
        """
            Clear all activations in this net

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        for syn in self.synapseLayers:
            syn.clear()
        for lay in self.layers:
            lay.clear()
    # end :: clearActivations


# end :: Network
