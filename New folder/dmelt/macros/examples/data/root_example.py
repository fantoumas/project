#
# To see the output of this macro, click begin_html <a href="gif/gerrors.gif">here</a>. end_html
#


from ROOT import * 
from ROOT import gROOT
from array import array
from math import sin
from array import array


gROOT.Reset()

c1 = TCanvas( 'c1', 'A Simple Graph with error bars', 200, 10, 700, 500 )

c1.SetFillColor( 42 )
c1.SetGrid()
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 12 )

n = 10;
x  = array( 'f', [ -0.22, 0.05, 0.25, 0.35,  0.5, 0.61,  0.7, 0.85, 0.89, 0.95 ] )
ex = array( 'f', [  0.05,  0.1, 0.07, 0.07, 0.04, 0.05, 0.06, 0.07, 0.08, 0.05 ] )
y  = array( 'f', [     1,  2.9,  5.6,  7.4,  9.0,  9.6,  8.7,  6.3,  4.5,    1 ] )
ey = array( 'f', [  0.8,  0.7,  0.6,  0.5,  0.4,  0.4,  0.5,  0.6,  0.7,  0.8  ] )
exl = array( 'f', [  0.05,  0.1, 0.07, 0.07, 0.02, 0.02, 0.02, 0.05, 0.05, 0.08 ] )
exh = array( 'f', [  0.08,  0.1, 0.07, 0.07, 0.04, 0.05, 0.04, 0.05, 0.07, 0.05 ] )
eyl = array( 'f', [  0.05,  0.12, 0.1, 0.07, 0.03, 0.05, 0.06, 0.07, 0.08, 0.05 ] )
eyh = array( 'f', [  0.08,  0.1, 0.07, 0.03, 0.04, 0.04, 0.04, 0.08, 0.07, 0.07 ] )

gr = TGraphErrors( n, x, y, ex, ey )
gr.SetName("TGraphError_example")
gr.SetTitle( 'TGraphErrors Example' )
gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )
gr.Draw( 'ALP' )


gr0=TGraphAsymmErrors(n,x,y,exl,exh,eyl,eyh);
gr0.SetName("TGraphAsymmErrors_example")
gr0.SetTitle( 'TGraphErrors Example' )



n = 20
x, y = array( 'd' ), array( 'd' )
for i in range( n ):
   x.append( 0.1*i )
   y.append( 10*sin( x[i]+0.2 ) )
   print ' i %i %f %f ' % (i,x[i],y[i])
gr1 = TGraph( n, x, y )
gr1.SetName("TGraph_example")
gr1.SetLineColor( 2 )
gr1.SetLineWidth( 4 )
gr1.Draw( 'ACP' )

import ROOT
# Initialize random number generator.
gRandom.SetSeed()
rannor, rndm = gRandom.Rannor, gRandom.Rndm
# Fill histograms randomly.
px, py = Double(), Double()



# Create some histograms, a profile histogram and an ntuple
hpx    = TH1F( 'hpx', 'This is the px distribution', 100, -4, 4 )
hpxpy  = TH2F( 'hpxpy', 'py vs px', 40, -4, 4, 40, -4, 4 )
for i in xrange( 25000 ):
 # Generate random values.
   rannor( px, py )
   pz = px*px + py*py
   random = rndm(1)

 # Fill histograms.
   hpx.Fill( px )
   hpxpy.Fill( px, py )





na = TFile( 'root_example.root','RECREATE', 'Demo ROOT file with histograms' )
gr.Write()
gr0.Write()
gr1.Write()
hpx.Write()
hpxpy.Write()
na.Write()
na.Close()


c1.Update()
