
#############################################################################
#
#  jpi -- Java Package Information
#
#         given a Java package identifier (java, java.util, javax.servlet),
#         list the subpackages in the named package and all the 
#         interfaces and classes in the package
#
#         Uses dir(), getattr() and type() to make the determination
#
#         Differentiating interfaces from classes is done by
#         using java.lang.Class.isInterface(target)
#
#############################################################################

import sys
import java.lang

from org.python.core import PyJavaClass, PyJavaPackage, PyString

#############################################################################

PY_STRING    = PyString
JAVA_PACKAGE = PyJavaPackage
JAVA_CLASS   = PyJavaClass

#############################################################################

def main(target):

    print "target: %s" % target
    javaPackages, javaInterfaces, javaClasses = packageElements(target)

    for jp in javaPackages:
        print "%-32.32s : Java Package" % jp

    print " "

    for ji in javaInterfaces:
        print "%-32.32s : Java Interface" % ji

    print " "

    for jc in javaClasses:
        print "%-32.32s : Java Class" % jc

#############################################################################

def packageElements(target):
    """
        Given a dot separated string represent a Java package name
        determine the sub-packages and classes that exist in that 
        target package.

        Return back two lists:
            1) list of package names in the target
            2) list of class   names in the target
    """

    targetComponents = target.split('.')
    base = targetComponents[0]
    baseMod = __import__(base, globals(), locals())

##    print dir(baseMod)

    mod = baseMod    # we will reassign mod value repeatedly in for loop
    for item in targetComponents[1:]:
        mod = getattr(mod, item)

    elements = dir(mod)

    javaPackages = [el for el in elements 
                    if type(getattr(mod, el)) == JAVA_PACKAGE ]

    javaClasses = [el for el in elements 
                    if type(getattr(mod, el)) == JAVA_CLASS ]

    javaInterfaces = []
    for cn in javaClasses[:]:   # use a copy of javaClasses, we'll be deleting
        if java.lang.Class.isInterface(getattr(mod, cn)):
            javaInterfaces.append(cn)
            javaClasses.remove(cn)

    return javaPackages, javaInterfaces, javaClasses

#############################################################################
#############################################################################

if __name__ == '__main__':
    main(sys.argv[1])

