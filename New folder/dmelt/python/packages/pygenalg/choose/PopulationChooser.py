class PopulationChooser(object):
    """
        Abstract class that defines the interface for genetic chromossomes choosers

        @abstract
        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build the Population Chooser

            @author     Thiago F Pappacena
        """
        pass
    # end :: __init__


    def choose(self, population, number):
        """
            Choose a number of chromossomes from the population

            @abstract
            @author     Thiago F Pappacena
            @param      integer     number          The number of choosen individuals
            @param      object      population      A Population object
            @return     object      Another population, only with choosen chromossomes
        """
        raise NotImplementedError('You must implement the choose method in subclasses of PopulationChooser')
    # end :: choose

# end :: PopulationChooser
