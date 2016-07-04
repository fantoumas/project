class SOM(object):
    """
        Kohonen's Self-Organized Map implementation

        @author     Thiago F Pappacena
    """
    
    def __init__(self, map, neighborhood, learnRate):
        """
            Build a new Kohonen's SOM object

            @author     Thiago F Pappacena
            @param      object      map             The Map object, with all clusters
            @param      object      neighborhood    The Neighborhood object
            @param      object      learnRate       The LearnRate object
        """
        self.map = map
        self.neighborhood = neighborhood
        self.learnRate = learnRate
    # end :: __init__


    def train(self, dataset, cycles):
        for i in xrange(0, cycles):
            [self.__doAjust(input, i) for input in dataset]
    # end :: train

    def doAjust(self, input, cycle):
        self.__doAjust(input, cycle)
    # end :: doAjust


    def __doAjust(self, input, cycle):
        winner = self.__selectWinner(input)
        neighbors = self.neighborhood.getNeighbors( self.map.getClusterPosition(winner), cycle )

        winner.ajustWeights(input, self.learnRate.getActualLearnRate(cycle))

        for distance, nodes in neighbors.items():
            [x.ajustWeights(input, self.learnRate.getActualLearnRate(cycle)) for x in nodes]
    # end :: __doAjust


    def __selectWinner(self, input):
        return self.map.selectWinner(input)
    # end :: __selectWinner


    def classify(self, input):
        return self.__selectWinner(input)
    # end :: classify

