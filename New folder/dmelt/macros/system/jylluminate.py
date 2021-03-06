##############################################################################
#
#  jylluminate.py
#
#  There was a question on the Jython mailing list in early December 2005
#  from Bill Woodward about how to get info about interfaces, methods,
#  superclasses, and attribute info from a Java object.
#  This module provides the ability to address that question.
#
#  This file contains source code with the following characteristics:
#     context provided
#     attribution provided
#     docstrings (module and function) provided
#     reasonably named functions provided
#     example usage provided
#     absence of gratuitous black-magic :-)
#     test runs have been executed
#
#  Kip Lehman
#  Dec 10 2005
#
__author__  = 'Kip Lehman "<kipster-t@earthlink.net>"'
__version__ = 1.1

##############################################################################

"""
    Inspired by a Dec 2005 Jython users mailing list question asked
    by Bill Woodward and responses from Helio R. Zwi and Jeff Emanuel,
    this mini-module contains functions to illuminate instances of a
    Java object.  Having dug up other useful perspectives provided by
    Rick Hightower, I've put together a set of functions that can help
    in illuminating the swamp of what lies beneath a Java object's surface.
    Using the functions defined here, one can:

      1) Find out the instance's lineage, ie., what superclasses the
         object inherits from or what interfaces the object implements.

           lineage(javaObject)

      2) Find out what methods that the class defines and what interfaces
         are implemented (excluding superclasses).

           methods(javaObject)

      3) Find rudimentary information about simple data attributes
         held by the instance.

           fields(javaObject)

      4) Find out what the method signatures are for the object

           signatures(javaObject)

    The code uses syntax legal for Jython 2.1 and 2.2.
    No attempt has been made to prove that this works for every
    Java object in the Milky Way galaxy.  The functions here are
    not optimized for elegance, non-repetitiveness or performance.
    This is meant to be _an_ example of how to peer into a Java object
    instance from Jython, I make no claims that it is the _only_ or
    the _best_ way!  I did add a signatures function using the declaredMethods
    method that wasn't mentioned in the first version of this module.

"""
##############################################################################

__all__ = ['lineage', 'methods', 'fields', 'signatures']

import org.python.core
import re

JAVA_METHOD = org.python.core.PyReflectedFunction
BASE_OBJECT = 'java.lang.Object'
BASE_OBJECT_METHODS = ['clone', 'equals', 'finalize', 'getClass',
                       'hash', 'hashCode', 'notify', 'notifyAll',
                       'registerNatives', 'toString', 'wait']

#
# Yes, I am aware that 'hash' is not a method defined by Object.
# However, in my estimation, showing that method for a subclass
# or an interface is not a net value-add.
# Hence, I stuck it in the B_O_M list.
# YMMV...
#

STD_INDENT = ' ' * 4

TYPE_ADDR_PAT = re.compile(r'\w+[\.\w+]+\w+ at \d+')

VIZSYM = {'public'    : '+',
          'protected' : '-',
          'private'   : '*'}

##############################################################################

