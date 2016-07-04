from pygenalg.modifier import GeneticPopulationModifier
from pygenalg import Chromossome

class BestChromossomeRestorer(GeneticPopulationModifier):
    """
        Restore to population the best chromossome saved by BestChromossomeSaver object

        @author     Thiago F Pappacena
    """

    def __init__(self, saver):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      object  saver   The BestChromossomeSaver object that is storing the best of a population
        """
        GeneticPopulationModifier.__init__(self)
        self.saver = saver
    # end :: __init__


    def modify(self, population):
        """
            Execute the modifier in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        for i in self.saver.pop():
            population.addChromossome(i)
    # end :: modify


    def pop(self):
        """
            Pop the list of individuals from this saver
        """
        r = self.chromossomes
        self.chromossome = []
        return r
    # end :: pop

# end :: GeneticPopulationModifier
