#!/usr/bin/env python

import pyann.som as som
import pyann.som.Cluster as Cluster
import random

def getRandVec(size = 5):
    return tuple([random.random() for x in xrange(0,size)])

lines = int(raw_input('Lines: '))
columns = int(raw_input('Columns: '))
neighborhood = int(raw_input('Neighborhood: '))
trainingCycles = int(raw_input('Training cycles: '))

clusterNumber = 0
clusters = []
for i in xrange(0,lines):
    clusters.append([])
    for j in xrange(0,columns):
        clusters[i].append(Cluster(getRandVec(), clusterNumber))
        clusterNumber += 1
        
"""
clusters = [    (Cluster(getRandVec(), 0), Cluster(getRandVec(), 1), Cluster(getRandVec(), 2), Cluster(getRandVec(), 3), som.Cluster(getRandVec(), 4)),
                (Cluster(getRandVec(), 5), Cluster(getRandVec(), 6), Cluster(getRandVec(), 7), Cluster(getRandVec(), 8), Cluster(getRandVec(), 9)),
                (Cluster(getRandVec(), 10), Cluster(getRandVec(), 11), Cluster(getRandVec(), 12), Cluster(getRandVec(), 13), som.Cluster(getRandVec(), 14)),
                (Cluster(getRandVec(), 15), Cluster(getRandVec(), 16), Cluster(getRandVec(), 17), Cluster(getRandVec(), 18), som.Cluster(getRandVec(), 19)),
                (Cluster(getRandVec(), 20), Cluster(getRandVec(), 21), Cluster(getRandVec(), 22), Cluster(getRandVec(), 23), som.Cluster(getRandVec(), 24))
            ]
"""

map         = som.Map(clusters)
neigh       = som.RectangularNeighborhood(map, neighborhood)
learnRate   = som.LinearDescendingLearnRate(0.5, 0.95, 100)

net = som.SOM(map, neigh, learnRate)


    ######

tree = {    'A': {  'padrao':(1,0,0,0,0),
                    'cluster': None },

            'B': {  'padrao': (2,0,0,0,0),
                    'cluster': None},

            'C': {  'padrao': (3,0,0,0,0),
                    'cluster': None},

            'D': {  'padrao': (4,0,0,0,0),
                    'cluster': None},

            'E': {  'padrao': (5,0,0,0,0),
                    'cluster': None},

            'F': {  'padrao': (3,1,0,0,0),
                    'cluster': None},

            'G': {  'padrao': (3,2,0,0,0),
                    'cluster': None},

            'H': {  'padrao': (3,3,0,0,0),
                    'cluster': None},

            'I': {  'padrao': (3,4,0,0,0),
                    'cluster': None},

            'J': {  'padrao': (3,5,0,0,0),
                    'cluster': None},

            'K': {  'padrao': (3,3,1,0,0),
                    'cluster': None},

            'L': {  'padrao': (3,3,2,0,0),
                    'cluster': None},

            'M': {  'padrao': (3,3,3,0,0),
                    'cluster': None},

            'N': {  'padrao': (3,3,4,0,0),
                    'cluster': None},

            'O': {  'padrao': (3,3,5,0,0),
                    'cluster': None},

            'P': {  'padrao': (3,3,6,0,0),
                    'cluster': None},

            'Q': {  'padrao': (3,3,7,0,0),
                    'cluster': None},

            'R': {  'padrao': (3,3,8,0,0),
                    'cluster': None},

            'S': {  'padrao': (3,3,3,1,0),
                    'cluster': None},

            'T': {  'padrao': (3,3,3,2,0),
                    'cluster': None},

            'U': {  'padrao': (3,3,3,3,0),
                    'cluster': None},

            'V': {  'padrao': (3,3,3,4,0),
                    'cluster': None},

            'W': {  'padrao': (3,3,6,1,0),
                    'cluster': None},

            'X': {  'padrao': (3,3,6,2,0),
                    'cluster': None},

            'Y': {  'padrao': (3,3,6,3,0),
                    'cluster': None},

            'Z': {  'padrao': (3,3,6,4,0),
                    'cluster': None},

            '1': {  'padrao': (3,3,6,2,1),
                    'cluster': None},
                    
            '2': {  'padrao': (3,3,6,2,2),
                    'cluster': None},

            '3': {  'padrao': (3,3,6,2,3),
                    'cluster': None},

            '4': {  'padrao': (3,3,6,2,4),
                    'cluster': None},

            '5': {  'padrao': (3,3,6,2,5),
                    'cluster': None},

            '6': {  'padrao': (3,3,6,2,6),
                    'cluster': None},

        };

treeOrderedKeys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'I', 'S', 'W', 'J', 'T', 'X', '1', '2', '3', '4', '5', '6', 'U', 'Y', 'V', 'Z']
presentationOrder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6']
treeOrderedClassifications = []
clustersSymbol = ['o', '+', ':', '@', '=', '&', '~', '%', '*', '^', ';', '#', '?', '|', 'H', '{', ']']

treeRepresentation =   """
            %s %s %s %s %s
                %s
                %s
                %s %s %s %s %s %s %s %s %s
                %s     %s     %s
                %s     %s     %s %s %s %s %s %s %s
                      %s     %s
                      %s     %s
            """

print treeRepresentation % tuple(treeOrderedKeys)



### Training ###
dataset = [v['padrao'] for k,v in tree.items()]

net.train(dataset, trainingCycles)


# classify everybody
#for k in tree.keys():
for k in presentationOrder:
    tree[k]['cluster'] = net.classify(tree[k]['padrao']).getID()

for k in treeOrderedKeys:
    treeOrderedClassifications.append( tree[k]['cluster'] )

#print treeRepresentation % tuple([clustersSymbol[i] for i in treeOrderedClassifications])
print treeRepresentation % tuple(treeOrderedClassifications)
print treeOrderedClassifications

print "\n\n### INITIAL MAP (Node Numbers) ###"

nodeNumber = 0
for i in xrange(0, lines):
    nodes = []
    for j in xrange(0, columns):
        nodes.append( nodeNumber )
        nodeNumber += 1
    print '-' + '-----' * len(nodes)
    print "| %s |" % ' | '.join([ str(x).ljust(2) for x in nodes])

print '-' + '-----' * len(nodes)


print "\n\n### FINAL MAP (Patterns in each cluster) ###"

nodeNumber = 0
for i in xrange(0, lines):
    nodes = []
    for j in xrange(0, columns):
        nodes.append( treeOrderedClassifications.count(nodeNumber) )
        nodeNumber += 1
    print '-' + '-----' * len(nodes)
    print "| %s |" % ' | '.join([ str(x).ljust(2) for x in nodes])

print '-' + '-----' * len(nodes)
