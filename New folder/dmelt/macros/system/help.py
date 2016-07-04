from jehep.ui import SetEnv
from jehep.ui import Editor 
from javax.swing import JButton, JDialog, JLabel, JPanel, JScrollPane, JTextArea
from java.awt import BorderLayout
from java.awt import Color
from java.awt.event import ActionListener, KeyEvent, KeyListener, MouseListener

frame =JDialog();
topPanel = JPanel();
lowerPanel = JPanel();
jDescription = JTextArea(80, 100);
helpFile=SetEnv.DirPath+SetEnv.fSep+"Docs"+SetEnv.fSep+"HelpJythonShell.txt";
text=SetEnv.readFile(helpFile);
jDescription.setText(text);

jDescription.setCaretPosition(0);
# jDescription.setBorder(BorderFactory.createEmptyBorder(2, 2, 2, 2));
jDescription.setEditable(0)


def exitme(event):
       frame.dispose()    

jB2 = JButton("Exit", actionPerformed=exitme)

 
lowerPanel.add(jB2);
topPanel.setLayout(BorderLayout());

# comments
jScrollPane1 = JScrollPane();
jScrollPane1.getViewport().add( jDescription );
topPanel.add(jScrollPane1,BorderLayout.CENTER);


jDescription.setLineWrap(1);
jDescription.setWrapStyleWord(1);
jDescription.setCaretColor(Color.red);
frame.add( topPanel,  BorderLayout.CENTER );
frame.add( lowerPanel, BorderLayout.SOUTH );


bounds = view.getBounds()
ww = bounds.width
hh=  bounds.height
xx = bounds.x
yy = bounds.y
  
frame.setLocation(xx+(int)(0.4*ww), yy+(int)(0.1*hh))
frame.pack()
frame.setSize( (int)(0.5*ww),(int)(0.8*hh) );
frame.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE)
frame.setVisible(1)
