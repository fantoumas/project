

class ART1(object):
    def __init__(self, f1, f2, orientSys):
        self.f1 = f1
        self.f2 = f2
        self.orientSys = orientSys
    # end :: __init__


    def classify(self, input):
        
        self.f1.clear()
        self.f2.clear()

        f1Output = self.f1.getOutput(input)

        while True:
            winner = self.f2.selectWinner(f1Output)
            if winner is None:      # there's no winner candidate
                break               # break

            f1Output = self.f1.getOutput( input, winner.getTopDownWeights() )
            #print "saind ode f1: %s (vetor de entrada %s)" % (str(f1Output), str(input))

            if not self.orientSys.triggerReset(input, f1Output):  # if reset was not triggered
                self.f2.updateWinner(input)                 # update winner
                break                                       # stop searching
            else:
                self.f2.resetWinner()
        # end :: while True

        return winner
    # end :: classify

# end :: ART1


class ART1Exception(Exception):
    pass

class ART1SizeMissmatch(ART1Exception):
    pass
