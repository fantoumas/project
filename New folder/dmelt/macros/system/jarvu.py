###########################################################################
#
#  jarvu  --  A Jython program to look inside a jar file,
#             output the names of all packages, interfaces and classes
#
###########################################################################

import sys

from java.util.jar import JarFile, JarEntry

###########################################################################

#TARGET = "C:/apps/jardump/foreign.jar"
TARGET = "C:/Windows/Desktop/dczip.jar"

###########################################################################

def main(args):
    sys.path.append(TARGET)

    mainClass = None  # replaced with an actual value if the jar
                      # header has a Main-Class: entry

    jf = JarFile(TARGET)

    mf = jf.getManifest()
    print "MANIFEST"
    print "--------"
    mfattr = mf.getMainAttributes()
    for mfKey in mfattr.keySet():
        print " %24.24s : %s" % (mfKey, mfattr.getValue(mfKey))
        if str(mfKey) == 'Main-Class':
            mainClassName = mfattr.getValue('Main-Class')
            mainClass = '%s.class' % mainClass
#            print "main class: %s" % mainClassName
    print " "
    if not mainClass:
        print "No Main-Class specified..."

    print " "
    mcm = None
    for entry in jf.entries():
        if entry.name == mainClass:
            print "found mainClass: %s" % entry.name
            # import the main class as a module
            mcm = __import__(mainClass, globals(), locals())
            print "imported mainClass: %s" % mainClass
        elif entry.name.endswith('.class'):
            fsPathToClass = entry.name.replace('.class', '')
            dottedPackagePathToClass = fsPathToClass.replace('/', '.')
            auxClass = dottedPackagePathToClass.split('.')[-1]
            try:
                aux = __import__(dottedPackagePathToClass, globals(),
locals())
                print dottedPackagePathToClass
            except ImportError:
#                print "unable to import %s" % dottedPackagePathToClass
                pass

    print " "

    if mcm:
        print dir(mcm)

###########################################################################
###########################################################################

if __name__ == '__main__':
    main(sys.argv[1:])


