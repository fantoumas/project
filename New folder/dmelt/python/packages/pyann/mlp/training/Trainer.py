class Trainer(object):
    """
        (abstract) A class to define what should a 
        <something>Trainer object implement

        @author     Thiago F Pappacena
    """

    def __init__(self, network = None, monitor = None):
        """
            Trainer builder

            @author     Thiago F Pappacena
            @param      object  network     The network to be trained
            @param      object  monitor     The monitor for this Trainer
            @param      void    void
        """
        self.net = network
        self.monitor = monitor
        if self.monitor:
            self.monitor.setTrainer(self)
        self.stopConditions = []
        self.stopConditionsJoiner = None
    # end :: __init__


    def setNetwork(self, net):
        """
            Defines the network being trained

            @author     Thiago F Pappacena
            @param      object  net     The network
            @return     void
        """
        self.net = net
    # end :: setNetwork


    def getNetwork(self):
        """
            Returns the network being trained

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The MLP Network
        """
        return self.net
    # end :: getNetwork


    def getMonitor(self):
        """
            Get the monitor

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The Monitor object
        """
        return self.monitor
    # end :: getMonitor


    def setMonitor(self, monitor):
        """
            Defines the Trainer monitor

            @author     Thiago F Pappacena
            @param      object      monitor     The Monitor object
            @return     void
        """
        self.monitor = monitor
        if self.monitor.getTrainer() is not self:
            self.monitor.setTrainer(self)
    # end :: setMonitor


    def setStopConditions(self, conditions, joiner = 'or'):
        """
            Defines the set of stop conditions

            @author     Thiago F Pappacena
            @param      tuple   conditions  The set of StopCondition objects
            @param      string  joiner      The joiner for conditions ['or'|'and']
            @return     void
        """
        self.stopConditions = conditions
        self.stopConditionsJoiner = joiner.strip().lower() == 'and' and 'and' or 'or'
    # end :: setStopConditions


    def getStopConditions(self):
        """
            Returns the StopConditions for this training
            
            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The list of StopConditions
        """
        return self.stopConditions
    # end :: getStopConditions


    def getStopConditionsJoiner(self):
        """
            Returns the StopCondition joiner for this training

            @author     Thiago F Pappacena
            @param      void    void
            @return     string  The join condition joiner
        """
        return self.stopConditionsJoiner
    # end :: getStopConditionsJoiner


    def mustStopTraining(self, iterationInfo):
        """
            Checks if the training cicles must stop

            @author     Thiago F Pappacena
            @param      object  iterationInfo   Information about this training iteration
            @return     boolean     True if the train must stop. False otherwise
        """
        if self.stopConditionsJoiner == 'or':
            for s in self.stopConditions:
                if s.mustStop(iterationInfo):
                    return True
            return False
        else:
            for s in self.stopConditions:
                if not s.mustStop(iterationInfo):
                    return False
            return True
    # end :: mustStopTraining

    
    def train(self, patterns):
        """
            (abstract) Train the network given a list of Pattern objects

            This method must implement a looping that, in each iteration,
            must build a IterationInfo object and check the return of
            self.mustStopTrainint(iterationInfo). If this method returns
            True, the training cycle must stop and return a IterationInfo
            object to caller.

            @author     Thiago F Pappacena
            @param      list    patterns    The list of Patterns object
            @return     object  A IterationInfo object
        """
        raise NotImplementedException('train method must be implemented in subclasses of Trainer object')
    # end :: train

# end :: Trainer
