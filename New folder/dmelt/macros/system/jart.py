#!C:/python24/bin/python.exe

#################################################################################
#
#   jart -- jar tell, find out what packages and classes are in a jar file
#
USAGE = """
Usage: jart.py <jarFile> | <directoryPath>
"""
#################################################################################

import sys, os
import zipfile

#################################################################################

def main(args):

    if not args:
        sys.stderr.write(USAGE)
        sys.exit(1)

    target = args[0]
    if not os.path.exists(target):
        sys.stderr.write('ERROR: jar target: %s not found\n' % target)
        sys.exit(1)

    if os.path.isfile(target):
        if not zipfile.is_zipfile(target):
            sys.stderr.write('ERROR: jar target: %s is not a zipfile\n' % target)
            sys.exit(1)
        processJarFile(target)

    elif os.path.isdir(target):   # look for jar files under this directory root
        allFiles = ['%s/%s' % (target, fn) for fn in os.listdir(target) 
                    if os.path.isfile('%s/%s' % (target, fn))]
        jarFiles = [fqp for fqp in allFiles 
                    if fqp.endswith('.jar') and zipfile.is_zipfile(fqp)]
        for jarFile in jarFiles:
            processJarFile(jarFile)

#################################################################################

def processJarFile(jarFileName):
    print ""
    print jarFileName

    package = None
    classes = []

    zf = zipfile.ZipFile(jarFileName)
    for ze in zf.infolist():
        item = ze.filename
        if item.endswith('/'):
            if package and classes:
                dumpInfo(package, classes)
                classes = []
            package = item[:-1].replace('/', '.')
        elif item.endswith('.class'):
            className = item[item.rfind('/')+1:].replace('.class', '')
            classes.append(className)
    zf.close()

    dumpInfo(package, classes)

#################################################################################

def dumpInfo(package, classes):
    if package and classes:
        print "    %s" % package
        for className in classes:
            print "        %s" % className
        print " "

#################################################################################
#################################################################################

if __name__ == '__main__':
    main(sys.argv[1:])

