from pygenalg.gene import Gene
import random

class BooleanGene(Gene):
    """
        A class represeting a boolean gene, implementing the Gene class

        @author     Thiago F Pappacena
    """

    
    def __init__(self, value):
        """
            Build an Boolean gene

            @author     Thiago F Pappacen
            @param      boolean     value       The value of this gene
        """
        Gene.__init__(self, value)
    # end :: __init__


    @classmethod
    def getRandomInstance(cls):
        """
            Gets a BooleanGene with random value

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      A random beetween BooleanGene(True) and BooleanGene(False)
        """
        return BooleanGene( bool(random.randint(0,1)) )
    # end :: getRandomInstance


    def mutate(self):
        """
            Do a mutation in this gene, changing it's value

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        self.value = not self.value
    # end :: mutate

# end :: BooleanGene
