from pygenalg import Population
from pygenalg.gene import NumericGene
from pygenalg.modifier import Mutation
import random

class RandomCreepMutation(Mutation):
    """
        A creep mutation operator 

        This operator try to apply a delta (adding or subtracting) to
        a numeric gene actual value

        @author     Thiago F Pappacena
    """

    def __init__(self, probability = 0.01, percentAdjust = 0.1):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      float   probability     The probability (between 0 and 1) of mutating someone
        """
        super(RandomCreepMutation, self).__init__()
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
            g = random.choice(chromo.getGenes())
            if not isinstance(g, NumericGene):
                return
            actualValue = g.getValue()
            if int(rand * 10):
                newValue = actualValue + actualValue * self.percentAdjust
            else:
                newValue = actualValue - actualValue * self.percentAdjust
            g.setValue(newValue)
            chromo.setFitness(None)
    # end :: modify

# end :: RandomCreepMutation
