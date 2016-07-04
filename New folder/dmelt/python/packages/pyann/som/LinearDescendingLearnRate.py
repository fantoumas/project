from pyann.som import LearnRate

class LinearDescendingLearnRate(LearnRate):
    """
        class for SOM learner that linearly descend the learning rate

        @author     Thiago F Pappacena
        @abstract
    """


    def __init__(self, initialLearnRate, reduce = 0, onEpoch = 0, minimumLearnRate = 0.1):
        """
            Init the object

            @author     Thiago F Pappacena
            @param      float   initialLearnRate        The initial learning rate
            @param      float   reduce                  How mutch the learning rate must be reduced (in percentage of the last learning rate)
            @param      float   onEpoch                 In which epoch the learning rate must be reduced
            @param      float   minimumLearnRate        The minimum learn rate to be used
        """
        LearnRate.__init__(self, initialLearnRate)
        self.reduce = reduce
        self.onEpoch = onEpoch
        self.minimumLearnRate = minimumLearnRate
    # end :: __init__


    def getActualLearnRate(self, epoch):
        """
            Returns the actual learn rate for the epoch. This may return the learn rate in function of training epoch

            @author     Thiago F Pappacena
            @param      integer     epoch       The epoch number
            @return     float       The actual learn rate to be used in network training
        """
        if self.onEpoch != 0 and self.reduce != 0:
            learnRate = (self.initialLearnRate - (self.initialLearnRate * self.reduce * int((epoch / self.onEpoch))))
            return max(learnRate, self.minimumLearnRate)
        else:
            return self.initialLearnRate
    # end :: getActualLearnRate
