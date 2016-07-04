import sys, os

from java.lang import System, Class, Object
import java
import java.net
import jarray

import jpi

#####################################################################################

"""
Some guy named Frederic Darthevel wrote
[The Antony Miguel ... solution]
   can solve the problem but it has 2 main drawbacks :
   - it does NOT work if the current classloader is NOT an URLClassLoader 
     (it's the case under Eclipse environment).
   - it seems weird to use the setAccessible method to use a protected function 
     (if the conceptor of this function designed it as protected, one can think 
     that he had good reasons to do it !!!).
     [ktl --  Often the conceptor is just into hiding...]

I propose an alternative solution that works in every context :

Suppose you want to load a class (lets' call it "myClass") that lies 
in some path (let's call it myClassPath) :

// Retrieve the current classpath
ClassLoader currentClassLoader = this.getClass().getClassLoader();

// Convert myClassPath to an URL
URL classpathURL = null;
try 
{
    File fileClasspath = new File(myClassPath );
    classpathURL = fileClasspath .toURL();
}
catch (MalformedURLException ex)
{
    // handle the exception
}

// Construct the new URL
URL [] urlClasspathArray = new URL [1];
urlClasspathArray[0] = classpathURL;

// Create the new classloader
URLClassLoader newClassLoader = new URLClassLoader(urlClasspathArray,currentClassLoader);

// Load the class
Class theClass = null;
try 
{
   theClass = newClassLoader.loadClass("myClass");
}
catch (ClassNotFoundException ex)
{
   // handle the exception
}

// At this step,
// Either an exception has been thrown (MalformedURLException or
// ClassNotFoundException)
// or the class "myClass" is loaded. 
"""

#############################################################################################

TARGET_JAR = "C:/apps/jardump/foreign.jar"
TARGET_PKG = 'test.out.of.classpath'
TARGET_CLASS = 'OutOfClassPath'

#############################################################################################

class ClassPathAugmenter(java.lang.Object):
    def addJar(self, jarFilePath):
        url = java.net.URL('file://%s' % jarFilePath)
        targJar = jarray.array([url], java.net.URL)
        currClassLoader = self.classLoader()
#       print "currClassLoader is a %s" % currClassLoader.__class__.__name__
        newClassLoader = java.net.URLClassLoader(targJar, currClassLoader)
#       print "got a new class loader!..."
#       print "newClassLoader is a %s" % newClassLoader.__class__.__name__
        sys.path.insert(0, os.path.dirname(jarFilePath))

    def classLoader(self):
        currClassLoader = self.getClass().getClassLoader()
        return currClassLoader

#############################################################################################

def demo(targetJar, packageChain, targetClass):
    cpa = ClassPathAugmenter()
    cpa.addJar(targetJar)

    import test.out.of.classpath
    print "imported the target package"
    print "\nsymbols known in the target package namespace:"
    print dir(test.out.of.classpath)
    print "\nObtaining an instance of OutOfClassPath..."
    OOCP = test.out.of.classpath.OutOfClassPath
    oocp = OOCP()

#############################################################################################

def spillPackageInfo(targetPkg):
    print "\nExamining target package: %s" % targetPkg
    pkgs, ifcs, classes = jpi.packageElements(targetPkg)

    if pkgs:
        print "Packages:"
        for pkg in pkgs:
            print "    %s" % pkg
    else:
        print "No subpackages..."

    print " "

    if ifcs:
        print "Interfaces:"
        for ifc in ifcs:
            print "    %s" % ifc
    else:
        print "No interfaces..."

    print " "

    if classes:
        print "Classes:"
        for className in classes:
            print "    %s" % className
    else:
        print "No Classes..."

#############################################################################################

demo(TARGET_JAR, TARGET_PKG, TARGET_CLASS)
spillPackageInfo(TARGET_PKG)

#############################################################################################

