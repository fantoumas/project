from pygenalg import *
from pygenalg.gene import *
from pygenalg.operator import *
from pygenalg.modifier import *
from pygenalg.choose import *
from pygenalg.planet import *
from pygenalg.planet.operator import *


# Fitness function: find the best chromossome that has more Trues before the last gene
class MyFit(FitnessFunction):
    def __init__(self):
        FitnessFunction.__init__(self)

    def evaluate(self, chromossome):
        genes = chromossome.getGenes()
        bestSolution = float(len(genes))
        fit = float(len([i for i in genes if i.getValue()]))

        return fit / bestSolution
    # end :: evaluate
# end :: MyFit


genotype    = tuple( [BooleanGene for i in xrange(0,100)] )
population  = Population.getRandomPopulation(10, genotype)
fitnessFunc = MyFit()

spcross     = SimpleCrossover(len(genotype) / 2.0, rate = 0.9)
eliteKeep   = ElitistKeeper(rate = 0.3)
oldKeep     = PopulationKeeper(rate = 0.2, chooser = RandomChooser())
migration   = MigrationCopy(['localhost:1777'], probability = 0.05, individuals = 1)

# pre and post modifiers
sortPopulation  = PopulationSorter(fitnessFunc)
saveBest        = BestChromossomeSaver(save = 1)
restoreBest     = BestChromossomeRestorer( saveBest )
mutate          = Mutation(probability = 0.3)
truncate        = PopulationTruncateSize(maxSize = 10, chooser = SimpleRouletChooser())

env = Environment(  population, 
                    fitnessFunc, 
                    preModifiers = (saveBest, sortPopulation),
                    operators = (migration, spcross, eliteKeep, oldKeep), 
                    postModifiers = (mutate, sortPopulation, truncate, restoreBest) )



continent = Continent('north', env, port = 1778, host = 'localhost')
continent.startServer()
