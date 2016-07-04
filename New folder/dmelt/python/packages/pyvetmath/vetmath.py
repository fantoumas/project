import math


def vectorNorm(vector):
    """
        Get the euclidean norm for the input vector
        
        @author       Thiago F Pappacena
        @param        tuple     vector      The vector
        @return       The vector norm
    """
    return math.sqrt(sum([math.pow(i, 2) for i in vector]))
# end :: vectorNorm


def normalize(vector, e = 0.0):
    """
        Returns the input vector divided by it's norm

        @author     Thiago F Pappacena
        @param      tuple       vector  The vector
        @param      float       e       Set this parameter to a small value to avoid zero-division
        @return     A list with the normalized vector
    """
    norm = vectorNorm(vector)
    return tuple([i/(norm+e) for i in vector])
# end :: normalize


def applyThreshold(vector, threshold):
    """
        Apply a threshold for every vector index

        This function will return, for each index i
            vector[i]       It vector[i] >= threshold
            0               If vector[i] < threshold

        @author     Thiago F Pappacena
        @param      list        vector      The vector
        @param      float       threashold  The threshold to be applyed
        @return     A list with the f(vector)
    """
    return tuple([i > threshold and i or 0 for i in vector])
# end :: applyThreshold


def makeEmptyVector(size):
    """
        Build and returns a vector (list) with all index equals to zero

        @author     Thiago F Pappacena
        @param      integer     size        The vector size (number of dimensions)
        @return     list        The empty vector
    """
    return tuple([0 for i in xrange(0, size)])
# end :: makeEmptyVector


def makeRandomVector(size, min = 0.0, max = 1.0):
    """
        Build a random vector with random indexes

        @author     Thiago F Pappacena
        @param      integer     size    The vector size
        @param      float       min     The minimum random number
        @param      float       max     The maximum random number
    """
    import random
    return tuple([min + (random.random() * (max-min)) for i in range(size)])
# end :: makeRandomVector


def makeRandomMatrix(lines, columns, min = 0.0, max = 1.0):
    """
        Build a random matrix

        @author     Thiago F Pappacena
        @param      integer     lines   The number of lines in the matrix
        @param      integer     columns The number of clumns in each line of the matrix
        @param      float       min     The minimum random number
        @param      float       max     The maximum random number
        @return     tuple       A tuple of tuples representing the matrix
    """
    matrix = []
    for l in range(lines):
        matrix.append(makeRandomVector(columns, min, max))
    return tuple(matrix)
# end :: makeRandomMatrix
