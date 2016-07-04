from pygenalg import Population
import random

class RandomChooser(object):
    """
        Class that chooses random number of individuals from a given population

        @abstract
        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build the Population Chooser

            @author     Thiago F Pappacena
        """
        pass
    # end :: __init__


    def choose(self, population, number):
        """
            Choose a number of chromossomes from the population

            @abstract
            @author     Thiago F Pappacena
            @param      integer     number          The number of choosen individuals
            @param      object      population      A Population object
            @return     object      Another population, only with choosen chromossomes
        """
        return Population([random.choice(population.getChromossomes()) for i in xrange(number)])
    # end :: choose

# end :: RandomChooser
