from pyann.mlp.training import StopCondition

class MinErrorStopCondition(StopCondition):
    """
        Stop training when the global error reaches
        a given limit

        @author     Thiago F Pappacena
    """

    def __init__(self, minError):
        """
            Build a stop condition

            @author     Thiago F Pappacena
        """
        super(MinErrorStopCondition, self).__init__()
        self.minError = minError
    # end :: __init__


    def mustStop(self, iterationInfo):
        """
            Checks if the iteration reached the min error

            @author     Thiago F Pappacena
            @param      object  iterationInfo   Informations about the training cycle
            @return     boolean     True if the cycle satisfies the stop condition. False otherwise
        """
        return iterationInfo.getError() <= self.minError
    # end :: mustStop

# end :: MinErrorStopCondition
