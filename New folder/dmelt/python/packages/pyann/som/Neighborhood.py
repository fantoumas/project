class Neighborhood(object):
    """
        Abstract class to define the neighbohood of a cluster

        @author     Thiago F Pappacena
        @abstract
    """

    def __init__(self, map, size, reduce = 0, onEpoch = 0):
        """
            Neighborhood constructor

            @author     Thiago F Pappacena
            @param      object      map     The map object
            @param      integer     size    The neighborhood size
            @param      integer     reduce  How to reduce the neighborhood with epoches
            @param      integer     onEpoch Reduce the neighbohood $reduce unites every $onEpoch cycles
        """
        self.map = map
        self.size = size
        self.reduce = reduce
        self.onEpoch = onEpoch
    # end :: __init__


    def getNeighbors(self, position, epoch = -1):
        """
        
            @author     Thiago F Pappacena
            @abstract
            @param      tuple   position    The position of the cluster in map
            @param      integer epoch       The training epoch (to be used when needed to reduce neighborhood in function of epoches)
            @return     dict    A dict where the index is the distance and the values are the clusters, like {'1': [cluster1, cluster3, cluster5], '2': [cluster2, cluster4, cluster6, cluster8], ... }
        """
        raise NotImplementedError('getNeighbors')
    # end :: getNeighbors

# end :: Neighborhood
