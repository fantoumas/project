from pygenalg import Chromossome, Population
from pygenalg.operator import SimpleCrossover
from pygenalg.choose import RandomChooser
import random

class MultiPointCrossover(SimpleCrossover):
    """
        A class to implement a multi-point crossover

        @author     Thiago F Pappacena
    """
    

    def __init__(self, points = None, rate = 0.99, chooser = RandomChooser()):
        """
            Build a simple crossover operator, spliting genes in the defined position

            @author     Thiago F Pappacena
            @param      mixed       points      If points is an integer, cross in $points random positions
                                                If points is a tuple of integers, cross in that points
            @param      float       rate        The population percentage to cross
            @param      object      chooser     The PopulationChooser object to choose who to cross
        """
        SimpleCrossover.__init__(self, position = None, rate = rate, chooser = chooser)
        if not isinstance(points, int):
            points = list(points)
            points.sort()
        self.points = points
    # end :: __init__


    def getPoints(self): return self.points
    def setPoints(self, points): 
        if not isinstance(points, int):
            points = list(points)
            points.sort()
        self.points = points
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
            @return     object      A new chromossome
        """
        c1Genes = tuple(g.copy() for g in chromossome1.getGenes())
        c2Genes = tuple(g.copy() for g in chromossome2.getGenes())
        lenGenes = len(c1Genes)

        if isinstance(self.points, int):
            points = [random.randrange(lenGenes) for i in range(self.points)]
            points.sort()
        else:
            points = self.points

        genes = []
        start = 0
        for end in points:
            genesList = random.random() > 0.5 and c1Genes or c2Genes
            genes += genesList[start:end]
            start = end
        genes += random.random() > 0.5 and c1Genes[start:] or c2Genes[start:]

        return Chromossome(genes)
    # end :: cross

# end :: MultiPointCrossover
