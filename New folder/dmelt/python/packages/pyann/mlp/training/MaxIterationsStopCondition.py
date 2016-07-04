from pyann.mlp.training import StopCondition

class MaxIterationsStopCondition(StopCondition):
    """
         Stop training after a given number of iterations

        @author     Thiago F Pappacena
    """

    def __init__(self, iterations):
        """
            Build a stop condition

            @author     Thiago F Pappacena
        """
        super(MaxIterationsStopCondition, self).__init__()
        self.iterations = iterations
    # end :: __init__


    def setIterations(self, iterations):
        """
            Redefine the number of max iterations

            @author     Thiago F Pappacena
            @param      integer iterations  The new max iterations number
            @return     void
        """
        self.iterations = iterations
    # end :: setIterations


    def mustStop(self, iterationInfo):
        """
            Checks if the iteration if the max number

            @author     Thiago F Pappacena
            @param      object  iterationInfo   Informations about the training cycle
            @return     boolean     True if the cycle satisfies the stop condition. False otherwise
        """
        return iterationInfo.getIterationNumber() >= self.iterations
    # end :: mustStop

# end :: MaxIterationsStopCondition
