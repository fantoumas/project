from pyann.mlp.training import Trainer, IterationInfo
from pyann.mlp import InputLayer
# import fpconst
import random

class BackpropagationTrainer(Trainer):
    """
        Backpropagation algorithm

        @author     Thiago F Pappacena
    """
    
    def __init__(self, network = None, monitor = None, learningRate = 1.0, momentum = 0.0, batch = False, randomize = False):
        """
            Build the backpropagation trainer

            @author     Thiago F Pappacena
            @param      object  network         The network to be trained
            @param      object  monitor         The object training Monitor
            @param      float   learningRate    The learn rate to be used
            @param      float   momentum        Momentum rate to be used
            @param      boolean batch           Bach weight updates?
            @param      boolean randomize       Randomize the patterns while presenting it to net?
        """
        super(BackpropagationTrainer, self).__init__(network, monitor)
        self.learningRate = learningRate
        self.momentum = momentum
        self.batch = batch
        self.randomize = randomize
    # end :: __init__


    def setLearningRate(self, learningRate):
        """
            Sets the learning rate

            @author     Thiago F Pappacena
            @param      float   learningRate    The learn rate
            @return     void
        """
        self.learningRate = learningRate
    # end :: setLearningRate


    def setMomentum(self, momentum):
        """
            Sets the momentum

            @author     Thiago F Pappacena
            @param      float   momentum    The momentum rate
            @return     void
        """
        self.momentum = momentum
    # end :: setMomentum


    def setBatch(self, batch):
        """
            Defines the batch weight update mode

            @author     Thiago F Pappacena
            @param      boolean     batch   True to use batch weigth update. False otherwise
            @return     void
        """
        self.batch = batch
    # end :: setBatch


    def getBatch(self):
        """
            Gets the batch weight update mode

            @author     Thiago F Pappacena
            @param      void        void
            @return     boolean     The batch update mode
        """
        return self.batch
    # end :: getBatch


    def setRandomize(self, randomize):
        """
            Set the randomization mode of patterns presenting

            @author     Thiago F Pappacena
            @param      boolean     randomize   True to randomize patterns. False otherwise
            @return     void
        """
        self.randomize = randomize
    # end :: setRandomize


    def getRandomize(self):
        """
            Gets the actual randomization mode of patterns presenting

            @author     Thiago F Pappacena
            @param      void        void
            @return     boolean     The randomization mode
        """
        return self.randomize
    # end :: getRandomize

    
    def train(self, patterns, validationSet = []):
        """
            Execute the training

            @author     Thiago F Pappacena
            @param      list    patterns        The list of patterns
            @param      list    validationSet   The list of patterns to be used in validation
            @return     object  The last IterationInfo object
        """
        iterInfo = IterationInfo()
        iterInfo.setIterationNumber(0)
        # iterInfo.setError(fpconst.PosInf)
        iterInfo.setError(1000000)
        iterInfo.setErrorDelta(0)
        iterInfo.setNetwork(self.net)

        patterns = patterns[:]
        
        while not self.mustStopTraining(iterInfo):
            # do the training...

            # randomize patterns?
            if self.randomize:
                random.shuffle(patterns)

            E = 0.0     # clear global error
            for pattern in patterns:
                self.net.clearActivations()

                outputLayer = self.net.getOutputLayer()
                hiddenLayers = self.net.getHiddenLayers()
                inputLayer = self.net.getInputLayer()
                synapseLayers = self.net.getSynapseLayers()

                desired = tuple( map(float, pattern.getOutput()) )   # get desired output from pattern
                output = tuple( map(float, self.net.getOutput( pattern.getInput() )) ) # Present pattern to the net...
                E += sum( ((desired[i] - output[i])**2 for i in range(len(output))) ) / 2.0

                # get output error term and deltas
                outputErrorTerm = tuple( ((desired[i] - output[i])*outputLayer[i].applyOutputDerivativeFunction(outputLayer[i].getActualInputSum()) for i in range(len(desired))) )
                outputDeltas = tuple( (self.learningRate * outputErrorTerm[i] for i in range(len(outputLayer))) )



                # Back-activate output layer with error information term
                outputLayer.setBackwardActivations(outputErrorTerm)
                for i in range(len(synapseLayers)-1, -1, -1):
                    synapseLayers[i].sendBackward()
                
                # calculate output error term and delta for hidden layers
                lenHiddenLayers = len(hiddenLayers)
                hiddenErrorTerm = [0.0] * lenHiddenLayers
                hiddenOutputs = [0.0] * lenHiddenLayers
                hiddenDeltas = [0.0] * lenHiddenLayers
                for h in range(lenHiddenLayers-1, -1, -1):
                    layer = hiddenLayers[h]
                    lenLayer = len(hiddenLayers[h])
                    hiddenErrorTerm[h] = tuple( (layer[i].getBackwardOutput() for i in range(lenLayer)) )
                    hiddenDeltas[h] = tuple( (self.learningRate * hiddenErrorTerm[h][i] for i in range(lenLayer)) )



                """
                print '\n\n$$$$ RESUMED ACTIVATIONS $$$$'
                print '*** weight matrixes ***'
                for syn in self.net.getSynapseLayers():
                    print 'bias: %s' % [n.bias for n in syn.outputLayer]
                    print 'syn matrix: %s' % [[j.weight for j in i] for i in syn.connectionsMatrix]
                print '\n\nfeed-forward ------>'
                print 'input activations: %s' % list(self.net.getInputLayer().getOutput())
                for lay in self.net.getHiddenLayers():
                    print 'hidden total input: %s' % ([n.getActualInputSum() for n in lay])
                    print 'hidden activations: %s' % list(lay.getOutput())
                print '\noutput input sums: %s' % [n.getActualInputSum() for n in self.net.getOutputLayer()]
                print 'output activations: %s' % list(self.net.getOutputLayer().getOutput())

                print '\n\nbackward ------>'
                print 'output backprop: %s' % list(self.net.getOutputLayer().getBackwardOutput())
                for lay in self.net.getHiddenLayers():
                    print 'hidden backprop: %s' % list(lay.getBackwardOutput())

                print '\n\nerror terms -------->'
                print 'output error term: %s' % outputErrorTerm
                print 'hidden error term: %s' % hiddenErrorTerm

                print '\n\ndeltas -------->'
                print 'output deltas: %s' % outputDeltas
                print 'hidden deltas: %s' % hiddenDeltas

                raw_input()

                """

                # Apply output deltas
                for i in range(len(outputLayer)):
                    neuron = outputLayer[i]
                    delta = outputDeltas[i]
                    momentum = neuron.getLastWeightDelta() * self.momentum
                    neuron.adjustWeights(delta + momentum)

                # Apply deltas to hidden layers
                for h in range(lenHiddenLayers):
                    layer = hiddenLayers[h]
                    for i in range(len(layer)):
                        neuron = layer[i]
                        delta = hiddenDeltas[h][i]
                        momentum = neuron.getLastWeightDelta() * self.momentum
                        neuron.adjustWeights(delta + momentum)

            # end of training cycle

            self.net.clearActivations()


            validationSetError = 0
            for pattern in validationSet:
                desired = pattern.getOutput()   # get desired output from pattern
                output = self.net.classify( pattern.getInput() )
                errors = tuple( ((desired[i] - output[i])**2 for i in range(len(desired))) )
                validationSetError += sum(errors)



            newError = E    # put new error here! :P
            iterInfo.adjustErrorDelta(newError)
            iterInfo.setError(newError)
            iterInfo.increaseIterationNumber()
            iterInfo.setValidationSetError(validationSetError)

            if self.monitor:
                self.monitor.monitore( iterInfo )
        return iterInfo
    # end :: train

# end :: BackpropagationTrainer
