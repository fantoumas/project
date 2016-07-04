from pygenalg.planet import getContinent
import time

south = getContinent('localhost', 1777)
north = getContinent('localhost', 1778)
north.startEvolution()
south.startEvolution()

while True:
    time.sleep(1)
    bestSouth = south.getBestFit()
    bestNorth = north.getBestFit()
    print 'bests: south(%s) | north(%s)' % (bestNorth.getFitness(), bestSouth.getFitness())
    if bestSouth.getFitness() >= 1 or bestNorth.getFitness() >= 1:
        south.stopEvolution()
        north.stopEvolution()
        break

print '*** Found the solution! ***'
print '\n\n\n'
print 'South: %s' % (bestSouth.getGenes(), )
print '\n\n'
print 'North: %s' % (bestNorth.getGenes(), )
