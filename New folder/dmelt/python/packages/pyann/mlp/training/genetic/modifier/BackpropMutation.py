from pygenalg.modifier import Mutation
from pyann.mlp.training.backprop import BackpropagationTrainer
from pyann.mlp.training import MaxIterationsStopCondition
from pyann.mlp import Network
import random

class BackpropMutation(Mutation):
    """
        A backpropagation mutation object

        @author     Thiago F Pappacena
    """

    def __init__(self,  netArch,
                        maxIterations,
                        patterns,
                        probability = 0.01, 
                        monitor = None, 
                        learningRate = 0.5, 
                        momentum = 0.0, 
                        batch = False,
                        randomize = True ):
        """
            Build the Backpropagation mutator

            @author     Thiago F Pappacena
            @param      tuple   netArch         The network archicteture (returned by Network.getDimension method)
            @param      integer maxIterations   The max number of iterations
            @param      list    patterns        The list of patterns to use in training
            @param      float   probability     The probability of operating
            @see        pyann.mlp.trainer.backprop.BackpropagationTrainer
        """
        super(BackpropMutation, self).__init__(probability = probability)
        self.patterns = patterns
        self.maxIterations = maxIterations
        self.stopMaxIter = MaxIterationsStopCondition(self.maxIterations)

        self.trainer = BackpropagationTrainer(  monitor = monitor, 
                                                learningRate = learningRate,
                                                momentum = momentum,
                                                batch = batch,
                                                randomize = randomize )
        self.trainer.setStopConditions( (self.stopMaxIter, ) )
        self.netArch = netArch
    # end :: __init__


    def modify(self, population):
        """
            Apply the backpropagation mutation in someone in population

            @author     Thiago  F Pappacena
            @param      object  population  The population object
            @return     void
        """
        if random.random() <= self.probability:
            self.stopMaxIter.setIterations( random.randrange(1, self.maxIterations) )

            chromo = random.choice(population.getChromossomes())
            genes = chromo.getGenes()
            weights = tuple(x.getValue() for x in genes)

            # rebuild the net and train
            net = Network.fromPlanifiedWeights(self.netArch, weights)
            self.trainer.setNetwork(net)
            self.trainer.train(self.patterns)
            self.netArch = net.getDimension()

            # copy values to genes
            for gene, weight in zip(genes, net.planify()):
                gene.setValue(weight)
            chromo.setFitness(None)
    # end :: modify

# end :: BackpropMutation
