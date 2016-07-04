
class Gene(object):
    """
        Abstract class representing one characteristic of a chromossome

        @abstract
        @author     Thiago F Pappacena
    """

    def __init__(self, value):
        """
            Build the Gene

            @author     Thiago F Pappacena
            @param      mixed       value       The value of the gene
        """
        self.value = value
    # end :: __init__


    @classmethod
    def getRandomInstance(cls):
        """
            Abstract method to build a random instance of the Gene

            @abstract
            @author     Thiago F Pappacena
            @param      void    void
        """
        raise NotImplementedError('This method must be implemented in subclasses')
    # end :: getRandomInstance


    def getValue(self):
        """
            Returns the value of the gene

            @author     Thiago F Pappacena
            @param      void        void
            @return     mixed       The value of this gene
        """
        return self.value
    # end :: getValue

    def setValue(self, value):
        """
            Define the value of the gene

            @author     Thiago F Pappacena
            @param      mixed   value   The gene value
            @return     void
        """
        self.value = value
    # end :: setValue



    def mutate(self):
        """
            Do a random mutation in this gene

            @abstract
            @author     Thiago F Pappacena
            @param      void
        """
        raise NotImplementedError('This method must be implemented in subclasses')
    # end :: mutate

    
    def copy(self):
        """
            Makes a copy of the Gene

            @author     Thiago F Pappacena
            @param      void        void
            @return     Gene        A copy of this object
        """
        return self.__class__(self.value)
    # end :: copy


    def __repr__(self):
        """
            Returns the string representation of the Gene

            @author     Thiago F Pappacena
            @param      void        void
            @return     string      The representation
        """
        return "%s(%s)" % (self.__class__.__name__, self.value)
    # end :: __repr__

# end :: Gene
