class OrientSystem(object):

    def __init__(self, rho):
        self.rho = rho
    # end :: __init__


    def triggerReset(self, input, f1activation):
        if len(input) != len(f1activation):
            raise ART1SizeMissmatch('Vectors sizes missmatch (%s / %s)' % (len(input), len(f1activation)))

        normInput = sum(input)
        normF1Activation = sum(f1activation)

        #print "\n%s / %s" % (normF1Activation, normInput)
        #print "Reset check: %s" % (normF1Activation / float(normInput))
        return (normF1Activation / float(normInput)) < self.rho
    # end :: triggerReset
        
