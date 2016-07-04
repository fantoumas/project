# create HTML files from the example directory
# 
import shutil, os

OUTFILE='examples.html'
DIR="../../examples/"
HTML_DIR="./examples"
EXTEN='.py'
print "dir =", DIR
print "extension =", EXTEN
if os.path.exists( HTML_DIR ) :
              print HTML_DIR, ' exists' 
else:
              os.mkdir( HTML_DIR )

print ' '

# walk 
def walk( dir, process):
    '''walk a directory tree'''
    for f in os.listdir( dir ):
        fullpath = os.path.join( dir, f)
        if os.path.isdir( fullpath ) and not os.path.islink( fullpath ):
            walk( fullpath, process )
        if os.path.isfile( fullpath ):
            if fullpath.lower().endswith('.py'):
                files.append(f)
                # print fullpath 
                # copy to HTML directory
                shutil.copyfile(fullpath,HTML_DIR+'/'+f)


files=[]
walk(DIR,files)


# remove duplicates
d = {}
for x in files: d[x]=x
List = d.values()

# sort
List.sort()

fout=open(OUTFILE, 'w')
fout.write( '<html> <title> DataMelt examples </title> <body>\n' )
fout.write( '<h2>DataMelt examples</h2>')
fout.write( '<td valign="top" align="left" width="100%">') 
fout.write( '<ol>')

for i in range(len(List)):
       xfile=HTML_DIR+'/'+List[i] 
       print 'converting:  '+xfile
       os.system('run_py2html.sh '+xfile)

       f=open(xfile, 'r')
       info=f.readline()
       info=info.strip()
       info=info.replace('\n','')
       info=info.replace('#','')
       info=info.strip()
       new='<li><a href="'+xfile+'.html'+'">'+info+'</a></li>\n'
       fout.write( new ) 
       if os.path.exists(xfile):
                  os.remove(xfile)

fout.write( '</ol></td>')

footer='<hr /><font size="-1">(C) S.Chekanov: email:<a href="mailto:chekanov@mail.desy.de">chekanov@mail.desy.de</a> </font>'

fout.write( footer)
fout.write( '</body></html>')
fout.close()
print 'output file:'+OUTFILE 
