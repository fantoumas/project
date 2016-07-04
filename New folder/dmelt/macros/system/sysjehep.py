# first import
import sys
import os
from jehep.ui import SetEnv
from jehep.ui import Editor 
from net.hep.graphics.ObjectBrowser.Reflector import ObjectBrowser
# mimic jEdit
textArea=Editor.get() 
view=SetEnv.win

# file separator
fSep=SetEnv.fSep

# system directory
SystemDir=SetEnv.DirPath
module_dir1=os.path.join(SetEnv.DirPath,'macros','system')
module_dir2=os.path.join(SetEnv.DirPath,'macros','user')
module_dir3=os.path.join(SetEnv.DirPath,'macros','shplot')
module_dir4=os.path.join(SetEnv.DirPath,'python','packages')

# add to system path user directories
sys.path.insert(0,module_dir1)
sys.path.insert(0,module_dir2)
sys.path.insert(0,module_dir3)
sys.path.insert(0,module_dir4)

# append current dir
sys.path.append(".")

# project directory
# sys.path.append(SetEnv.ProjDir) 
# Doc name 
DocName=Editor.DocName()

# Doc dir
DocDir=Editor.DocDir()

# Project directory
ProjDir=SetEnv.ProjDir

# class path 
ClassPath=SetEnv.ClassPath

# Doc style
DocStyle=Editor.DocStyle()

#  DocMasterName
DocMasterName=Editor.DocMasterName()
DocMasterName=DocMasterName.strip()
if len(DocMasterName)<1: 
                DocMasterName="Default"

# directory for dictionaries
DicDir=SetEnv.DicDir;


DocMasterNameShort=Editor.DocMasterNameShort();
DocMasterNameShort=DocMasterNameShort.strip()
if len(DocMasterNameShort)<1: 
                            DocMasterNameShort="Default";


UserMacrosDir=SetEnv.DirPath+SetEnv.fSep+"macros" + SetEnv.fSep+"user"; 
SystemMacrosDir=SetEnv.DirPath+SetEnv.fSep+"macros" + SetEnv.fSep+"system";


############## UTILS macros
from  webutils import wget
