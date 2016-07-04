from pygenalg import Population

class Environment(object):
    """
        A genetic environemt

        @author     Thiago F Pappacena
    """
    
    def __init__(self, population, fitFunction, preModifiers = [], operators = [], postModifiers = []):
        """
            Build the environment
            
            @author     Thiago F Pappacena
            @param      object  population      The initial population
            @param      object  fitFunction     The fitness function to eval individuals
            @param      list    preOperators    The list of operators to apply before building next generations
            @param      list    operators       The genetic operators in to build next generations
            @param      list    operators       The genetic operators to apply after building next generation
        """
        self.initialPopulation = population
        self.actualPopulation = population
        self.fitFunction = fitFunction
        self.preModifiers = preModifiers
        self.operators = operators
        self.postModifiers = postModifiers
    # end :: __init__


    def doEvolution(self):
        """
            Do an evolution in actual population, returning the new Population

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      The new Population
        """
        if self.preModifiers:
            # Apply the pre-operators
            for op in self.preModifiers:
                op.modify(self.actualPopulation)

        # apply operators to actual population
        finalPopulation = Population([])
        for op in self.operators:
            finalPopulation += op.operate(self.actualPopulation)
        self.actualPopulation = finalPopulation

        if self.postModifiers:
            # apply the post-operators
            for op in self.postModifiers:
                op.modify(self.actualPopulation)

        return self.actualPopulation
    # end :: doEvolution


    def getMostAdapted(self):
        """
            Returns the most adapted individual in actual population

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The most adapted chromossome
        """
        self.actualPopulation.sort( self.fitFunction )
        return self.actualPopulation.getChromossomes()[0]
    # end :: getMostAdapted


    def getActualPopulation(self):
        """
            Returns the actual Population of environment

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      The Population object
        """
        return self.actualPopulation
    # end :: getActualPopulation


# end :: Environment
