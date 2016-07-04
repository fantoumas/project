import compileall
import re
import os


jhepwork='.'
if os.environ['JHEPWORK']:
        jhepwork=os.environ['JHEPWORK']

print jhepwork 
DIR=jhepwork+'/jehep/macros/shplot'
compileall.compile_dir(DIR, rx=re.compile('/[.]svn'), force=True)

ir=[]
for  f  in os.listdir(DIR):
         if not f.endswith(".py"): continue 
         if f.startswith("Compile"):  continue
         if f.endswith("_test.py"):   continue
         if f.startswith("shplot."):  continue

         print 'process:'+f
         f=f.replace('.py','')
         ir.append(f)      

# make include file
myFile = open("shplot.py","w")
myFile.write('""" Main shplot module for DataMelt scripting. @ S.Chekanov (ANL) """')
myFile.write('\n')
myFile.write('\n')
myFile.write('\n')
for i in range(len(ir)):
         myFile.write('from '+ir[i]+' import '+ir[i]+'\n')
myFile.close()