def lineage(javaObject):
    """
        Given an instance of a Java object, assemble a list of information
        about the object, such as the class name, its superclasses and what
        interface(s) it implements.
        Join the elements of the list with a newline and return the
        string to caller such that they can either print the string or
        percolate the string to a higher level caller.

        Example:

        >>> what = lineage(java.util.String("Hello World"))
        >>> print what

        class: java.lang.String

        superclass hierarchy (excluding Object):
            java.io.Serializable                   (interface)
                java.lang.Comparable               (interface)
                    java.lang.CharSequence         (interface)
                        java.lang.String

        methods defined in interfaces/implemented in superclasses (minus Object):
            java.lang.Comparable
                compareTo

            java.lang.CharSequence
                charAt
                length
                subSequence
                toString
    """
    info = []

    objectClassName  = javaObject.__class__.__name__
    objectSuperClass = javaObject.class.superclass
    superClasses     = javaObject.__class__.__bases__
    interfaces       = javaObject.class.interfaces
    definedMethods   = javaObject.class.methods
    md = _buildMethodDict(javaObject.class)

    info.append('')
    info.append('class: %s' % objectClassName)
    info.append('')
    info.append('superclass hierarchy (excluding Object):')

    hierarchy = []

    ix = 1
    ofmt = "%-56.56s %s"
    for sc in superClasses:
        scName = '%s' % sc
        if scName == BASE_OBJECT:
            continue
        indent = STD_INDENT * ix
        icn = "%s%s" % (indent, scName)
        isIfc = sc in interfaces
        if isIfc:
            ifcInfo = "(interface)"
            hierarchy.append((sc, scName, 'interface'))
        else:
            ifcInfo = ""
            hierarchy.append((sc, scName, 'class'))
        info.append(ofmt % (icn, ifcInfo))
        ix += 1
    info.append('%s%s' % (STD_INDENT * ix, objectClassName))

    info.append('')
    info.append('methods defined in interfaces/implemented in superclasses (minus Object):')
    mentioned = BASE_OBJECT_METHODS[:]

    for superClass, name, javaType in hierarchy:
        if javaType == 'interface':
            ifc = [ifc for ifc in interfaces if str(ifc) == name][0]
            meths = dir(ifc)
            if not meths:
                continue
            info.append('%s%-36.36s  (interface)' % (STD_INDENT, ifc))
            for method in meths:
                if method not in mentioned:
                    info.append('%s%s' % (STD_INDENT * 2, method))
                    mentioned.append(method)
            info.append('')
        else:
            if md.has_key(name):
                info.append('%s%s' % (STD_INDENT, name))
                meths = []
                meths = md[name]
                meths.sort()
                for methodName in meths:
                    info.append('%s%s' % (STD_INDENT*2, methodName))
                info.append('')

    return '\n'.join(info)

##############################################################################

def signatures(javaObject):
    """
        Show all method signatures for the given Java object.
    """
    signatureInfo = []
    objectClassName  = javaObject.__class__.__name__

    declaredMethods = javaObject.__class__.declaredMethods.get()
    for methObj in declaredMethods:
        mts = '%s' % methObj
        mna = mts.split()[-1]
        methodSig = mna.replace(objectClassName, '')[1:]
        signatureInfo.append(methodSig)

    return '\n'.join(signatureInfo)

##############################################################################

def methods(javaObject):
    """
        Given an instance of a javaObject, assemble a list of methods
        that are implemented in the javaObject class, specifically
        excluding any methods implemented in superclasses.  Once the
        list of method information is assembled, it is joined with a
        newline character resulting in a printable string.
        The resultant string is returned to the caller to be printed
        or percolated up to a higher level caller.

        Example:

        >>> what = methods(java.util.String("Hello World"))
        >>> print what

        methods implemented by the java.lang.String class
            charAt
            checkBounds
            ...
            trim
            valueOf
    """
    info = []

    objectClass      = javaObject.class
    objectClassName  = javaObject.__class__.__name__
    objectSuperClass = javaObject.class.superclass
    interfaces       = javaObject.class.interfaces
    superClasses     = javaObject.__class__.__bases__
    superMethods     = _superMethods(objectSuperClass)
    attributes       = javaObject.class.__dict__.items()
    meths            = []
    methodExclusions = BASE_OBJECT_METHODS[:]
    for method in superMethods:
        methodExclusions.append(method)

    for ifc in interfaces:
        ifcMethods = dir(ifc)
        for method in ifcMethods:
            methodExclusions.append('%s' % method)

    info.append('')
    info.append('methods implemented by the %s class' % objectClassName)

    for attrName, attrValue in attributes:
        if attrName in methodExclusions:
            continue

        avrep = '%r' % attrValue
        if avrep.find('<java function ') >= 0 and avrep.find('$') < 0:
            meths.append(attrName)
    meths.sort()
    for meth in meths:
        info.append('%s%s' % (STD_INDENT, meth))
    info.append('')

    return '\n'.join(info)

##############################################################################

