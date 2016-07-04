from Continent import *
import Pyro.core


def getContinent(host, port):
    """

    """
    return Pyro.core.getAttrProxyForURI('PYROLOC://%s:%s/continent' % (host, port))
# end :: getContinent
