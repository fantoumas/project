import random

class Chromossome(object):
    """
        A class representing a chromossome (a collection of genes)

        @author     Thiago F Pappacena
    """


    def __init__(self, genes = ()):
        """
            Build the Chromossome based on genes

            @author     Thiago F Pappacena
            @param      tuple       genes       The tuple of genes
        """
        self.genes = genes
        self.fitness = None
    # end :: __init__


    def getGenes(self):
        """
            Returns the genes of this chromossome

            @author     Thiago F Pappacena
            @param      void        void
            @return     tuple       The tuple of genes
        """
        return self.genes
    # end :: getGenes


    @classmethod
    def getRandomInstance(cls, genotypes):
        """
            Build a random chromossome based on the genotypes tuple.

            Examples:   To build a random chromossome with the genotype (Boolean, Boolean, Integer, Decimal),
                        use a list of respectives Gene objects. In other words, you will do a call like this:
                            x = Chromossome.getRandomInstance( (BooleanGene, BooleanGene, IntegerGene, DecimalGene) )

            @author     Thiago F Pappacena
            @param      list        genotypes       The genotypes list
            @return     object      A Chromossome object
        """
        genes = tuple([x.getRandomInstance() for x in genotypes])
        return Chromossome(genes)
    # end :: getRandomInstance


    def mutate(self):
        """
            Generates a mutation in a random gene in this chromossome

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        random.choice(self.genes).mutate()
        self.fitness = None
    # end :: mutate


    def getFitness(self):
        """
            Returns the actual fitness for this chromossome

            @author     Thiago F Pappacena
            @param      void    void
            @return     float   The actual fitness
        """
        return self.fitness
    # end :: getFitness


    def setFitness(self, fitness):
        """
            Defines the actual fitness for this chromossome

            @author     Thiago F Pappacena
            @param      float   fitness     The fitness
            @return     void
        """
        self.fitness = fitness
    # end :: setFitness

    '''
    def __repr__(self):
        """
            The representation of a chromossome

            @author     Thiago F pappacena
            @param      void        void
            @return     string      The string representation
        """
        return '<Chromossome %s>' % str(self.genes)
    '''

# end :: Chromossome
