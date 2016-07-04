from pygenalg import Chromossome, Population
from pygenalg.operator import GeneticOperator
from pygenalg.choose import RandomChooser

class SimpleCrossover(GeneticOperator):
    """
        A class to implement a single-point crossover operator

        @author     Thiago F Pappacena
    """
    

    def __init__(self, position = None, rate = 0.99, chooser = RandomChooser()):
        """
            Build a simple crossover operator, spliting genes in the defined position

            @author     Thiago F Pappacena
            @param      integer     position    The position where to split the genes
            @param      float       rate        The population percentage to cross
            @param      object      chooser     The PopulationChooser object to choose who to cross
        """
        GeneticOperator.__init__(self)
        self.position = None
        self.rate = rate
        self.chooser = chooser
    # end :: __init__


    def getPosition(self): return self.position
    def setPosition(self, position): self.position = position
    def getRate(self): return self.rate
    def setRate(self, rate): self.rate = rate
    def getChooser(self): return self.chooser
    def setChooser(self, chooser): self.chooser = chooser


    def operate(self, population):
        """
            Execute the crossovers in the population

            @author     Thiago F Pappacena
            @param      object      population  The population object
            @return     object      The new population
        """
        totalNewChromossomes = int(round(len(population) * self.rate))
        chromossomes = population.getChromossomes()
        choosen = [i for i in self.chooser.choose(population, totalNewChromossomes * 2)]         # choose individuals
        pairs = zip(choosen[:totalNewChromossomes], choosen[totalNewChromossomes:]) # make pairs

        return Population([self.cross(*pair) for pair in pairs])
    # end :: operate


    def cross(self, chromossome1, chromossome2):
        """
            Returns a new chromossome, mixing genes from both chromossomes

            @author     Thiago F Pappacena
            @param      object      chromossome1    The first father
            @param      object      chromossome2    The mother :P
            @return     object      A new population
        """
        c1Genes = tuple(g.copy() for g in chromossome1.getGenes())
        c2Genes = tuple(g.copy() for g in chromossome2.getGenes())

        position = self.position is not None and self.position or int(len(c1Genes)/2.0)

        return Chromossome(c1Genes[:position] + c2Genes[position:])
    # end :: cross

# end :: SimpleCrossover
