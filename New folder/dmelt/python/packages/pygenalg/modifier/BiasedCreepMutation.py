from pygenalg import Population
from pygenalg.gene import NumericGene
from pygenalg.modifier import Mutation
import random

class BiasedCreepMutation(Mutation):
    """
        A creep mutation operator 

        This operator try to apply a delta (adding or subtracting) to
        a numeric gene actual value

        @author     Thiago F Pappacena
    """

    def __init__(self, probability = 0.01, percentAdjust = 0.5):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      float   probability     The probability (between 0 and 1) of mutating someone
        """
        super(BiasedCreepMutation, self).__init__()
        self.probability = probability
        self.percentAdjust = percentAdjust
    # end :: __init__


    def getProbability(self): return self.probability
    def setProbability(self, probability): self.probability = probability
    def setPercentAdjust(self, percentAdjust): self.percentAdjust = percentAdjust
    def getPercentAdjust(self): return self.percentAdjust


    def modify(self, population):
        """
            Execute the creep mutation operation in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        rand = random.random()
        if rand <= self.probability:
            chromo = random.choice(population.getChromossomes())
            mutationCandidates = chromo.getGenes()
            geneIndex = random.randrange(0, len(mutationCandidates))
            g = mutationCandidates[ geneIndex ]
            if not isinstance(g, NumericGene):
                return
            target = population.getChromossomes()[0].getGenes()[ geneIndex ].getValue()
            actualValue = g.getValue()
            diff = target - actualValue
            if diff > 0:
                newValue = actualValue + diff * self.percentAdjust
            else:
                newValue = actualValue - diff * self.percentAdjust
            g.setValue(newValue)
            chromo.setFitness(None)
    # end :: modify

# end :: BiasedCreepMutation
