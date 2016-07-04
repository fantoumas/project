from pygenalg.choose import PopulationChooser
from pygenalg import Population
import random

class SimpleRouletChooser(PopulationChooser):
    """
        Simple roulet population chooser

        @author     Thiago F Pappacena
    """


    def __init__(self):
        """
            Build the simple roulet

            @author     Thiago F Pappacena
            @param      void        void
        """
        PopulationChooser.__init__(self)
    # end :: __init__


    def choose(self, population, number):
        """
            Choose a number of individuals of the population based on the fitness function

            @author     Thiago F Pappacena
            @author     Thiago F Pappacena
            @param      integer     number          The number of choosen individuals
            @param      object      population      A Population object
            @return     object      Another population, only with choosen chromossomes
        """
        if number >= len(population):
            return population

        chromossomes = population.getChromossomes()
        roulet       = self.__buildRoulet(chromossomes)

        choosen = set(self.__pick(roulet) for x in xrange(0, number))
        while(len(choosen) < number):
            choosen.add( self.__pick(roulet) )
         
        return Population(list(choosen))
    # end :: choose
    


    def __buildRoulet(self, chromossomes):
        """
            Build a roulet based in chromossomes and it's results from fitness function

            @author     Thiago F Pappacena
            @param      list    chromossomes    The list of chromossomes
            @return     dict    The dictionary where keys are probabilistic of chromossome to survive
        """
        absoluteFitness = [x.getFitness() for x in chromossomes]
        #absoluteFitness.sort()
        sumFitness      = sum(absoluteFitness)

        # build roulet
        relativeFitness = {}
        actual = 0
        for i in xrange(0, len(chromossomes)):
            relFit = float(absoluteFitness[i])/sumFitness
            index = relFit + actual
            if index not in relativeFitness:
                relativeFitness[index] = []
            relativeFitness[ relFit + actual ].append(chromossomes[i])
            actual += relFit

        return relativeFitness
    # end :: __buildRoulet

    
    def __pick(self, roulet):
        """
            Pick a random chromossome from the roulet, based on the probabilities

            @author     Thiago F Pappacena
            @param      dict        roulet      The roulet build with __buildRoulet() method
            @return     object      A chromossome
        """
        randNumber = random.random()
        for k in sorted(roulet):
            if randNumber <= k:
                v = roulet[k]
                if not len(v):
                    break
                choosen = random.choice(v)
                v.remove(choosen)
                return choosen

        # Ok... could not return nobody... return anyone
        for i in roulet:
            if len(roulet[i]):
                return roulet[i][0]
    # end :: __pick
