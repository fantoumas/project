from pygenalg.gene import NumericGene
import random

class FloatGene(NumericGene):
    """
        A class represeting a floating point number gene, implementing the Gene class

        @author     Thiago F Pappacena
    """

    
    def __init__(self, value, minValue = 0.0, maxValue = 100.0):
        """
            Build a Float gene

            @author     Thiago F Pappacen
            @param      float       minValue        The minimum possible value for the instance
            @param      float       maxValue        The maximum possible value for the instance
        """
        NumericGene.__init__(self, value, minValue, maxValue)
    # end :: __init__


    @classmethod
    def getRandomInstance(cls, minValue = 0.0, maxValue = 100.0):
        """
            Gets a FloatGene with random value

            @author     Thiago F Pappacena
            @param      float       minValue        The minimum possible value for the instance
            @param      float       maxValue        The maximum possible value for the instance
            @return     object      A random beetween FloatGene(minValue) and FloatGene(maxValue)
        """
        value = (random.random() * (maxValue - minValue) + minValue)
        return FloatGene( value, minValue, maxValue )
    # end :: getRandomInstance


    def mutate(self):
        """
            Do a mutation in this gene, changing it's value

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        self.value = (random.random() * (self.max - self.min) + self.min)
    # end :: mutate

# end :: FloatGene
