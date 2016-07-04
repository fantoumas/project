from pyann.mlp import InputSizeMissmatch
import random

class Neuron(object):
    """
        A neuron unit

        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build a neuron

            @author     Thiago F Pappacena
            @param      object  inputSynapses   The input synapse object
            @param      object  outputSynapses  The output synapse object
        """
        self.inputSynapses = []
        self.outputSynapses = []
        self.actualInputSum = None
        self.actualActivation = None
        self.actualBackwardInputSum = None
        self.actualBackwardActivation = None
        self.lastWeightDelta = 0
        #self.bias = random.random()
        self.bias = -0.5 + (random.random() * 0.5*2)
    # end :: __init__


    def disconnect(self):
        """
            Disconnect connections of this neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        self.inputSynapses = []
        self.outputSynapses = []
    # end :: disconnect


    def setInputSynapses(self, inputSynapses):
        """
            Set the list of input synapses

            @author     Thiago F Pappacena
            @param      list    inputSynapses   The list of Synapse objects
            @return     void
        """
        self.inputSynapses = inputSynapses
    # end :: setInputSynapses


    def setOutputSynapses(self, outputSynapses):
        """
            Set the list of output synapses

            @author     Thiago F Pappacena
            @param      list    outputSynapses   The list of Synapse objects
            @return     void
        """
        self.outputSynapses = outputSynapses
    # end :: setOutputSynapses


    def addInputSynapse(self, inputSynapse):
        """
            Add an input synapse to the neuron

            @author     Thiago F Pappacena
            @param      object  inputSynapse    The input synapse for this neuron
            @return     void
        """
        self.inputSynapses.append(inputSynapse)
    # end :: addOutputSynapse


    def addOutputSynapse(self, outputSynapse):
        """
            Add an output synapse to this neuron

            @author     Thiago F Pappacena
            @param      object  outputSynapse an output synapse object
            @return     void
        """
        self.outputSynapses.append(outputSynapse)
    # end :: addOutputSynapse


    def getInputSynapses(self):
        """
            Returns the list of input synapses

            @author     Thiago F Pappacena
            @param      void    void
            @return     list    The list of input Synapse objects
        """
        return self.inputSynapses
    # end :: getInputSynapses


    def getOutputSynapses(self):
        """
            Returns the list of output synapses

            @author     Thiago F Pappacena
            @param      void    void
            @return     list    The list of input Synapse objects
        """
        return self.outputSynapses
    # end :: getInputSynapses


    def applyOutputFunction(self, value):
        """
            (abstract) Apply a function to the input value.

            This function must be implemented in subclasses of
            Neuron and the math function must implement what is
            needed to be used in a MLP network

            @author     Thiago F Pappacena
            @param      float   value   The input value for the neuron
            @return     float   The output
        """
        raise NotImplementedError('applyOutputFunction must be implemented in subclasses of Neuron [%s]' % self)
    # end :: applyOutputFunction


    def applyOutputDerivativeFunction(self, value):
        """
            (abstract) Apply the derivative function to the input value

            This function must be implemented in subclasses fo Neuron

            @author     Thiago F Pappacena
            @param      float   value   The input value for the neuron
            @return     float   The output
        """
        raise NotImplementedError('applyOutputDerivativeFunction must be implemented in subclasses of Neuron [%s]' % self)
    # end :: applyOutputDerivativeFunction


    def activate(self):
        """
            Activate a neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        totalInput = sum(i.getActivation() for i in self.inputSynapses) + (1 * self.bias)
        self.actualInputSum = totalInput
        self.actualActivation = self.applyOutputFunction(self.actualInputSum)
    # end :: activate


    def backwardActivate(self):
        """
            Activate a neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        #print '%s backward activations : %s' % (self, [i.getBackwardActivation() for i in self.outputSynapses])
        totalInput = sum(i.getBackwardActivation() for i in self.outputSynapses)
        self.actualBackwardInputSum = totalInput
        self.actualBackwardActivation = self.applyOutputDerivativeFunction(self.actualInputSum) * self.actualBackwardInputSum
        #self.actualBackwardActivation = self.actualBackwardInputSum
    # end :: backwardActivate


    def getOutput(self):
        """
            Gets the output of this neuron for a given input

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The total output for the input
        """
        #if self.actualActivation is None:
        #    self.activate()
        return self.actualActivation
    # end :: getOutput

    
    def getBackwardOutput(self):
        """
            Returns the actual backward output

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The actual backward output
        """
        #if self.actualBackwardActivation is None:
        #    self.backwardActivate()
        return self.actualBackwardActivation
    # end :: getBackwardOutput


    def getBias(self):
        """
            Returns the neuron's bias

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The actual neuron's bias
        """
        return self.bias
    # end :: getBias



    def setBias(self, bias):
        """
            Define the neuron bias

            @author       Thiago F Pappacena
            @param        float   bias    The neuron bias
            @return       void
        """
        self.bias = bias
    # end :: setBias

    
    def adjustWeights(self, deltaWeight):
        """
            Adjust the weights of every input synapse and the bias,
            given a deltaWeight

            @author     Thiago F Pappacena
            @param      float   deltaWeight     The delta to be used
            @return     void
        """
        #print 'ajusting %s with delta %s' % (self, deltaWeight)
        self.lastWeightDelta = deltaWeight
        for inp in self.inputSynapses:
            inp.adjustWeight(deltaWeight)
        self.bias += deltaWeight
    # end :: adjustWeights

    
    def getLastWeightDelta(self):
        """
            Returns the last weight ajust factor
            (usefull for momentum, for example)

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The last weightDelta applyed
        """
        return self.lastWeightDelta
    # end :: getLastWeightDelta


    def getActualInputSum(self):
        """
            Returns sum of all actual input to this neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The som of this inputs
        """
        #if self.actualInputSum is None:
        #    self.actualInputSum = sum((i.getActivation() for i in self.inputSynapses))
        return self.actualInputSum
    # end :: getActualInputSum


    def getActualBackwardInputSum(self):
        """
            Returns the sum of actual backward inputs

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The backward inputs sum
        """
        #if self.actualBackwardInputSum is None:
        #    self.actualBackwardActivation = sum((i.getBackwardActivation() for i in self.outputSynapses))
        return self.actualBackwardInputSum
    # end :: getActualBackwardInputSum


    def clear(self):
        """
            Clear the activations for this neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        self.actualInputSum = None
        self.actualActivation = None
        self.actualBackwardInputSum = None
        self.actualBackwardActivation = None
    # end :: clear


    def getSkel(self):
        """
            Returns a copy of this neuron structure

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  A skeleton :P
        """
        return self.__class__()
    # end :: getSkel


# end :: Neuron
