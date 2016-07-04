from pygenalg import *
from pyann.mlp import Network


class GeneticTrainerFitness(FitnessFunction):
    """
        A genetic trainer fitness function
        
        @author     Thiago F Pappacena
    """

    def __init__(self, netArch = None, patterns = None):
        """
            Build the fitness function

            @author     Thiago F Pappacena
            @param      list    patterns    The list of patterns to check the fitness
            @author     tuple   netArch     List of (layer type, layer size) for net (as returned by Network.getDimensions method)
        """
        FitnessFunction.__init__(self)
        self.patterns = patterns
        self.netArch = netArch
    # end :: __init__

    def setPatterns(self, patterns):
        """
            Se the patterns to use in avaliation
        """
        self.patterns = patterns
    # end :: setPatterns


    def evaluate(self, chromossome):
        """
            Evaluate a chromossome and check it's fitness to patterns
            
            @author     Thiago F Pappacena
            @param      object  chromossome     The chromossome to check
            @return     float   The fitness of the chromossome
        """
        weights = tuple(i.getValue() for i in chromossome.getGenes())
        net = Network.fromPlanifiedWeights(self.netArch, weights)
        error = 0.0
        for p in self.patterns:
            net.clearActivations()
            error += sum( (i[1] - i[0])**2 for i in zip(net.getOutput(p.getInput()), p.getOutput()) ) / 2.0
        return -error
    # end :: evaluate

# end : GeneticTrainerFitness
