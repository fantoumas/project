import pyann.mlp
import pyann.mlp.training.genetic
import pyann.mlp.monitoring
import math
import random
import sys

try:
    import psyco
    psyco.full()
except:
    print >> sys.stderr, 'No psyco found. If you\'re using a x86 machine, psyco might'\
                            'speedup things here. Install it!'

"""
    This example builds a Backpropagation MLP that can
    learn a senoidal function between -1 and 1
"""

WINDOW = 5
MIN_VALUE = -1
MAX_VALUE = 1

pyann.mlp.training.genetic.WeightGene.MIN_VALUE = MIN_VALUE
pyann.mlp.training.genetic.WeightGene.MAX_VALUE = MAX_VALUE

# Building net
layers = (  pyann.mlp.layer.SigmoidInputLayer(WINDOW, minValue = MIN_VALUE, maxValue = MAX_VALUE), 
            #pyann.mlp.layer.SigmoidLayer(5, minValue = MIN_VALUE, maxValue = MAX_VALUE), 
            pyann.mlp.layer.SigmoidLayer(3, minValue = MIN_VALUE, maxValue = MAX_VALUE), 
            pyann.mlp.layer.SigmoidOutputLayer(1, minValue = MIN_VALUE, maxValue = MAX_VALUE)   )

net = pyann.mlp.Network( layers )

# Build data set
data = []
for i in range(-360, 361, 10):
    data.append(math.sin(i))

# Build patterns
start = len(data) - WINDOW - 1
patterns = []
while len( data[start : start+WINDOW] ) == WINDOW:
    input = tuple(data[start : start+WINDOW])
    output = (data[start+WINDOW], )
    patterns.append(pyann.mlp.Pattern(input = input, output = output))
    start -= 1


# Train the net
raw_input('Training net with %s patterns. Press <enter> to continue.' % (len(patterns)))

monitor = pyann.mlp.monitoring.VerboseMonitor()

stopOnMaxIter = pyann.mlp.training.MaxIterationsStopCondition(1500)
stopOnMinError = pyann.mlp.training.MinErrorStopCondition(0.01)

trainer = pyann.mlp.training.genetic.GeneticTrainer(net, monitor, populationSize = 10)
trainer.setStopConditions((stopOnMaxIter, stopOnMinError), joiner = 'or')

trainInfo = trainer.train(patterns)
print """
Epochs: %(epoch)s
Final error: %(error)s
Validation set error: %(validationError)s
""" % { 'epoch': trainInfo.getIterationNumber(),
        'error': trainInfo.getError(),
        'validationError': trainInfo.getValidationSetError() }

print net.planify()
for i in range(370, 725, 10):
    start = len(data) - WINDOW
    predicted = net.classify( tuple(data[start:]) )[0]
    data.append(predicted)
    print 'sin(%s) = %s' % (i, predicted)
