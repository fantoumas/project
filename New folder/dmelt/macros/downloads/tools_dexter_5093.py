from debuxter import JDebux;
import urllib

#print "run debuxter"
#file=SystemDir+fSep+"macros"+fSep+"examples"+fSep+"data"+fSep+"example.gif"

wfile="example.gif"
urllib.urlretrieve ("http://jwork.org/dmelt/examples/data/"+wfile,wfile)

c1=JDebux(wfile)
