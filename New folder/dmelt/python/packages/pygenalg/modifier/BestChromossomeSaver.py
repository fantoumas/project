from pygenalg.modifier import GeneticPopulationModifier
from pygenalg import Chromossome

class BestChromossomeSaver(GeneticPopulationModifier):
    """
        Save the best chromossome

        @author     Thiago F Pappacena
    """

    def __init__(self, save = 1):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      integer     save    The number of individuals do save
        """
        GeneticPopulationModifier.__init__(self)
        self.save = save
        self.chromossomes = []
    # end :: __init__


    def modify(self, population):
        """
            Execute the modifier in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        self.chromossomes = [Chromossome([gene.copy() for gene in chromo.getGenes()]) for chromo in population.getChromossomes()[:self.save]]
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
