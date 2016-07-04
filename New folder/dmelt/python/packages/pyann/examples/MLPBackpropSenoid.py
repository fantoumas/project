import pyann.mlp
import pyann.mlp.training.backprop
import pyann.mlp.monitoring
import math
import random
import sys

try:
    import psyco
    psyco.full()
except:
    print >> sys.stderr, 'No psyco!'

"""
    This example builds a Backpropagation MLP that can
    learn a senoidal function between -1 and 1
"""

WINDOW = 10
MIN_VALUE = -1
MAX_VALUE = 1

# Building net
layers = (  pyann.mlp.layer.SigmoidInputLayer(WINDOW), 
            #pyann.mlp.layer.SigmoidLayer(5, minValue = MIN_VALUE, maxValue = MAX_VALUE), 
            pyann.mlp.layer.SigmoidLayer(5), 
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

# build validation patterns
validationPatterns = []
for i in range(int(len(patterns)*0.2)): # 20% for validation set
    validationPatterns.append( patterns.pop(random.randrange(len(patterns))) )


# Train the net
raw_input('Training net with %s patterns and %s validation patterns. Press <enter> to continue.' % (len(patterns), len(validationPatterns)))

monitor = pyann.mlp.monitoring.VerboseMonitor()

stopOnMaxIter = pyann.mlp.training.MaxIterationsStopCondition(500)
stopOnMinError = pyann.mlp.training.MinErrorStopCondition(0.01)
stopOnVMinError = pyann.mlp.training.MinValidationErrorStopCondition(0.005)

trainer = pyann.mlp.training.backprop.BackpropagationTrainer(net, monitor)
trainer.setLearningRate(0.7)
trainer.setMomentum(0.5)
trainer.setRandomize(True)     # randomize patterns presentation
#trainer.setBatch(True)          # batch update weights
trainer.setStopConditions((stopOnMaxIter, stopOnMinError, stopOnVMinError), joiner = 'or')

trainInfo = trainer.train(patterns, validationPatterns)
print """
Epochs: %(epoch)s
Final error: %(error)s
Validation set error: %(validationError)s
""" % { 'epoch': trainInfo.getIterationNumber(),
        'error': trainInfo.getError(),
        'validationError': trainInfo.getValidationSetError() }

for i in range(370, 725, 10):
    start = len(data) - WINDOW
    predicted = net.classify( tuple(data[start:]) )[0]
    data.append(predicted)
    print 'sin(%s) = %s' % (i, predicted)
