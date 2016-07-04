import sys, os

import java.lang
import java.io.File
import java.net.URL
import java.net.URLClassLoader
import jarray

import jylluminate

##############################################################################

TARGET_JAR = 'C:/apps/jardump/foreign.jar'

##############################################################################

class ClassPathAugmenter(java.lang.Object):
    """
        based on  http://forum.java.sun.com/thread.jspa?threadID=300557
        Author: SG Langer Jan 2007 translated the above Java to this
                Jython class
        Purpose: Allow runtime additions of new Class/jars either from
                 local files or URL
    """

    def addJar(self, jarFilePath):
        """
            Supply the filesystem path to a jar file
            Returns an URL
        """
        module = "utils:ClassPathAugmenter: addJar"

        # make a URL out of 'jarFilePath'
        file = java.io.File (jarFilePath)
        url = file.toURL()
        #print url
        addedURL = self.addURL(url)
        return addedURL

    def addURL(self, url):
        """
            Supply a valid URL for the Class or jar to be loaded
        """
        module = "utils:ClassPathAugmenter: addURL"
        parameters = jarray.array([java.net.URL], java.lang.Class)
        #parameters = self.jarray.array([self.java.net.URL], self.java.lang.Class)

        sysloader =  java.lang.ClassLoader.getSystemClassLoader()
        print jylluminate.methods(sysloader)

        sysclass = java.net.URLClassLoader
        method = sysclass.getDeclaredMethod("addURL", parameters)
        #print method
        a = method.setAccessible(1)
        jar_a = jarray.array([url], java.lang.Object)
        b = method.invoke(sysloader, jar_a)

        print "urls known by the URLClassLoader" 
        getURLs = sysclass.getDeclaredMethod("getURLs", None)
        urls = getURLs.invoke(sysloader, jarray.array([], java.lang.Object))
        for url in urls:
            print "    %s" % url
        print " "
        return url


##############################################################################################

def showProperties(target=None):
    props = java.lang.System.getProperties()
    propNames = props.keys()
    for propName in propNames:
        if target:
            if  propName.find(target) >= 0:
                print propName, props[propName]
        else:
            print propName, props[propName]

##############################################################################################

def demo():
    """
        Here's a demonstration of how to effect a run-time augmentation
        of the CLASSPATH with a target jar file and obtain components within
        that jar file.
    """
    #showProperties('java.class.path')
    #startupClassPath = r'C:\apps\jython22b\jython.jar;.'
    #java.lang.System.setProperty('java.class.path', '%s;%s' % \
    #                             (startupClassPath, TARGET_JAR))

    try :
        cpa = ClassPathAugmenter()
        a = cpa.addJar(TARGET_JAR)
    except :
        sys.stderr.write("Unable to load your jar target of '%s'\n%s" % \
                          (TARGET_JAR, sys.exc_info() ))
        sys.exit(1)

    #showProperties('java.class.path')

    sys.path.insert(0, os.path.dirname(TARGET_JAR))
    import test.out.of.classpath

    print "symbols in the test.out.of.classpath namespace"
    print dir(test.out.of.classpath)
    print " "
    oocp = test.out.of.classpath.OutOfClassPath()

##############################################################################################

demo()

