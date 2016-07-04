class StopCondition(object):
    """
        (abstract)  A stop condition to a training

        @author     Thiago F Pappacena
    """

    def __init__(self):
        """
            Build a stop condition

            @author     Thiago F Pappacena
        """
        pass
    # end :: __init__


    def mustStop(self, iterationInfo):
        """
            (abstract) Checks if the iteration satisfies the stop condition

            @author     Thiago F Pappacena
            @param      object  iterationInfo   Informations about the training cycle
            @return     boolean     True if the cycle satisfies the stop condition. False otherwise
        """
        raise NotImplementedException('This method must be implemented in subclasses')
    # end :: mustStop

# end :: StopCondition
