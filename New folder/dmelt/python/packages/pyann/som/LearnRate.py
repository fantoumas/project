class LearnRate(object):
    """
        Abstract class for SOM learner

        @author     Thiago F Pappacena
        @abstract
    """


    def __init__(self, initialLearnRate):
        """
            Init the object

            @author     Thiago F Pappacena
        """
        self.initialLearnRate = initialLearnRate
    # end :: __init__


    def getActualLearnRate(self, epoch):
        """
            Returns the actual learn rate for the epoch. This may return the learn rate in function of training epoch

            @author     Thiago F Pappacena
            @param      integer     epoch       The epoch number
            @return     float       The actual learn rate to be used in network training
        """
        raise NotImplementedError('getActualLearnRate')
    # end :: getActualLearnRate
