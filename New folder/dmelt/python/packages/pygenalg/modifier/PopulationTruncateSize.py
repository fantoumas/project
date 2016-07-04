from pygenalg import Population
from pygenalg.modifier import GeneticPopulationModifier
from pygenalg.choose import SimpleRouletChooser
import random

class PopulationTruncateSize(GeneticPopulationModifier):
    """
        A population truncate size operator

        @author     Thiago F Pappacena
    """

    def __init__(self, maxSize, chooser = SimpleRouletChooser()):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      integer maxSize     Max population size
        """
        super(PopulationTruncateSize, self).__init__()
        self.maxSize = maxSize
        self.chooser = chooser
    # end :: __init__


    def getMaxSize(self): return self.maxSize
    def setMaxSize(self, maxSize): self.maxSize = maxSize
    def getChooser(self): return self.chooser
    def setChooser(self, chooser): self.chooser = chooser


    def modify(self, population):
        """
            Truncate the population to max size

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        if len(population) > self.maxSize:
            newPopulation = self.chooser.choose(population,self.maxSize)
            population.setChromossomes( newPopulation.getChromossomes() )
    # end :: modify

# end :: Mutation
