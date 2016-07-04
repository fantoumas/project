import pyvetmath
from pyann.mlp import InputSizeMissmatch
import random


class Synapse(object):
    """
        A simple synapse object to connect 2 neurons

        @author     Thiago F Pappacena
    """

    def __init__(self, inputNeuron, outputNeuron):
        """
            Build the synapse connection

            @author     Thiago F Pappacena
            @param      object      inputNeuron      The input Neuron object
            @param      object      outputNeuron     The output Neuron object
        """
        self.inputNeuron = inputNeuron
        self.outputNeuron = outputNeuron
        #self.weight = random.random() 
        self.weight = -0.5 + (random.random() * 0.5*2)
        self.lastWeightDelta = 0
        self.actualActivation = None
        self.actualBackwardActivation = None
        self.__connect()
    # end :: __init__


    def __connect(self):
        """
            Connect two neurons

            @author     Thiago F Pappacena
            @param      object  inputNeuron     Another neuron
            @param      object  outputNeuron    A neuron
        """
        #self.outputNeuron = outputNeuron
        #self.inputNeuron = inputNeuron
        self.outputNeuron.addInputSynapse(self)
        self.inputNeuron.addOutputSynapse(self)
    # end :: connect


    def getWeight(self):
        """
            Returns the actual weight for this Synapse

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The connection weight
        """
        return self.weight
    # end :: getWeight


    def setWeight(self, weight):
        """
            Defines the feedforward weight of this synapse

            @author     Thiago F Pappacena
            @param      float   weight      The new connection weight
            @return     void
        """
        self.weight = weight
    # end :: setWeight


    def getInputNeuron(self):
        """
            Returns the input neuron of this synapse

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The input Neuron object
        """
        return self.inputNeuron
    # end :: getInputNeuron


    def getOutputNeuron(self):
        """
            Returns the output neuron of this synapse

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The output Neuron object
        """
        return self.outputNeuron
    # end :: getOutputNeuron


    def adjustWeight(self, deltaWeight):
        """
            Ajust the synapse weight given a delta weight

            @author     Thiago F Pappacena
            @param      float   deltaWeight     The delta to apply
            @return     void
        """
        self.lastWeightDelta = deltaWeight
        #before = self.weight
        self.weight = self.weight + (deltaWeight * self.inputNeuron.getOutput())
        #print 'adjusting %s with delta %s: %s => %s' % (self, deltaWeight, before, self.weight)
    # end :: ajustWeight


    def activate(self, input = None):
        """
            Activate this synapse with a given input

            @author     Thiago F Pappacena
            @param      float   input   The input for this synapse [optional. If not given, get from inputNeuron]
            @return     void
        """
        if input is not None:
            self.actualActivation = input * self.weight
        else:
            #print 'synapse %s => %s: %s * %s = %s' % (self.inputNeuron, self.outputNeuron, self.inputNeuron.getOutput(), self.weight, self.inputNeuron.getOutput() * self.weight)
            self.actualActivation = self.inputNeuron.getOutput() * self.weight
    # end :: self.actualActivation


    def backwardActivate(self, input = None):
        """
            Active the backward synapse

            @author     Thiago F Pappacena
            @param      float   input   The backward input for this synapse [optional. If not given, get from outputNeuron]
            @return     void
        """
        if input is not None:
            self.actualBackwardActivation = input * self.weight
        else:
            #print 'synapse %s => %s: %s * %s = %s' % (self.inputNeuron, self.outputNeuron, self.outputNeuron.getBackwardOutput(), self.weight, self.outputNeuron.getBackwardOutput() * self.weight)
            self.actualBackwardActivation = self.outputNeuron.getBackwardOutput() * self.weight
    # end :: backwardActivate


    def getActivation(self):
        """
            Returns the synapse activation

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   Synapse activation
        """
        return self.actualActivation
    # end :: getActivation

    
    def getBackwardActivation(self):
        """
            Gets the actual backward activation for the neuron

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The actual backward activation
        """
        return self.actualBackwardActivation
    # end :: getBackwardActivation


    def getLastWeightDelta(self):
        """
            Returns the last weight update in this synapse

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The last weight update in this synapse
        """
        return self.lastWeightDelta
    # end :: getLastWeightDelta


    def clear(self):
        """
            Clear activations for this synapse

            @author     Thiago F Pappacena
            @param      void
            @return     void    void
        """
        self.actualBackwardActivation = None
        self.actualActivation = None
        self.inputNeuron.clear()
        self.outputNeuron.clear()
    # end :: clear


    def sendForward(self):
        self.outputNeuron.activate()
    # end :: sendForward

# end :: Synapse
