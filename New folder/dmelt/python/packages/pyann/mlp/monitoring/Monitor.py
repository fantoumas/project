class Monitor(object):
    """
        (abstract) A Trainer monitor object

        @author     Thiago F Pappacena
    """

    def __init__(self, trainer = None):
        """
            Build a trainer monitor

            @author     Thiago F Pappacena
            @param      object  trainer     The Trainer object to be monitored
        """
        self.trainer = trainer
    # end :: __init__


    def monitore(self, iteration):
        """
            (abstract) Monitore this iteration

            @author     Thiago F Pappacena
            @param      object  iteration   The IterInfo object
            @return     void
        """
        raise NotImplementedError('This method must be implemented in one' + \
                                  'of the Monitor subclasses')
    # end :: monitore


    def setTrainer(self, trainer):
        """
            Defines the trainer

            @author     Thiago F Pappacena
            @param      object  trainer     The trainer object
            @return     void
        """
        self.trainer = trainer
        if self.trainer.getMonitor() is not self:
            self.trainer.setMonitor(self)
    # end :: setTrainer


    def getTrainer(self):
        """
            Retursn the trainer object

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The trainer object
        """
        return self.trainer
    # end :: getTrainer

# end :: Monitor
