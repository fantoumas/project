from pyann.mlp import InputSizeMissmatch

class Layer(object):
    """
        Abstract class to define a Layer in
        MLP network

        @author     Thiago F pappacena
    """

    def __init__(self, units):
        """
            Build a Layer

            @author     Thiago F Pappacena
            @param      list     units   The list of units in this layer
        """
        self.units = units
        self.nextLayer = None
        self.previousLayer = None
    # end :: __init__


    def getSkel(self):
        """
            Returns the dimensions of this layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     
        """
        return self.__class__([i.getSkel() for i in self.units])
    # end :: getSkel


    def getUnits(self):
        """
            Returns the list of units in this Layer

            @author     Thiago F Pappacena
            @param      void        void
            @return     list        The list of units in this Layer
        """
        return self.units
    # end :: getUnits


    def setUnits(self, units):
        """
            Defines the units of this layer

            @author     Thiago F Pappacena
            @param      list    units   The units
            @return     void
        """
        self.units = units
    # end :: setUnits


    def getPreviousLayer(self):
        """
            Returns the previous layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  A Layer object
        """
        return self.previousLayer
    # end :: getPreviousLayer


    def setPreviousLayer(self, layer):
        """
            Defines the previous synapse layer

            @author     Thiago F Pappacena
            @param      object  layer   The new previous SynapseLayer
            @return     void
        """
        self.previousLayer = layer
    # end :: setPreviousLayer


    def disconnect(self):
        """
            Remove connections between layers

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        self.previousLayer = None
        self.nextLayer = None
    # end :: disconect


    def getNextLayer(self):
        """
            Returns the next synapse layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  A SynapseLayer object
        """
        return self.nextLayer
    # end :: getNextLayer


    def setNextLayer(self, layer):
        """
            Defines the next synapse layer

            @author     Thiago F Pappacena
            @param      object  layer   The new next SynapseLayer
            @return     void
        """
        self.nextLayer = layer
    # end :: setNextLayer


    def getOutput(self):
        """
            Gets the output from the layer given

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The output from this Layer
        """
        return tuple( (u.getOutput() for u in self.units) )
    # end :: getOutput


    def getBackwardOutput(self):
        """
            Gets the backward output from the layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The backward output from this layer
        """
        return tuple( (u.getBackwardOutput() for u in self.units) )
    # end :: getBackwardOutput


    def getBackwardInputSums(self):
        """
            Returns the sum of backward inputs for each neuron in this layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The backward input sums
        """
        return tuple( (u.getActualBackwardInputSum() for u in self.units) )
    # end :: getBackwardInputSums


    def getInputSums(self):
        """
            Returns the sum of inputs for each neuron in this layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The input sums
        """
        return tuple( (u.getActualInputSum() for u in self.units) )
    # end :: getInputSums


    def clear(self):
        """
            Clear activations of neurons in this layer

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        for n in self.units:
            n.clear()
    # end :: clear


    def __len__(self):
        """
            Gets the length of units in this layer

            @author     Thiago F Pappacena
            @param      void        void
            @return     integer     The number of items in this layer
        """
        return len(self.units)
    # end :: __len__


    def __getitem__(self, x):
        """
            Indexing Layer objects as common lists

            @author     Thiago F Pappacena
            @param      integer     x   The index
            @return     object      The neuron in that position
        """
        return self.units[x]
    # end :: __getitem__

# end :: Layer
