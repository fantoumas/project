import sys, os

import java.lang
import java.io.File
import java.net.URL
import java.net.URLClassLoader

import jylluminate

##############################################################################

"""
robbieshere posted this in Feb 2007 in response to Java approach 
implemented as classpath.py
	
Thats a good way to do it, but I found creating a custom class loader 
which extends URLClassLoader was a cleaner way to do it. 
Defining the following constructor...

public NewURLClassLoader (URL[] u)
       {
           super(u);
       }

and using it this way worked for me:

File file  = new File("path_here");
URL[] urls = new URL[]{ file.toURL() };

NewURLClassLoader loader = new NewURLClassLoader(urls);

loader.addURL(file.toURL());
loader.loadClass("class_here");
"""
##############################################################################

class MyClassLoader(java.net.URLClassLoader):

    def addURL(self, url):
        java.net.URLClassLoader.addURL(self, url)
        #myClassLoader.addURL(self, url)

class ClassPathAugmenter(java.lang.Object):
    def addURL(self, jarFilePath):
        jarFile = java.io.File(jarFilePath)
        urls = [jarFile.toURL()]
        myCL = MyClassLoader(urls)
        print "got myCL..."
        print jylluminate.methods(myCL)
        #stuff = dir(myCL)
        #for item in stuff:
        #    print item
        #URLClassLoader.findLoadedClass()
        # 
        #packages
        #classes = getattr(myCL, 'classes')
        #print classes

        #myCL.loadClass('test.out.of.classpath.OutOfClassPath')
        #print "loaded OutOfClassPath class"

        #obj = OutOfClassPath()
        #obj = test.out.of.classpath.OutOfClassPath()

##############################################################################

def demo():

    TARGET_JAR = "C:/apps/jardump/foreign.jar"
    cpa = ClassPathAugmenter()
    cpa.addURL(TARGET_JAR)

    sys.path.insert(0, os.path.dirname(TARGET_JAR))
    #test = __import__('test', globals(), locals())

    #tooc = test.out.of.classpath
    #print "tooc is a %s" % type(tooc)
    #print dir(tooc)
    #obj = tooc.OutOfClassPath()
    #print dir(obj)

    import test.out.of.classpath
    print "imported the target package!"
    print "symbols known in the test.out.of.classpath namespace"
    print dir(test.out.of.classpath)
    print "\nObtaining a instance of OutOfClassPath..."
    OOCP = test.out.of.classpath.OutOfClassPath
    oocp = OOCP()

##############################################################################

def showProperties(target=None):
    props = java.lang.System.getProperties()
    propNames = props.keys()
    for propName in propNames:
        if target:
            if  propName.find(target) >= 0:
                print propName, props[propName]
        else:
            print propName, props[propName]

##############################################################################
##############################################################################

demo()

