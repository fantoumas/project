from pygenalg.modifier import GeneticPopulationModifier

class PopulationSorter(GeneticPopulationModifier):
    """
        Sort the population from best fitness to worst

        @author     Thiago F Pappacena
    """

    def __init__(self, fitnessFunction):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      object  fitnessFunction The fitness function to eval population
        """
        self.fitFunc = fitnessFunction
    # end :: __init__


    def modify(self, population):
        """
            Sort the individuals in the population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        population.sort(self.fitFunc)
    # end :: modify

# end :: PopulationSorter
