import Pyro.core
import threading

class Continent(Pyro.core.ObjBase):
    """
        A remote object to do parallel and distributed evolution

        @author     Thiago F Pappacena
    """

    def __init__(self, name, environment, port = 9666, host = 'localhost'):
        """
            Build the continent

            @author     Thiago F Pappacena
            @param      string  name            The continent name
            @param      object  environment     The env to put in this continent
        """
        Pyro.core.ObjBase.__init__(self)
        self.name = name
        self.environment = environment
        self.port = port
        self.host = host

        # Lock for critical region of self.environment
        self.evolvingThread = None
        self.envLock = threading.Lock()
    # end :: __init__


    def getPort(self): return self.port
    def getHost(self): return self.host
    def getName(self): return self.name


    def getEnvironment(self):
        """
            Returns the environment of this continent

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The Environment object
        """
        return self.environment
    # end :: getEnvironment


    def setEnvironment(self, env):
        """
            Defines the environment of this continent

            @author     Thiago F Pappacena
            @param      object  env     The new environment
            @return     void
        """
        self.environment = env
    # end :: setEnvironment


    def startEvolution(self):
        """
            Start evolving the environment

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
            @see        Continent.stopEvolving method
        """
        if self.evolvingThread is not None:
            raise ParallelException('Environment is already evolving!')
        self.evolvingThread = EvolutionThread(self.environment, self.envLock)
        self.evolvingThread.start()
    # end :: startEvolving


    def stopEvolution(self):
        """
            Stop evolving the environment

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        self.evolvingThread.stop()
        self.evolvingThread.join()
        self.evolvingThread = None
    # end :: stopEvolution


    def getPopulation(self):
        """
            Returns the actual population of continent

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The actual population of the continent
        """
        return self.environment.getActualPopulation()
    # end :: getPopulation


    def getBestFit(self):
        """
            Returns the most adapted chromossome in continent

            @author     Thiago F Pappacena
            @param      void    void
            @return     object  The most adapted chromossome
        """
        self.envLock.acquire()
        best = self.environment.getMostAdapted()
        self.envLock.release()
        return best
    # end :: getBestFit


    def startServer(self):
        """
            Start the pyro server

            @author     Thiago F Pappacena
            @param      void    void
            @return     void
        """
        Pyro.core.initServer(banner = 0)
        daemon = Pyro.core.Daemon(host = self.host, port = self.port)
        uri = daemon.connect(self, 'continent')
        daemon.requestLoop()
    # end :: startServer


# end :: Continent


class EvolutionThread(threading.Thread):
    """
        Helper class to evolve the environment in a separated thread

        @author     Thiago F Pappacena
    """
    
    def __init__(self, env, envLock):
        """
            Build the evolving thread

            @author     Thiago F Pappacena
            @param      object  env     The environment to run evolution
            @param      object  envLock The threading.Lock object to use
                                        when running in critical region
        """
        threading.Thread.__init__(self)
        self.env = env
        self.envLock = envLock
        self.running = False
    # end :: __init__


    def run(self):
        self.running = True
        while self.running:
            self.envLock.acquire()
            self.env.doEvolution()
            self.envLock.release()
    # end :: run
    

    def stop(self):
        self.running = False
    # end :: stop

# end :: EvolutionThread



class ParallelException(Exception):
    """
        Parallel evolving exception: launched when you
        try to evolve an already evolving environment

        @author     Thiago F Pappacena
    """
    pass
