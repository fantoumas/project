from pygenalg import Population
from pygenalg.operator import GeneticOperator
from pygenalg.choose import SimpleRouletChooser

class PopulationKeeper(GeneticOperator):
    """
        A class to keep individuals from a generation to the next

        @author     Thiago F Pappacena
    """

    def __init__(self, rate = 0.1, chooser = SimpleRouletChooser()):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      float   rate        The percentage rate to keep
            @param      object  chooser     The choosing method
        """
        super(PopulationKeeper, self).__init__()
        self.rate = rate
        self.chooser = chooser
    # end :: __init__


    def getRate(self): return self.rate
    def setRate(self, rate): self.rate = rate
    def getChooser(self): return self.chooser
    def setChooser(self, chooser): self.chooser = chooser


    def operate(self, population):
        """
            Execute the genetic operation in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        num = int(round(len(population) * self.rate))
        return self.chooser.choose(population, num)
    # end :: operate

# end :: PopulationKeeper
