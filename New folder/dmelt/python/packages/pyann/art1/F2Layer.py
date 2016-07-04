class F2Layer(object):
    
    def __init__(self, l, clusters):
        """
            Build an F2 layer

            @author     Thiago F Pappacena
            @param      float       l           The L (node's weights update) parameter
            @param      list        clusters    The list of clusters in this layer
        """
        self.clusters = clusters
        self.l = l
    # end :: __init__


    def selectWinner(self, f1output):
        raise NotImplementedError('')
    # end :: selectWinner


    def clear(self):
        [node.setReseted(False) for node in self.clusters]
    # end :: clear
