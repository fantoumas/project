#
from org.jplot2d.env import InterfaceInfo
from org.jplot2d.axtype import *
from org.jplot2d.data import *
from org.jplot2d.element import *
from org.jplot2d.element.AxisPosition import *
from org.jplot2d.element.XYGraph.ChartType import *
from org.jplot2d.layout import *
from org.jplot2d.sizing import *
from org.jplot2d.transform.TransformType import *
from org.jplot2d.util import *

from java.awt import Color
from java.awt.Color import *
from java.awt import Paint
from java.awt.geom import Dimension2D
from java.awt.geom import Point2D

import jarray


jplot2d_default_element_factory = ElementFactory.getInstance()

def jplot2d_set_prop(iinfo, obj, name, v):
#   print name, '=', v
    if isinstance(v, tuple):
        argType = iinfo.getPropWriteMethodType(name)
        if argType == Dimension2D:
            v = DoubleDimension2D(v[0], v[1])
        elif argType == Point2D:
            v = Point2D.Double(v[0], v[1])
        elif argType == Range:
            v = Range.Double(v[0], v[1])
        elif argType == Paint and len(v) == 3:
            v = Color(*v)
    setattr(obj, name, v)

def plot(*args, **kwargs):
    p = jplot2d_default_element_factory.createPlot()
    
    plotinfo = InterfaceInfo.loadInterfaceInfo(Plot)
    return p

def subplot(*args, **kwargs):
    p = jplot2d_default_element_factory.createSubplot()
    
    plotinfo = InterfaceInfo.loadInterfaceInfo(Plot)
    return p

def title(text, *args, **kwargs):
    title = jplot2d_default_element_factory.createTitle(text)
    
    iinfo = InterfaceInfo.loadInterfaceInfo(Title)
    return title


def axis(*args, **kwargs):
    return axes(1, *args, **kwargs)[0]

def axes(n, *args, **kwargs):
    axes = jplot2d_default_element_factory.createAxes(n)

    axisinfo = InterfaceInfo.loadInterfaceInfo(Axis)
    tminfo = InterfaceInfo.loadInterfaceInfo(AxisTickManager)
    txfinfo = InterfaceInfo.loadInterfaceInfo(AxisTransform)
    return axes

def layer(*args, **kwargs):
    layer = jplot2d_default_element_factory.createLayer()
    
    iinfo = InterfaceInfo.loadInterfaceInfo(Layer)
    for arg in args:
        if isinstance(arg, Graph):
            layer.addGraph(arg)
        else:
            raise TypeError, "Cannot add " + str(type(arg)) + " to layer."

    return layer


def xygraph(*args, **kwargs):
    arglist = []
    for arg in args:
        if type(arg) == list or type(arg) == tuple:
            arglist.append(jarray.array(arg, 'd'))
        else:
            arglist.append(arg)

    graph = jplot2d_default_element_factory.createXYGraph(*arglist);
        
    ginfo = InterfaceInfo.loadInterfaceInfo(XYGraph)
    return graph


def imagegraph(*args, **kwargs):
    graph = jplot2d_default_element_factory.createImageGraph(*args)

    ginfo = InterfaceInfo.loadInterfaceInfo(ImageGraph)
    return graph


def rgbimagegraph(*args, **kwargs):
    graph = jplot2d_default_element_factory.createRGBImageGraph(*args);
    
    ginfo = InterfaceInfo.loadInterfaceInfo(RGBImageGraph)
    return graph


def hlineannotation(y, *args, **kwargs):
    ann = jplot2d_default_element_factory.createHLineAnnotation(y)
        
    anninfo = InterfaceInfo.loadInterfaceInfo(HLineAnnotation)
    return ann
 
def vlineannotation(x, *args, **kwargs):
    ann = jplot2d_default_element_factory.createVLineAnnotation(x)
        
    anninfo = InterfaceInfo.loadInterfaceInfo(VLineAnnotation)
    return ann
 
def hstripannotation(start, end, *args, **kwargs):
    ann = jplot2d_default_element_factory.createHStripAnnotation(start, end)
        
    anninfo = InterfaceInfo.loadInterfaceInfo(HStripAnnotation)
    return ann
 
def vstripannotation(start, end, *args, **kwargs):
    ann = jplot2d_default_element_factory.createVStripAnnotation(start, end)
        
    anninfo = InterfaceInfo.loadInterfaceInfo(VStripAnnotation)
    return ann
 
def rectangleannotation(x1, x2, y1, y2, *args, **kwargs):
    ann = jplot2d_default_element_factory.createRectangleAnnotation(x1, x2, y1, y2)
        
    anninfo = InterfaceInfo.loadInterfaceInfo(RectangleAnnotation)
    return ann
 
def symbolannotation(*args, **kwargs):
    ann = jplot2d_default_element_factory.createSymbolAnnotation(*args)
        
    anninfo = InterfaceInfo.loadInterfaceInfo(SymbolAnnotation)
    return ann

def stroke(width, dash=None):
    return jplot2d_default_element_factory.createStroke(width, dash)



# set property for the given obj
def setp(obj, *args, **kwargs):
    if isinstance(obj, Legend):
        iinfo = InterfaceInfo.loadInterfaceInfo(Legend)
