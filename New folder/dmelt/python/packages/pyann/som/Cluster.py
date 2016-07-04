import pyvetmath as vetmath
import math
from pyann.som import SOMDimensionsMissmatchException

class Cluster(object):
    
    def __init__(self, weights, ID):
        """
            Build the Cluster

            @author     Thiago F Pappacena
            @param      mixed       weights     If it's a tuple, it will be the weights itself. If is's an integer, will be the number of dimensions of the weights vector
            @param      mixed       ID          The cluster identification
        """
        if type(weights) == type(()):   # if it a tuple, it's the vector of weights
            self.weights = weights
        else:                           # otherwise, it's the number of dimensions of the weights vector
            self.weights = vetmath.makeEmptyVector(weights)

        self.ID = ID
    # end :: __init__

    
    def getTotalInput(self, input):
        """
            Returns the sum of the square differences between the weights vector and the input vector

            @author     Thiago F Pappacena
            @param      tuple       input       The input vector
            @return     double      The sum of pow(weights[i] - input[i], 2)
        """
        if len(input) != len(self.weights):
            raise SOMDimensionsMissmatchException('Input size: %d / weights size: %d' % (len(input), len(self.weights)))

        return sum( [   math.pow((self.weights[i] - input[i]), 2)   for i in xrange(0, len(input))  ] )    # it's raising precision problems
        #return sum( [   abs((self.weights[i] - input[i]))   for i in xrange(0, len(input))  ] )
    # end :: getTotalInput


    def ajustWeights(self, input, learnRate):

        if len(input) != len(self.weights):
            raise SOMDimensionsMissmatchException('Input size: %d / weights size: %d' % (len(input), len(self.weights)))

        self.weights = tuple( [self.weights[i] + learnRate * (input[i] - self.weights[i]) for i in xrange(0, len(self.weights))] )
    # end :: ajustWeights


    def getWeights(self):
        return self.weights

    def getID(self):
        return self.ID

# end :: self.Cluster
