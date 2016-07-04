#!C:/Python/bin/python.exe

import sys, os
import zipfile


target = "C:/j2sdk1.4.2_07/servlet.jar"
target = "D:/archive/java/dczip.jar"

exists = os.path.exists(target)
print "target exists: %s" % exists

iz = zipfile.is_zipfile(target)
print "target is zip: %s" % iz


zf = zipfile.ZipFile(target)

for name in zf.namelist():	
	print name

zf.printdir()
