from jehep.ui import SetEnv
from jehep.ui import Editor 
from javax.swing import JButton, JDialog, JLabel, JPanel, JScrollPane, JTextArea
from java.awt import BorderLayout
from java.awt import Color
from java.awt.event import ActionListener, KeyEvent, KeyListener, MouseListener
from java.lang import Thread


help_file=SystemDir+fSep+"Docs"+fSep+"license.txt";
print("Open  a test  file  and wait for 3 sec"+help_file);
view.open( help_file, 0  );
Thread.sleep(3000);
  
print("Select the text and wait for 3 sec");
view.selectAll();
Thread.sleep(3000); 

print("Remove the text and wait for 3 sec");
mydoc=view.getText();
view.setText("");
Thread.sleep(3000); 

print("Type some text and wait for 3 sec");
view.setText("This is some sample text");
Thread.sleep(3000); 

print("Insert some text and wait for 3 sec");
cc=view.getCaretPosition();
view.insertString("Some inserted text at position 4", 4);
view.insertString("Again some text is  inserted at position 10", 10);
Thread.sleep(3000); 

print("Put the removed text back, go to line 4");
view.setText(mydoc);
view.goToLine(4);
cc=view.getCaretPosition();
Thread.sleep(3000);

print("Insert some text at line 20");
view.insertString("This text was inserted", cc);
view.insertString("", cc); 
Thread.sleep(3000); 


print("set caret and select, then  wait for 3 sec");
view.setCaretPos(50);
view.select(0,20);
Thread.sleep(3000);


print("replace \"t\" by \"m\", then  wait for 3 sec"); 
ss=view.getText();
ss=ss.replace("t","m");
view.setText(ss);
Thread.sleep(3000);


dir();
print("");
print("Above is the list of jeHEP imported classes");

print("--This macro is located here:"+SystemDir+
            fSep+"macros"+fSep+"system"+fSep+"test.py");

print("--The user can put any macro in:"+SystemDir+
            fSep+"macros"+fSep+"user"+fSep);

