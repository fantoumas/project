from pygenalg.gene import Gene
import random

class GeneList(Gene):
    """
        A class represeting a list of genes, implementing the Gene class

        @author     Thiago F Pappacena
    """

    
    def __init__(self, *values):
        """
            Build an numeric gene

            @author     Thiago F Pappacen
            @param      list        The list of genes
        """
        Gene.__init__(self, values)
    # end :: __init__


    @classmethod
    def getRandomInstance(cls):
        """
            Gets a NumericGene with random value

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      A random GeneList
        """
        raise NotImplementedError('You cannot get a random instance of GeneList')
    # end :: getRandomInstance


    def mutate(self):
        """
            Do a mutation in this gene, changing it's value

            @author     Thiago F Pappacena
            @param      void        void
            @return     void
        """
        random.choice(self.value).mutate()
    # end :: mutate


    def copy(self):
        """
            Make a copy of a NumericGene

            @author     Thiago F Pappacena
            @param      void        void
            @return     object      The GeneList copy
        """
        return self.__class__(self.value)
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
        if not recursive:
            return super(Gene, self).getValue()
        return [i.getValue() for i in self.value]
    # end :: getValue


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
