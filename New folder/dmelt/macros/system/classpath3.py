import sys

import java.lang
#import java.lang.reflect.Method
import java.io.File
import java.net.URL
import java.net.URLClassLoader
import jarray

##############################################################################

TARGET_JAR = 'C:/apps/Moneta/SP4-QFE260/server/lib/pop3.jar'

##############################################################################


##############################################################################################

"""
Hello everybody, I've work a little bit on this problem. 
The solution posted by Antony Miguel is really cool, but it sounds 
like too much of a hack. The day sun (or anyother JVM vendor) changes 
the default classloader from a subclass of URLClassLoader to a 
subclass of WhatTheHellClassLoader it will stop working, and so will the 
app written upon that.

So because an app I'm writing needs something like that (well, to be honest,
I can address the problem in another way, and probably I will do so... 
but that's not the point...) I spent some time hacking on it.

The result of my thoughts can be found here:
http://arys.sytes.net/awiki/SomeDocs/JavaAddableClassLoader

The main idea is to use a custom classloader (Actually a subclass of 
URLClassLoader) and in the main method set it as the current ClassLoader 
of the Thread and the current ClassLoader of the class.

This way the custom classloader will be used in the rest of the application. 
The only way (well, at least the only way I have found...) this can be 
bypassed is when some code forces the classloader to be 
ClassLoader.getSystemClassLoader. I don't know if this could be a problem.

The pro of this method is that it doesn't make an assumption on the 
environment and it is based only on the J2SE documented API so it should 
be safe.
"""

import com.sun.mail.pop3

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

def demo():
    import com.sun
    print dir(com.sun)

    #
    # when you need to use run-time CLASSPATH Augmentation
    #
    ALIEN_JAR = 'C:/apps/Moneta/SP4-QFE260/server/lib/pop3.jar'

    cpa = ClassPathAugmenter()
    a = cpa.addJar(ALIEN_JAR)

    #showProperties('class.path')
    #startupClassPath = r'C:\apps\jython22b\jython.jar;.'
    java.lang.System.setProperty('java.class.path', '%s;%s' % \
                                 (startupClassPath, ALIEN_JAR))

    #try :
    #    cpa = ClassPathAugmenter()
    #    a = cpa.addJar(ALIEN_JAR)
    #except :
    #    sys.stderr.write("still failed \n%s" % (sys.exc_info() ))
    #    sys.exit(1)

    import com.sun.mail.pop3

    print dir(com.sun.mail.pop3)
    popper = com.sun.mail.pop3.POP3Message()

##############################################################################################

#demo()

