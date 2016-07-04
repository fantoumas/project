from pygenalg.gene import NumericGene
import random

class IntegerGene(NumericGene):
    """
        A class represeting an integer gene, implementing the NumericGene class

        @author     Thiago F Pappacena
    """

    
    def __init__(self, value, minValue = 0, maxValue = 100):
        """
            Build an Integer gene

            @author     Thiago F Pappacen
            @param      integer     minValue        The minimum possible value for the instance
            @param      integer     maxValue        The maximum possible value for the instance
        """
        NumericGene.__init__(self, int(value), minValue, maxValue)
    # end :: __init__


    @classmethod
    def getRandomInstance(cls, minValue, maxValue):
        """
            Gets a IntegerGene with random value

            @author     Thiago F Pappacena
            @param      integer     minValue        The minimum possible value for the instance
            @param      integer     maxValue        The maximum possible value for the instance
            @return     object      A random beetween IntegerGene(minValue) and IntegerGene(maxValue)
        """
        return IntegerGene( random.randint(minValue, maxValue), minValue, maxValue )
    # end :: getRandomInstance


    def mutate(self):
        """
            Do a mutation in this gene, changing it's value

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        self.value = random.randint(self.min, self.max)
    # end :: mutate

# end :: IntegerGene
