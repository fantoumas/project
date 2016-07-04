from pygenalg.modifier import GeneticPopulationModifier
from pygenalg.choose import RandomChooser
import random

class DisasterCauser(GeneticPopulationModifier):
    """
        Causes a disaster in population!

        This modifier must be used with a low probability.
        It will kill a big portion of the population, choosing
        randomly from living chromossomes, to emulate something
        like what happened to dinos and mamals ;)

        @author     Thiago F Pappacena
    """

    def __init__(self, probability = 0.001, tokeep = 0.1, chooser = RandomChooser()):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      void    void
        """
        super(DisasterCauser, self).__init__()
        self.tokeep = tokeep
        self.probability = probability
        self.chooser = chooser
    # end :: __init__


    def modify(self, population):
        """
            Execute the modifier in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        if random.random() < self.probability:
            keep = int(len(population) * self.tokeep)
            if keep > 4:    # at least 2 couples, please! :P
                newPop = self.chooser.choose(population, keep)
                population.setChromossomes( newPop.getChromossomes() )
    # end :: modify

# end :: DisasterCauser
