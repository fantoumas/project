#!/usr/bin/env python

from pyann import art2
import sys

a = 10.0
b = 10.0
c = 0.1
d = 0.9
rho = float(raw_input('Rho: '))
learnRate = 0.6
clusters = 100
m = 5
threshold = float(raw_input('Threshold: '))
debug = raw_input('Debug? ').strip().lower() in ['s', 'y', 't', 'sim', 'yes', 'true']
learnCycles = 10

clusters = [art2.Cluster(m, d, learnRate, i, debug) for i in xrange(0, clusters)]

f1      = art2.DefaultF1Layer(m, a, b, d, threshold, learnCycles, debug = debug)
f2      = art2.DefaultF2Layer(m, d, learnRate, clusters, debug = debug)
oriSys  = art2.OrientationalSubsys(c, rho, d, debug = debug)

net = art2.ART2(f1, f2, oriSys)

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


# classify everybody
#for k in tree.keys():
for k in presentationOrder:
    tree[k]['cluster'] = net.classify(tree[k]['padrao']).getID()

for k in treeOrderedKeys:
    treeOrderedClassifications.append( tree[k]['cluster'] )

print treeRepresentation % tuple([clustersSymbol[i] for i in treeOrderedClassifications])

# legenda

print '\n\nLegenda:'
print 'Simbolo ~> ID do cluster'
for i in xrange(0, len(clustersSymbol)):
    print "%s ~> %s" % (clustersSymbol[i], i)
