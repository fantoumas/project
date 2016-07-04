from urllib2 import *

_author__  = 'S.Chekanov'
__version__ = 1.1

##############################################################################

"""
   Get http files (similar to linux wget  
"""

def getURLName(url):
        directory=os.curdir

        name="%s%s%s" % (
                directory,
                os.sep,
                url.split("/")[-1]
        )

        return name

def createDownload(url):
        instream=urlopen(url)

        filename=instream.info().getheader("Content-Length")
        if filename==None:
                filename="temp"

        return (instream, filename)


def wget(url):

 try:
   outfile=open(getURLName(url), "wb")
   fileName=outfile.name.split(os.sep)[-1]
   url, length=createDownload(url)
   print "Downloading %s (%s bytes) ..." % (url.url, length)
   if not length:
               length="?"
               print "File empty or does not exists"
               sys.exit(1)
 
   length=float(length)
   sc=length/10;
   count=0.0
   while count<length:
      data=url.read(int(sc))
      count+=sc
      outfile.write(data)
      print "%s: %.02f/%.02f kb (%d%%)" % (
                                                fileName,
                                                count/1024.0,
                                                length/1024.0,
                                                100*count/length
                                           )
        

   url.close()
   outfile.close()
   print "Done"

 except Exception, e:
         print "Error downloading %s: %s" % (url, e)

