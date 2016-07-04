import sys, math
from java.util import *
from jhplot import HTable


file=SystemDir+fSep+"macros"+fSep+"system"
file=file+fSep+"PDG"+fSep+"mass_width_2004.csv"


# vector with names
v1 = Vector()
v1.add("Name")
v1.add("Mass")
v1.add("Err-")
v1.add("Err+")
v1.add("Width")
v1.add("Err-")
v1.add("Err+")
v1.add("I")
v1.add("J")
v1.add("ID")
v1.add("charge")
v1.add("quark")


# data vector
v2 =Vector()



############## Now open file for reading (example)
ifile = open (file,'r')
lines = ifile.readlines()      # read file into list of lines
ifile.close()
# go through each line and split line into x and y columns:
mass = [];  mass_up = []; mass_down=[];   # store data pairs in two lists x and y
width = []; width_up = []; width_down=[];
I=[]  # isospin
G=[] # G parity
J=[] # J total spin
P=[] # P space parity
C=[] #  C charge conjugation parity
A=[] # A: antiparticle=|=particle flag
ID=[] #  PDG particle ID number
charge=[] # charge
R=[] #  Number of baryon stars - used only on baryons.
S=[] # particle status
name=[] # particle name
quark=[] # Quark contents  
for line in lines:
     if  (line[0]=="*" or line[0]=="#"): continue  
     mass,mass_up,mass_down,width,width_up,\
     width_down,I,G,J,P,C,A,ID,charge,R,S,name,quark =line.split(",")
     quark = quark.replace('\n', '')
     vv = Vector(12)
     vv.add(name); 
     vv.add(mass); vv.add(mass_down); vv.add(mass_up);  
     vv.add(width);  vv.add(width_down); vv.add(width_up);
     vv.add(I)
     vv.add(J); vv.add(ID); 
     vv.add(charge); vv.add(quark)
     v2.add(vv)
    

b=HTable("PDG 2004",v1,v2);
