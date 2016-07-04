from pygenalg import Chromossome, Population
from pygenalg.operator import SimpleCrossover
from pygenalg.choose import SimpleRouletChooser

class ArithmeticAverageCrossover(SimpleCrossover):
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
        c1Fit = chromossome1.getFitness()
        c2Fit = chromossome2.getFitness()
        sumFit = c1Fit + c2Fit
        c1RelFit = c1Fit / sumFit
        c2RelFit = c2Fit / sumFit

        c1Genes = tuple(g.copy().getValue() for g in chromossome1.getGenes())
        c2Genes = tuple(g.copy().getValue() for g in chromossome2.getGenes())
        genotype = tuple(x.__class__ for x in chromossome1.getGenes())

        values = tuple((c1RelFit * x[0] + c2RelFit * x[1]) for x in zip(c1Genes, c2Genes))
        return Chromossome([x[0](x[1]) for x in zip(genotype, values)])
    # end :: cross

# end :: ArithmeticAverageCrossover
