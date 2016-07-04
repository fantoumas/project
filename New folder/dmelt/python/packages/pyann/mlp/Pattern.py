from pyann.mlp import DataTypeMissmatch

class Pattern(object):
    def __init__(self, input, output = None):
        """
            Build a pattern

            @author     Thiago F Pappacena
            @param      tuple   input       The input pattern
            @param      tuple   output      The output from pattern [optional]
        """
        if type(input) != type(()):
            raise DataTypeMissmatch('Pattern input must be a tuple. Got %s' % type(input))
        if type(output) != type(()):
            raise DataTypeMissmatch('Pattern output must be a tuple. Got %s' % type(output))
        self.__input = input
        self.__output = output
    # end :: __init__


    def setInput(self, input):
        """
            Defines the input pattern

            @author     Thiago F Pappacena
            @param      tuple   input   The input from pattern
            @return     void
        """
        if type(input) != type(()):
            raise DataTypeMissmatch('Pattern input must be a tuple. Got %s' % type(input))       
        self.__input = input
    # end :: setInput


    def getInput(self):
        """
            Get the input from this pattern

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The input tuple
        """
        return self.__input
    # end :: getInput

    
    def setOutput(self, output):
        """
            Defines the output for this pattern

            @author     Thiago F Pappacena
            @param      tuple   output  The output for this pattern
            @return     void
        """
        if type(output) != type(()):
            raise DataTypeMissmatch('Pattern output must be a tuple. Got %s' % type(output))
        self.__output = output
    # end :: setOutput


    def getOutput(self):
        """
            Returns the output from this pattern

            @author     Thiago F Pappacena
            @param      void    void
            @return     tuple   The output
        """
        return self.__output
    # end :: getOutput

    def __str__(self):
        """
        """
        return '<pyann.mlp.Pattern object (%s) ~> (%s)>' % (self.__input, self.__output)

# end :: Pattern
