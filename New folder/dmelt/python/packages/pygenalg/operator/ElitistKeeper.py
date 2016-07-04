from pygenalg import Population
from pygenalg.operator import GeneticOperator

class ElitistKeeper(GeneticOperator):
    """
        A class to keep to next generation the best individuals

        @author     Thiago F Pappacena
    """

    def __init__(self, rate = 0.01):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      float   rate    The percentage rate of best individuals to keep
        """
        super(ElitistKeeper, self).__init__()
        self.rate = rate
    # end :: __init__


    def operate(self, population):
        """
            Execute the genetic operation in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        toKeep = int(round(len(population) * self.rate))
        return Population( population.getChromossomes()[:toKeep] )
    # end :: operate

# end :: ElitistKeeper
