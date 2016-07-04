class GeneticPopulationModifier(object):
    """
        An abstract class to define the interfaces for a genetic population modifier

        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build the genetic operator

            @author     Thiago F Pappacena
            @param      void    void
        """
        pass
    # end :: __init__


    def modify(self, population):
        """
            Execute the modifier in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        raise NotImplementedError('You must implement the modify() method in GeneticPopulationModifier subclasses')
    # end :: modify

# end :: GeneticPopulationModifier
