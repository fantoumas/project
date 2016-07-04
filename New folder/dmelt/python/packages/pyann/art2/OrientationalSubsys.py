import pyvetmath as vetmath

class OrientationalSubsys(object):
    
    def __init__(self, c, rho, d, debug = True):
        self.c = c

        if rho < 0 or rho > 1:
            raise ART2InvalidIntialization('Rho must be between 0 and 1')

        self.rho = rho
        self.debug = debug
        self.r = ()

    # end :: __init__


    def dump(self, title, vector):
        if self.debug:
            print "%s ~> %s" % (title, vector)


    def triggerReset(self, u, p):
        self.setR(u, p)

        rSize = vetmath.vectorNorm(self.r)
        self.dump('r-Size', rSize)
        self.dump('rho', self.rho)
        if rSize < self.rho:
            self.dump('\n\n\n**RESET', 'TRIGGERED **\n\n')
            return True
        return False
    # end :: triggerReset


    def setR(self, u, p):
        if len(u) != len(p):
            raise ART2SizeMissmatch('U and P do not have the same length')

        cp = [self.c * x for x in p]

        cpSize = vetmath.vectorNorm(cp)
        uSize  = vetmath.vectorNorm(u)

        self.r = tuple([ (u[i] + cp[i]) / (uSize + cpSize) for i in xrange(0, len(p)) ])
        self.dump('u', u)
        self.dump('p', p)
        self.dump('r', self.r)
    # end :: setR
