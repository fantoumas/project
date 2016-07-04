class MLPException(Exception):
    """
        Base MLP Exception

        @author     Thiago F Pappacena
    """
    pass

class InputSizeMissmatch(MLPException):
    """
        Missmatch between input size and number of neurons

        @author     Thiago F Pappacena
    """
    pass

class DataTypeMissmatch(MLPException):
    """
        Missmatch between required datatypes

        @author     Thiago F Pappacena
    """
    pass

class WrongLayersOrganization(MLPException):
    """
        Wrong organization of layers

        @author     Thiago F Pappacena
    """
    pass

class LayerUseException(MLPException):
    """
        Wrong use of a layer

        @author     Thiago F Pappacena
    """
    pass
