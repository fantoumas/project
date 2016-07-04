from pyann.som import Neighborhood, SOMClusterPositionOutOfBoundsException

class RectangularNeighborhood(Neighborhood):
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
        """
        Neighborhood.__init__(self, map, size, reduce, onEpoch)
    # end :: __init__


    def getNeighbors(self, position, epoch = -1):
        """
        
            @author     Thiago F Pappacena
            @abstract
            @param      tuple   position    The position of the cluster in map
            @param      integer epoch       The training epoch (to be used when needed to reduce neighborhood in function of epoches)
            @return     dict    A dict where the index is the distance and the values are the clusters, like {'1': [cluster1, cluster3, cluster5], '2': [cluster2, cluster4, cluster6, cluster8], ... }
        """
        if self.onEpoch != 0 and self.reduce != 0:
            actualNeighbohoodSize = self.size - (self.reduce * int((epoch / self.onEpoch)))
        else:
            actualNeighbohoodSize = self.size

        if len(position) not in [1,2]:
            raise NotImplementedError('Retangular %d neighborhood is not implemented yet' % len(position))

        ret = {}
        if len(position) == 1:
            for x in xrange(1, actualNeighbohoodSize):
                try:
                    ret[x].append(self.map.getCluster( position - x ))
                except Exception, e:
                    pass
                try:
                    ret[x].append(self.map.getCluster( position + x ))
                except Exception, e:
                    pass
        return ret
    
        ret = {}
        for dist in xrange(1, actualNeighbohoodSize):
            ret[dist] = []
            try:
                ret[dist].append( self.map.getCluster( (position[0] - 1, position[1]) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

            try:
                ret[dist].append( self.map.getCluster( (position[0] + 1, position[1]) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

            try:
                ret[dist].append( self.map.getCluster( (position[0], position[1] - 1) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

            try:
                ret[dist].append( self.map.getCluster( (position[0], position[1] + 1) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

            try:
                ret[dist].append( self.map.getCluster( (position[0] - 1, position[1] - 1) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

            try:
                ret[dist].append( self.map.getCluster( (position[0] - 1, position[1] + 1) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass
 
            try:
                ret[dist].append( self.map.getCluster( (position[0] + 1, position[1] - 1) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

            try:
                ret[dist].append( self.map.getCluster( (position[0] + 1, position[1] + 1) ) )
            except SOMClusterPositionOutOfBoundsException, e:
                pass

        return ret
    # end :: getNeighbors


# end :: Neighborhood
