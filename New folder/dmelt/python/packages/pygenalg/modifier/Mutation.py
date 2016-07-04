from pygenalg import Population
from pygenalg.modifier import GeneticPopulationModifier
import random

class Mutation(GeneticPopulationModifier):
    """
        A mutation operator

        @author     Thiago F Pappacena
    """

    def __init__(self, probability = 0.01):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      float   probability     The probability (between 0 and 1) of mutating someone
        """
        super(Mutation, self).__init__()
        self.probability = probability
    # end :: __init__


    def getProbability(self): return self.probability
    def setProbability(self, probability): self.probability = probability


    def modify(self, population):
        """
            Execute the mutation operation in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        if random.random() <= self.probability:
            random.choice(population.getChromossomes()).mutate()
    # end :: modify

# end :: Mutation
