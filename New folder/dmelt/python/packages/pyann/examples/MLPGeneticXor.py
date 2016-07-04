import pyann.mlp
import pyann.mlp.layer
import pyann.mlp.training.genetic
import pyann.mlp.monitoring
import pprint
import sys

try:
    import psyco
    psyco.full()
except:
    print >> sys.stderr, 'Bad, bad psyco!'

# Building net
#layers = (pyann.mlp.layer.SigmoidInputLayer(2), pyann.mlp.layer.SigmoidLayer(3), pyann.mlp.layer.SigmoidOutputLayer(1))
layers = (pyann.mlp.layer.SigmoidInputLayer(2), pyann.mlp.layer.SigmoidLayer(5), pyann.mlp.layer.SigmoidOutputLayer(1))

net = pyann.mlp.Network( layers )

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
monitor = pyann.mlp.monitoring.VerboseMonitor()

stopOnMaxIter = pyann.mlp.training.MaxIterationsStopCondition(2500)
stopOnMinError = pyann.mlp.training.MinErrorStopCondition(0.001)

trainer = pyann.mlp.training.genetic.GeneticTrainer(net, monitor, populationSize = 30)
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
