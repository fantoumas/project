import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.net.*;


public class app extends JFrame implements ActionListener
{
  private JTextArea jta;
  private JMenuItem jmiOpen, jmiClose, jmiQuit;

  public app()
  {
    super("Swing application");

    Container contentPane = getContentPane();
    jta = new JTextArea();
		jmiOpen = new JMenuItem("Open");
		jmiQuit = new JMenuItem("Quit");

		JMenuBar jmb = new JMenuBar();
		setJMenuBar(jmb);

		JMenu jfile = new JMenu("File");
		jfile.add(jmiOpen);
		jfile.add(jmiQuit);

		JMenu jedit = new JMenu("Edit");

		jmb.add(jfile);
		jmb.add(jedit);

		getContentPane().setLayout(new BorderLayout());
		getContentPane().add(jta, BorderLayout.CENTER);


    jmiQuit.addActionListener(this);
  }

    public static void main(String args[])
    {
        app f = new app();

        f.setSize(400, 300);
        f.setVisible(true);

        f.setDefaultCloseOperation(DISPOSE_ON_CLOSE);

        f.addWindowListener(new WindowAdapter() {
            public void windowClosed(WindowEvent e) {
                System.exit(0);
            }
        });

    }

 

        public void actionPerformed(ActionEvent e){

         if (e.getSource() == jmiQuit) {
            System.exit(0);
           }

	}

}
