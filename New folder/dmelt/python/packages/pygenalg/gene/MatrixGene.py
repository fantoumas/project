from pygenalg.gene import Gene, FloatGene
import random

class MatrixGene(Gene):
    """
        A class represeting a matrix of genes, implementing the Gene class

        @author     Thiago F Pappacena
    """

    
    def __init__(self, values):
        """
            Build an numeric gene

            @author     Thiago F Pappacen
            @param      list        The list of genes
        """
        Gene.__init__(self, None)
        self.lines = len(values)
        self.columns = len(values[0])
        self.value = values
        #self.value = list(range(0,self.lines))

        #for i in range(len(values)):
        #    line = values[i]
        #    assert len(line) == self.columns, 'Dimension missmatch in MatrixGene creation!'
        #    self.value[i] = list(theclass(i) for i in line)

    # end :: __init__


    @classmethod
    def getRandomInstance(cls, lines = 5, columns = 5, theclass = FloatGene):
        """
            Gets a MatrixGene with random value

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      A random GeneList
        """
        #lineList = []
        #for i in range(lines):
        #    lineList.append( tuple(theclass.getRandomInstance() for i in range(columns)) )
        #return cls(lineList)
        return cls( tuple(  tuple(theclass.getRandomInstance() for j in range(columns)) 
                            for i in range(lines)   ) 
                )
    # end :: getRandomInstance


    def mutate(self):
        """
            Do a mutation in this gene, changing it's value

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        print 'muuuuu'
        random.choice(random.choice(self.value)).mutate()
    # end :: mutate


    def copy(self):
        """
            Make a copy of a NumericGene

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      The GeneList copy
        """
        return self.__class__(self.getValue(recursive = False))
    # end :: copy


    def getValue(self, recursive = False):
        """
            Returns the value of this gene list

            If recursion parameter is True, this will get the value of
            every item in value list, including sublists

            @author     Thiago F Pappacena
            @param      boolean     recursive   The the value of itens recursivily?
            @return     list        The list of values in this GeneList
        """
        if recursive:
            return tuple(tuple(x.getValue() for x in line) for line in self.value)
        return self.value
    # end :: getValue


    def planify(self):
        """
            Planify the 2D matrix to a single-dimensional list

            @author     Thiago F Pappacena
            @param      void    void
            @return     list    The single-dimensional matrix 
        """
        r = []
        for i in self.value:
            r += i
        return r
    # end :: planify

    
    @classmethod
    def fromPlanified(self, line, lines, columns):
        """
            Arrange the line into a lines x columns matrix and return this MatrixGene

            @author     Thiago F Pappacena
            @param      list    line    The list of values
            @param      integer lines   The number of lines in final matrix
            @param      integer columns The number of columns in final matrix
        """
        assert lines * columns == len(line), 'Not a valid size for values in %sx%s matrix' % (lines, columns)
        return MatrixGene( tuple(line[ i*columns : i*columns + columns ] for i in range(lines)) )
    # end :: unplanify


    def __len__(self):
        """
            Returns the length of this GeneList

            @author     Thiago F Pappacena
            @param      void        void
            @return     integer     The list size
        """
        return len(self.value)
    # end :: __len__


    def __getitem__(self, item):
        """
            Get an item from the list

            @author     Thiago F Pappacena
            @param      integer     item    The item
        """
        return self.value[item]
    # end :: __getitem__


    def __getslice__(self, x, y):
        """
            Get a slice from the list

            @author     Thiago F Pappacena
            @param      integer     x   Begining of slice
            @param      integer     y   Ending of slice
            @return     list        The slice
        """
        return self.__class__(self.value[x:y])
    # end :: __getslice__


    def __contains__(self, gene):
        """
            Checks if the gene is in this list

            @author     Thiago F Pappacena
            @param      object      gene        The Gene
            @return     boolean     Is gene in the list?
        """
        return gene in self.value
    # end :: __contains__

# end :: GeneList
