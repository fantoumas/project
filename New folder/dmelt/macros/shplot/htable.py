from jhplot import HTable,H1D,F1D,P1D,P2D,P3D,P0D 


"""

Build a table to keep data
S.Chekanov (ANL)

"""
class htable(HTable):

    def __init__(self): 
        HTable.__init__()
 

if __name__ == '__main__':

     h=htable()
