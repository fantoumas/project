class GeneticOperator(object):
    """
        An abstract class to define the interfaces for a genetic operator

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


    def operate(self, population):
        """
            Execute the genetic operation in a given population

            @author     Thiago F Pappacena
            @param      object      population      The Population
            @return     void
        """
        raise NotImplementedError('You must implement the operate() method in GeneticOperator subclasses')
    # end :: operate

# end :: GeneticOperator
