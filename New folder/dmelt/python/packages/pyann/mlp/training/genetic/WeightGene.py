from pygenalg.gene import FloatGene
import fpconst


class WeightGene(FloatGene):
    """
        A special FloatGene that hold values between -20 and +20
        
        @author     Thiago F Pappacena
    """

    MIN_VALUE = -100.0
    MAX_VALUE = 100.0

    def __init__(self, value, minValue = None, maxValue = None):
        if minValue is None:
            minValue = self.MIN_VALUE
        if maxValue is None:
            maxValue = self.MAX_VALUE
        FloatGene.__init__(self, value, minValue = minValue, maxValue = maxValue)

    @classmethod
    def getRandomInstance(cls, minValue = None, maxValue = None):
        if minValue is None:
            minValue = cls.MIN_VALUE
        if maxValue is None:
            maxValue = cls.MAX_VALUE
        return FloatGene.getRandomInstance(minValue = minValue, maxValue = maxValue)

# end :: WeightGene

