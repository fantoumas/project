class FitnessFunction(object):
    """
        Abstract class that defines the interface for a Fitness Function implementation

        @abstract
        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build the Fitness Function

            @author     Thiago F Pappacena
            @param      void        void
        """
        pass
    # end :: __init__


    def evaluate(self, chromossome):
        """
            Evaluate a chromossome and returns how adaptated to objective it is

            @abstract
            @author     Thiago F Pappacena
            @param      object      chromossome     The Chromossome to be evaluated
            @return     float       A floating poing number between 0 and 1
        """
        raise NotImplementedError('You must implement you own evaluation of Fitness Function')
    # end :: evaluate
