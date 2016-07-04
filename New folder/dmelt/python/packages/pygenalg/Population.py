from pygenalg import Chromossome

class Population(object):
    """
        A population: a collection of candidates (chromossomes) for solving a problem

        @author     Thiago F Pappacena
    """

    def __init__(self, chromossomes = []):
        """
            Build the population

            @author     Thiago F Pappacena
            @param      list    chromossomes        The list of chromossomes
        """
        self.chromossomes = chromossomes
    # end :: __init__

    
    def getSize(self):
        """
            Returns the size of the population (number of individuals)

            @author     Thiago F Pappacena
            @param      void        void
            @return     integer     The number of individuals
        """
        return len(self.chromossomes)
    # end :: getSize


    def getChromossomes(self):
        """
            Returns a list of all chromossomes in the population

            @author     Thiago F Pappacena
            @param      void        void
            @return     list        The list of chromossomes
        """
        return self.chromossomes
    # end :: getChromossomes


    def setChromossomes(self, chromossomes):
        """
            Sets the chromossomes in population

            @author     Thiago F Pappacena
            @param      list    chromossomes    The list of chromossomes
            @return     void
        """
        self.chromossomes = chromossomes
    # end :: setChromossomes


    def addChromossome(self, chromossome):
        """
            Add another chromossome to population

            @author     Thiago F Pappacena
            @param      object      chromossome     The Chromossome object to be inserted in population
            @return     void
        """
        self.chromossomes.append( chromossome )
    # end :: addChromossome


    @classmethod
    def getRandomPopulation(cls, size, genes):
        """
            Generates a random population of chromossomes

            @author     Thiago F Pappacena
            @param      integer     size        The number of individuals of population
            @param      tuple       genes       A tuple of gene CLASSES for each chromossome (like (BooleanGene, IntegerGene, IntegerGene) )
            @return     object      A Population of chromossomes
        """
        chromos = [ Chromossome(tuple((i.getRandomInstance() for i in genes))) for x in xrange(0, size) ]
        return Population( chromos )
    # end :: getRandomPopulation

    def evalFitness(self, fitnessFunction, force = False):
        """
            Evaluate chromossome's fitness

            @author     Thiago F Pappacena
            @param      object  fitnessFunction     The fitness function
            @param      boolean force               Eval even if the fitness is already set?
        """
        if not force:
            for c in self.chromossomes:
                if c.getFitness() is None:
                    c.setFitness( fitnessFunction.evaluate(c) )
        else:
            for c in self.chromossomes:
                c.setFitness( fitnessFunction.evaluate(c) )
    # end :: evalFitness


    def sort(self, fitnessFunction):
        """
            Sort the population in ascending order of adaptation of fitness

            @author     Thiago F Pappacena
            @param      object  fitnessFunction     The fitness function to evaluate each chromossome
            @return     void
        """
        self.evalFitness(fitnessFunction)

        def compare(c1, c2):
            c1f = c1.getFitness()
            c2f = c2.getFitness()
            if c1f == c2f:
                return 0
            return c1f > c2f and -1 or 1
        
        self.chromossomes.sort(compare)
    # end :: sort


    def __len__(self):
        """
            Returns the size of population

            @author     Thiago F Pappacena
            @param      void        void
            @return     integer     The population length ( len(self.chromossomes) )
        """
        return len(self.chromossomes)
    # end :: __len__

    
    def __add__(self, population):
        """
            Build a new population, joining the individual of both to a new Population object

            @author     Thiago F Pappacena
            @param      object  population  The other population object
            @return     object  population  The new population object
        """
        return Population(self.chromossomes + population.chromossomes)
    # end :: __add__


    def __iter__(self):
        """
            The iteration throught individuals in population

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The population iterable
        """
        return self.chromossomes.__iter__()
    # end :: __iter__


    def __repr__(self):
        """
            Returns the representation of the population

            @author     Thiago F Pappacena
            @param      void        void
            @return     string      The class representation
        """
        return 'Population(%s)' % str(self.chromossomes)
    # end :: __repr__
