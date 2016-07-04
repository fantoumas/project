from pygenalg import Chromossome, Population
from pygenalg.operator import SimpleCrossover
from pygenalg.choose import SimpleRouletChooser

class AverageCrossover(SimpleCrossover):
    """
        A class to implement an average crossover

        The generated genes' value are the average value
        between it's father genes' value sum

        @author     Thiago F Pappacena
    """
    

    def __init__(self, rate = 0.99, chooser = SimpleRouletChooser()):
        """
            Build an average crossover operator, spliting genes in the defined position

            @author     Thiago F Pappacena
            @param      integer     position    The position where to split the genes
            @param      float       rate        The population percentage to cross
            @param      object      chooser     The PopulationChooser object to choose who to cross
        """
        SimpleCrossover.__init__(self, rate = rate, chooser = chooser)
        self.rate = rate
        self.chooser = chooser
    # end :: __init__


    def getRate(self): return self.rate
    def setRate(self, rate): self.rate = rate
    def getChooser(self): return self.chooser
    def setChooser(self, chooser): self.chooser = chooser

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
        genotype = tuple(x.__class__ for x in chromossome1.getGenes())

        values = tuple((x[0].getValue() + x[1].getValue())/2.0 for x in zip(c1Genes, c2Genes))
        return Chromossome([x[0](x[1]) for x in zip(genotype, values)])
    # end :: cross

# end :: AverageCrossover
