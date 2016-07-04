from pygenalg.gene import Gene
import random

class NumericGene(Gene):
    """
        A class represeting a numeric gene, implementing the Gene class

        @author     Thiago F Pappacena
    """

    
    def __init__(self, value, minValue, maxValue):
        """
            Build an numeric gene

            @author     Thiago F Pappacen
            @param      integer     minValue        The minimum possible value for the instance
            @param      integer     maxValue        The maximum possible value for the instance
        """
        Gene.__init__(self, value)
        self.min = minValue
        self.max = maxValue
    # end :: __init__


    def getMaxValue(self):
        """
            Returns the max value for this gene

            @author     Thiago F Pappacena
            @param      void    void
            @return     mixed   The max number
        """
        return self.max
    # end :: getMaxValue


    def getMinValue(self):
        """
            Returns the mix value for this gene

            @author     Thiago F Pappacena
            @param      void    void
            @return     mixed   The mix number
        """
        return self.min
    # end :: getMinValue


    @classmethod
    def getRandomInstance(cls, minValue, maxValue):
        """
            Gets a NumericGene with random value

            @author     Thiago F Pappacena
            @param      integer     minValue        The minimum possible value for the instance
            @param      integer     maxValue        The maximum possible value for the instance
            @return     object      A random beetween IntegerGene(minValue) and IntegerGene(maxValue)
        """
        raise NotImplementedError('You must implement this method in subclasses')
    # end :: getRandomInstance


    def mutate(self):
        """
            Do a mutation in this gene, changing it's value

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        raise NotImplementedError('You must re-implement this method in subclasses')
    # end :: mutate


    def copy(self):
        """
            Make a copy of a NumericGene

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      The NumericGene copy
        """
        return self.__class__(self.value, self.min, self.max)
    # end :: copy

# end :: NumericGene
