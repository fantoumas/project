from pygenalg.operator import GeneticOperator
from pygenalg.choose import RandomChooser
from pygenalg import Population
import random
import Pyro.core

class MigrationCopy(GeneticOperator):
    """
        Migration between Continents operator, keeping the remote individuals

        @author     Thiago F Pappacena
    """
    
    def __init__(self, continentsServers, individuals = 2, probability = 0.1, chooser = RandomChooser()):
        """
            Build the migration copy operator

            @author     Thiago F Pappacena
            @param      list    continentsServers   The list of continents servers
                                                    This list must contein strings in format
                                                        'host:port', like '127.0.0.1:777'
            @param      integer individuals         The number of individuals to copy migrate
            @param      float   probability         The probability of running this operator
            @param      object  chooser             The method of choosing individuals from
                                                        remote population
        """
        self.continentsServers = continentsServers
        self.probability = probability
        self.individuals = individuals
        self.chooser = chooser
    # end :: __init__


    def operate(self, population):
        """
            Run the migration

            @author     Thiago F Pappacena
            @param      object  population  The actual local population
            @return     object  A new population to be used in evolution
        """
        if random.random() <= self.probability:
            proxy = self.__getServer()
            remotePopulation = proxy.getPopulation()

            totalMigrators = self.individuals
            if len(remotePopulation):
                return self.chooser.choose(remotePopulation, totalMigrators)
        return Population([])
    # end :: operate


    def __getServer(self):
        """
            Get a proxy to one of the avaiable servers

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The proxy to one of the servers
        """
        server = random.choice(self.continentsServers)
        return Pyro.core.getAttrProxyForURI('PYROLOC://%s/continent' % server)
    # end :: chooseServer

# end :: Migrate
