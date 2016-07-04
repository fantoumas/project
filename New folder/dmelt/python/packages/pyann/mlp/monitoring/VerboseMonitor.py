from pyann.mlp.monitoring import Monitor

class VerboseMonitor(Monitor):
    """
        A Trainer monitor object

        @author     Thiago F Pappacena
    """

    def __init__(self, trainer = None, cycles = 1):
        """
            Build a trainer monitor

            @author     Thiago F Pappacena
            @param      object      trainer     The Trainer object to be monitored
            @param      integer     cycles      Print messages when iteration % cycles == 0
        """
        super(Monitor, self).__init__
        self.cycles = cycles
    # end :: __init__


    def monitore(self, iter):
        """
            Monitore this iteration

            @author     Thiago F Pappacena
            @param      object  iter    The IterInfo object
            @return     void
        """
        if iter.getIterationNumber() % self.cycles  == 0:
            print "Iteration: %d | Error**2 sum: %.10f | Validation Error**2 sum: %.10f" % (  iter.getIterationNumber(),
                                                                                        iter.getError(),
                                                                                        iter.getValidationSetError() )
    # end :: monitore

# end :: VerboseMonitor
