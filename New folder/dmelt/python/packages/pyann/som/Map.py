from pyann.som import Cluster, SOMClusterPositionOutOfBoundsException

class Map(object):
    
    def __init__(self, clusters):
        """
            Build the map

            @author     Thiago F Pappacena
            @param      list    Clusters        The list of tuples of clusters, like [ (Cluster1, Cluster2, Cluster3), (Cluster4, Cluster5, Cluster6) ]
        """
        self.clusters = clusters
        self.hashMap = {}
        self.buildDictMapping()
    # end :: __init__


    def buildDictMapping(self, clusters = None, deep = ()):
        if clusters is None:
            clusters = self.clusters

        if isinstance(clusters, Cluster):
            return deep

        if isinstance(clusters[0], Cluster):    # last level! Uhuu
            for i in xrange(0, len(clusters)):
                position = tuple([x for x in deep] + [i])
                self.hashMap[position] = clusters[i]
            return self.hashMap

        # not the last level... try next level
        for i in xrange(0, len(clusters)):
            self.buildDictMapping(clusters[i], tuple([x for x in deep] + [i]))

    def getCluster(self, position):
        """
            Returns the cluster at a defined position

            @author     Thiago F Pappacena
            @param      tuple   position        The coordinates of the desired cluster in map, like (0,3)
            @return     object  The cluster at the given position
        """
        if not self.hashMap.has_key(position):
            raise SOMClusterPositionOutOfBoundsException('%s is out of bounds' % str(position))
        return self.hashMap[ position ]
        #pos = '[%s]' % (']['.join(positions))
        #return eval('self.clusters%s' % pos)
    # end :: getCluster


    def getClusterPosition(self, cluster):
        for position, node in self.hashMap.items():
            if cluster == node:
                return position
    # end :: getClusterPosition


    def selectWinner(self, input, clusters = None):
        """
            Select a winner cluster in the map

            @author     Thiago F Pappacena
            @param      tuple       input       The input vector
            @param      mixed       clusters    The list of clusters where to search the winner one
            @return     Cluster     The winner of competition
        """
        #if clusters is None:
        #    clusters = self.clusters

        #if type(clusters) == type([]) and ( type(clusters[0]) == type([]) or type(clusters[0]) == type(()) ):  # if it's multidimensional
        #    
        #    # reducing dimensions
        #    lines = []
        #    for i in clusters:
        #        lines = lines + list(i)

        #    # try again
        #    return self.selectWinner(input, lines)

        #elif type(clusters) == type(()) or type(clusters) == type([]):        # if it's just one dimension,

        #    maxInput = None
        #    selectedCluster = None
        #    clusterInput = 0

        #    for cluster in clusters:                            # for each cluster
        #        clusterInput = cluster.getTotalInput(input)     # get the cluster's total input
        #        if maxInput is None or clusterInput > maxInput: # if it's bigger than the actual,
        #            selectedCluster = cluster                   # we found a new candidate
        #            maxInput = clusterInput
        #    # end :: for

        #    return selectedCluster      # return the cluster and it's input
        # end :: if

        #raise SOMTypeMismatchException('%s is not a valid type to be used in map' % type(clusters))


        minInput = None
        selectedCluster = None
        clusterInput = None
        for position, cluster in self.hashMap.items():
            clusterInput = cluster.getTotalInput(input)
            #print 'Input %s ao clusterID#%s -> %s' % (input, cluster.getID(), clusterInput)
            if minInput is None or clusterInput < minInput:
                selectedCluster = cluster
                minInput = clusterInput

        return selectedCluster

    # end :: selectWinner


