class IterationInfo(object):
    """
        An object to hold informations about
        an training cycle iteration

        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build the IterationInfo object

            @author     Thiago F Pappacena
        """
        self.iterationNumber = 0
        self.error = 0
        self.errorDelta = 0
        self.net = None
        self.validationSetError = 0
    # end :: __init__


    #########################
    ## GETTERS AND SETTERS ##
    #########################

    def getIterationNumber(self):
        return self.iterationNumber
    def getError(self):
        return self.error
    def getErrorDelta(self):
        return self.errorDelta
    def getNetwork(self):
        return self.net
    def getValidationSetError(self):
        return self.validationSetError

    def setIterationNumber(self, iterationNumber):
        self.setIterationNumber = iterationNumber
    def setError(self, error):
        self.error = error
    def setErrorDelta(self, errorDelta):
        self.errorDelta = errorDelta
    def setNetwork(self, network):
        self.net = network
    def setValidationSetError(self, error):
        self.validationSetError = error

    ################################
    ## END :: GETTERS AND SETTERS ##
    ################################


    def adjustErrorDelta(self, newError):
        """
            Set a new error delta based in the past iteration error

            @author     Thiago F Pappacena
            @param      float   newError    The error in this iteration
            @return     void
        """
        self.errorDelta = self.error - newError
    # end :: adjustErrorDelta


    def increaseIterationNumber(self):
        """
            Increate the iteration number

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        self.iterationNumber += 1
    # end :: increaseIterationNumber

# end :: IterationInfo
