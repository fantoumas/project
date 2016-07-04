from pygenalg import Chromossome, Population, Environment
from pygenalg.operator import MultiPointCrossover, ArithmeticAverageCrossover, ElitistKeeper, PopulationKeeper
from pygenalg.modifier import DisasterCauser, Mutation, BiasedCreepMutation, BestChromossomeSaver, BestChromossomeRestorer, PopulationSorter, PopulationTruncateSize
from pygenalg.choose   import RandomChooser, SimpleRouletChooser
from pyann.mlp.training import Trainer, IterationInfo
from pyann.mlp.training.genetic import WeightGene, GeneticTrainerFitness
from pyann.mlp import Network
import fpconst
import random


class GeneticTrainer(Trainer):

    def __init__(self,  network = None, 
                        monitor = None, 
                        populationSize = 100, 
                        preModifiers = [], 
                        operators = [], 
                        postModifiers = []):
        """
            Build a basic genetic trainer

            @author     Thiago F Pappacena
            @param      object      network         The network to be trained
            @param      object      monitor         The monitor object
        """
        super(GeneticTrainer, self).__init__(network, monitor)
        self.populationSize = populationSize
        self.fitnessFunc = GeneticTrainerFitness(netArch = self.net.getDimension())

        if not preModifiers and not operators and not postModifiers:
            # if nothing is given, build a default set of
            # pre-modifiers, post-modifiers and operators

            mpcross     = MultiPointCrossover(points = 2, rate = 0.8, chooser = SimpleRouletChooser())
            avgcross    = ArithmeticAverageCrossover(rate = 0.2)
            eliteKeep   = ElitistKeeper(rate = 0.2)
            oldKeep     = PopulationKeeper(rate = 0.1, chooser = RandomChooser())

            # pre and post modifiers
            sortPopulation  = PopulationSorter(self.fitnessFunc)
            saveBest        = BestChromossomeSaver(save = 1)
            restoreBest     = BestChromossomeRestorer( saveBest )
            mutate          = Mutation(probability = 0.01)
            bcreepmutate    = BiasedCreepMutation(probability = 0.05, percentAdjust = 0.8)
            truncate        = PopulationTruncateSize(maxSize = self.populationSize, chooser = SimpleRouletChooser())

            self.preModifiers = (sortPopulation, saveBest)
            self.operators = (avgcross, mpcross, eliteKeep, oldKeep)
            self.postModifiers = (sortPopulation, bcreepmutate, mutate, sortPopulation, truncate, restoreBest)
        else:
            self.preModifiers = preModifiers
            self.operators = operators
            self.postModifiers = postModifiers

        self.env = None
    # end :: __init__


    def setPreModifiers(self, preModifiers):
        self.preModifiers  = preModifiers

    def setPostModifiers(self, postModifiers):
        self.postModifiers = postModifiers

    def getPostModifiers(self):
        return self.postModifiers

    def getPreModifiers(self):
        return self.preModifiers


    def train(self, patterns):
        """
            Train the net using this patterns for validation

            @author     Thiago F Pappacena
            @param      list    patterns    The list of patterns objects
            @return     object  The last IterationInfo object
        """
        self.fitnessFunc.setPatterns(patterns)
        planifiedNet = self.net.planify()
        netArch = self.net.getDimension()

        chromossomes = []
        for i in range(1, self.populationSize):
            #net = Network.fromDimension(netArch)
            net = self.net.copyStructure()
            newChromo = Chromossome(tuple(WeightGene(value) for value in net.planify()))
            chromossomes.append(newChromo)

        chromossomes += [ Chromossome(tuple(WeightGene(i) for i in planifiedNet)) ]

        population = Population(chromossomes)

        self.env = Environment( population      = population, 
                                fitFunction     = self.fitnessFunc,
                                preModifiers    = self.preModifiers,
                                operators       = self.operators,
                                postModifiers   = self.postModifiers )


        iterInfo = IterationInfo()
        iterInfo.setIterationNumber(0)
        iterInfo.setError(fpconst.PosInf)
        iterInfo.setErrorDelta(0)
        iterInfo.setNetwork(self.net)

        oldError = fpconst.PosInf
        while not self.mustStopTraining(iterInfo):
            self.env.doEvolution()                  # Do Pearl Jam
            best = self.env.getMostAdapted()        # Get the best chromossome in environment
            newError = - best.getFitness() # Get it's fitness

            if newError != oldError:                # If error changed, set the neural network weights
                self.net.setPlanifiedWeightMatrix( tuple(i.getValue() for i in best.getGenes()) )

            iterInfo.adjustErrorDelta(newError)
            iterInfo.setError(newError)
            iterInfo.increaseIterationNumber()
            iterInfo.setValidationSetError(fpconst.NegInf)

            if self.monitor:
                self.monitor.monitore( iterInfo )
        # end :: while

        return iterInfo
    # end :: train

# end :: GeneticTrainer