def fields(javaObject):
    """
        Given an instance of a javaObject, assemble a list
        of attribute name and value strings that represent the
        data attributes held in the javaObject.  Once the list
        of data attribute information is assembled, join the
        elements of the list using a newline and return that
        string back to the caller.  The intent is that the
        caller can print the result or percolate it back to
        a higher level caller.

        Example:

        >>> what = fields(java.lang.String("Hello World!"))
        >>> print what

        The symbol to the left of the separating colon indicates the
        visibility of the field, ' ' for default or unknown, '+' for
        public, '-' for private and '*' for protected.
    """
    info = []
    jc = javaObject.getClass()
    fields = jc.getDeclaredFields()
    for field in fields:
        parts = field.toString().split()
        viz  = parts[0]
        ftyp = parts[-2]
        fullnam = parts[-1]
        fieldName = fullnam.split('.')[-1]
        if fieldName in ['serialVersionUID', 'serialPersistentFields', 
                         'CASE_INSENSITIVE_ORDER']:
            continue
        value = str(getattr(javaObject, fieldName))
        if value.find('<method ') >= 0:
            continue
        #if value.find('java.Foobar@hexnumber') >= 0:
        #   continue
        if VIZSYM.has_key(viz):
            vz = VIZSYM[viz]
        else:
            vz = ' '
        fldInfo = '    %-16s %s: %s' % (fieldName, vz, value)
        info.append(fldInfo)
    info.sort()
    info.insert(0, '\nfields held by the %s object' % jc.__name__)

    return '\n'.join(info)
        
##############################################################################

def dataAttributes(javaObject):
    """
        ****!!!!! deprecated in favor of fields function !!!!!****
        ****      function remains here to cherry pick        ****
        ****      any code helpful in futzing with data types ****

        Given an instance of a javaObject, assemble a list
        of attribute name and value strings that represent the
        data attributes held in the javaObject.  Once the list
        of data attribute information is assembled, join the
        elements of the list using a newline and return that
        string back to the caller.  The intent is that the
        caller can print the result or percolate it back to
        a higher level caller.

        Example:

        >>> what = dataAttributes(java.lang.String("Hello World!"))
        >>> print what
    """
    info = []

    objectClassName  = javaObject.__class__.__name__
    objectSuperClass = javaObject.class.superclass
    interfaces       = javaObject.class.interfaces
    superClasses     = javaObject.__class__.__bases__
    superMethods     = _superMethods(objectSuperClass)
    attributes       = javaObject.class.__dict__.items()
    properties       = []
    methodExclusions = BASE_OBJECT_METHODS[:]
    for method in superMethods:
        methodExclusions.append(method)

    for ifc in interfaces:
        meths = dir(ifc)
        for method in meths:
            methodExclusions.append(method)

    for attrName, attrValue in attributes:
        if attrName in methodExclusions:
            continue
        if attrName in ['serialVersionUID']:
            continue
        av = str(attrValue)
        if av.find('<java function ') >= 0:
            continue
        if av.find('<java constructor') >= 0:
            continue
        if av.find('CASE_INSENSITIVE_ORDER') >= 0:
            continue
        if av.find('serialPersistentFields') >= 0:
            continue
        av = av[1:-1].replace('reflected field ', '')

        viz = ' '
        if av.find('public') >= 0:
            av = av.replace('public ', '')
            viz = '+'
        elif av.find('private') >= 0:
            av = av.replace('private ', '')
            viz = '-'
        elif av.find('protected') >= 0:
            av = av.replace('protected ', '')
            viz = '*'
        av = av.replace('static ', '')
        av = av.replace('final ', '')

        av = TYPE_ADDR_PAT.sub('', av)
        av = re.sub(r'type: .*', '', av).strip()

        if av in ['boolean', 'int', 'long', 'char',  'char[]',
                  'beanProperty bytes',
                  'java.lang.String']:
            value = getattr(javaObject, attrName)
            properties.append('%-16s %s: %s' % (attrName, viz, value))
        else:
            properties.append('%-16s %s: %s' % (attrName, viz, av))

    properties.sort()
    properties.append('%-16s :  %s' % ('toString()', javaObject.toString()))
    if properties:
        info.append('')
        info.append('instance properties (typically data values or delegate instances):')
    for prop in properties:
        info.append('%s%s' % (STD_INDENT, prop))

    return '\n'.join(info)

##############################################################################

