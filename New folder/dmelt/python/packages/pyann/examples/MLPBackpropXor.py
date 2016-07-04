import pyann.mlp
import pyann.mlp.layer
import pyann.mlp.training.backprop
import pyann.mlp.monitoring
import pprint

# Building net
"""
    Classes:
        (abstract)  Layer
                    |__ SigmoidLayer(numberOfUnits)
                    Network(tupleOfLayers)
                        + getOutput(inputTuple)
                    Pattern(input,output)
"""
#layers = (pyann.mlp.SigmoidInputLayer(2), pyann.mlp.SigmoidLayer(4), pyann.mlp.SigmoidOutputLayer(1))  # FAUSSET topology
#layers = (pyann.mlp.SigmoidInputLayer(2), pyann.mlp.SigmoidLayer(2), pyann.mlp.SigmoidOutputLayer(1))
#layers = (pyann.mlp.SigmoidInputLayer(2), pyann.mlp.SigmoidLayer(2), pyann.mlp.SigmoidOutputLayer(1))   # BPNN sample
layers = (pyann.mlp.layer.SigmoidInputLayer(2), pyann.mlp.layer.SigmoidLayer(3), pyann.mlp.layer.SigmoidOutputLayer(1))

net = pyann.mlp.Network( layers )





# FORCING FOR PYTHON BPNN SAMPLE
"""
synLayers = net.getSynapseLayers()

intohidden = synLayers[0].connectionsMatrix
hidden = net.getHiddenLayers()[0]

intohidden[0][0].weight = 0.495
intohidden[0][1].weight = -0.382
intohidden[1][0].weight = 0.123
intohidden[1][1].weight = -0.432

hidden[0].bias = 0.41
hidden[1].bias = -0.22

hiddentoout = synLayers[1].connectionsMatrix
outputLayer = net.getOutputLayer()
hiddentoout[0][0].weight = 0.33
hiddentoout[0][1].weight = -0.25
outputLayer[0].bias = 0
"""
# END :: FORCING FOR PYTHON BPNN SAMPLE


# FORCING FOR FAUSSET EXAMPLE VALUES (FAUSSET94, page 300)
"""
synLayers = net.getSynapseLayers()

intohidden = synLayers[0].connectionsMatrix
hidden = net.getHiddenLayers()[0]
intohidden[0][0].weight = 0.1970
intohidden[1][0].weight = 0.3191
intohidden[2][0].weight = -0.1448
intohidden[3][0].weight = 0.3594
intohidden[0][1].weight = 0.3099
intohidden[1][1].weight = 0.1970
intohidden[2][1].weight = -0.0347
intohidden[3][1].weight = -0.4861

hidden[0].bias = -0.3378
hidden[1].bias = 0.2771
hidden[2].bias = 0.2859
hidden[3].bias = -0.3329


hiddentoout = synLayers[1].connectionsMatrix
outputLayer = net.getOutputLayer()
hiddentoout[0][0].weight = 0.4919
hiddentoout[0][1].weight = -0.2913
hiddentoout[0][2].weight = -0.3979
hiddentoout[0][3].weight = 0.3581
outputLayer[0].bias = -0.1401
"""
# END :: FORCING FOR FAUSSET EXAMPLE VALUES (FAUSSET94, page 300)


# FORCING A GOOD EXAMPLE
"""
netWeights = net.getWeightMatrix()
pprint.pprint(net.getWeightMatrix())

newW = (    (   (0.60105502085746354, 2.0068750042980206), (1.9011117158884758, 1.573929759124068), (6.5038657960661412, 5.9791681600377027) ), 
            (   (-5.42186475418164, -15.879583943244249, 14.257866328393369),)
    )
net.setWeightMatrix(newW)
print '\n\n\n'
pprint.pprint(net.getWeightMatrix())
"""
# END :: FORCING A GOOD EXAMPLE



# Testing before training
print "***** Testing the network before learning ***** "
print '0.0 xor 0.0 = %s' % net.classify((0.0, 0.0))[0]
print '1.0 xor 1.0 = %s' % net.classify((1.0, 1.0))[0]
print '1.0 xor 0.0 = %s' % net.classify((1.0, 0.0))[0]
print '0.0 xor 1.0 = %s' % net.classify((0.0, 1.0))[0]
raw_input()

# Build patterns
patterns = []
patterns.append( pyann.mlp.Pattern(input=(0.0, 0.0), output=(0.0,)) )
patterns.append( pyann.mlp.Pattern(input=(0.0, 1.0), output=(1.0,)) )
patterns.append( pyann.mlp.Pattern(input=(1.0, 0.0), output=(1.0,)) )
patterns.append( pyann.mlp.Pattern(input=(1.0, 1.0), output=(0.0,)) )

# Training network
"""
    Classes:
        (abstract)  StopCondition
                        |__ MaxIterationsStopCondition(iterations)
                        |__ MinErrorStopCondition(error)
        (abstract)  Trainer
                        + setStopConditions(tupleOfConditions, joiner = 'or'|'and')
                        |__ BackpropagationTrainer
"""
monitor = pyann.mlp.monitoring.VerboseMonitor()

#stopOnMaxIter = pyann.mlp.training.MaxIterationsStopCondition(1500)
stopOnMaxIter = pyann.mlp.training.MaxIterationsStopCondition(15000)
stopOnMinError = pyann.mlp.training.MinErrorStopCondition(0.0015)

trainer = pyann.mlp.training.backprop.BackpropagationTrainer(net, monitor)
trainer.setLearningRate(0.7)
trainer.setMomentum(0.3)
trainer.setStopConditions((stopOnMaxIter, stopOnMinError), joiner = 'or')

trainInfo = trainer.train(patterns)
print """
Epochs: %(epoch)s
Final error: %(error)s
Validation set error: %(validationError)s
""" % { 'epoch': trainInfo.getIterationNumber(),
        'error': trainInfo.getError(),
        'validationError': trainInfo.getValidationSetError() }

#net.setWeightMatrix(newW)
print '\n\nFinal weights:\n'
pprint.pprint(net.getWeightMatrix(), )
print '\n\n'

# Testing the net
print "***** Testing the network AFTER learning ***** "
print '0.0 xor 0.0 = %s' % net.classify((0.0, 0.0))[0]
print '1.0 xor 1.0 = %s' % net.classify((1.0, 1.0))[0]
print '1.0 xor 0.0 = %s' % net.classify((1.0, 0.0))[0]
print '0.0 xor 1.0 = %s' % net.classify((0.0, 1.0))[0]