def _buildMethodDict(objectClass):
    """
        An internal convenience function that takes an objectClass
        as an argument and returns a dict keyed by class name where
        each class name has an associated list of methods implemented
        by any superclass of the objectClass.
    """
    md = {}
    for method in objectClass.methods:
        temp = '%s' % method
        if temp.find(' throws ') > 0:
            temp = temp.split(' throws ')[0]
        temp = temp.split(None)[-1]
        openingParen = temp.find('(')
        methodName = temp[:openingParen]
        if methodName.find('java.lang.Object.') < 0:
            lastDot = methodName.rfind('.')
            if lastDot:
                className = methodName[:lastDot]
                shortName = methodName[lastDot+1:]
                if not md.has_key(className):
                    md[className] = []
                md[className].append(shortName)
    return md

##############################################################################

def _superMethods(objectSuperClass):

    """
        An internal convenience function that takes an objectSuperClass
        as an argument and returns a list of methods implemented by
        that superClass.
    """
    superMethods = []
    superClassName = objectSuperClass.__name__
    objectSuperClassName = objectSuperClass.__name__
    if superClassName != BASE_OBJECT:
        scStuff = objectSuperClass.__dict__.items()
        guts = [(name, value) for name, value in scStuff]
        guts.sort()
        for name, value in guts:
            if type(value) == JAVA_METHOD and name.count('$') < 1:
                superMethods.append(name)
    superMethods.sort()
    return superMethods

##############################################################################

def test():
    """
        Show example usage of the three functions defined in this module
        for a number of different Java objects.

        Yes, I know, this isn't the rigorous test suite you may
        have expected.  Feel free to "fix" the situation to your taste.
    """
    testString()
    testHashtable()
    testProperties()
    testHashMap()
    testLinkedHashMap()
    testVector()
    testStringBuffer()

##############################################################################

def testString():
    from java.lang import String
    print "-" * 75
    print " "
    print "a java.lang.String -> 'Hello World!'"

    greeting = String("Hello World!")
    print lineage(greeting)
    print methods(greeting)
    print fields(greeting)

##############################################################################

def testHashtable():
    from java.util import Hashtable
    print "-" * 75
    print " "
    print "a java.util.Hashtable instance -> {'Bora Bora' : 'nautical', 'Kenai Peninsula' : 'wildlife'}"
    props = Hashtable()
    props.put("Bora Bora"  , "nautical")
    props.put("Kenai Peninsula", "wildlife")

    print lineage(props)
    print methods(props)
    print fields(props)

##############################################################################

def testProperties():
    from java.util import Properties

    print "-" * 75
    print " "
    print "a java.util.Properties instance -> {'candy bar' : 'Snickers', 'steak sauce' : 'A1'}"
    props = Properties()
    props.put("candy bar"  , "Snickers")
    props.put("steak sauce", "A1")

    print lineage(props)
    print methods(props)
    print fields(props)

##############################################################################

def testHashMap():
    from java.util import HashMap
    print "-" * 75
    print " "
    print "a java.util.HashMap instance -> {'candy bar' : '3 Musketeers!', 'steak sauce' : 'KC Masterpiece'}"
    map = HashMap()
    map.put('candy bar',   '3 Musketeers')
    map.put('steak sauce', 'KC Masterpiece')

    print lineage(map)
    print methods(map)
    print fields(map)

##############################################################################

def testLinkedHashMap():
    from java.util import LinkedHashMap
    print "-" * 75
    print " "
    print "a java.util.LinkedHashMap instance -> {'candy bar' : 'Oh Henry!', 'steak sauce' : 57}"
    od = LinkedHashMap()
    od.put("candy bar"  , "Oh Henry!")
    od.put("steak sauce", 57)

    print lineage(od)
    print methods(od)
    print fields(od)

##############################################################################

def testVector():
    from java.util import Vector
    print "-" * 75
    print " "
    print "a java.util.Vector -> [1, 2, 4, 9]"
    viktor = Vector()
    viktor.add(1)
    viktor.add(2)
    viktor.add(4)
    viktor.add(9)

    print lineage(viktor)
    print methods(viktor)
    print fields(viktor)

##############################################################################

def testStringBuffer():
    from java.lang import StringBuffer
    print "-" * 75
    print " "
    print "a java.lang.StringBuffer -> 'Adios muchacho!'"
    goodbye = StringBuffer('Adios muchacho!')
    print lineage(goodbye)
    print methods(goodbye)
    print fields(goodbye)

##############################################################################
##############################################################################

if __name__ == '__main__':
    test()

