import org.jgap.InvalidConfigurationException;
import org.jgap.gp.impl.GPConfiguration;

import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;

/**
 * Created by Christina on 27/6/2016.
 */
public class Screen extends JPanel{

    private static int text_length = 10;
    private static int length = 100;
    private static int height = 30;
    
    private String data_file;

    String createMenuBar(JFrame w)
    {
        JMenuBar menubar = new JMenuBar();
        JMenu file = new JMenu("File");
        JMenuItem dataMenuItem = new JMenuItem("Open Data");
        dataMenuItem.setMnemonic(KeyEvent.VK_E);
        JMenuItem aboutMenuItem = new JMenuItem("About");
        aboutMenuItem.setMnemonic(KeyEvent.VK_E);
        JMenuItem exitMenuItem = new JMenuItem("Exit");
        exitMenuItem.setMnemonic(KeyEvent.VK_E);
        exitMenuItem.setToolTipText("Exit application");
        exitMenuItem.addActionListener(event -> System.exit(1));
        dataMenuItem.addActionListener(e -> {
           data_file = showFileChooserDemo(w);
            try {
                GPConfiguration conf = new GPConfiguration();
                try {
                    MathProblem fx = new MathProblem(conf);
                    fx.start(data_file);
                } catch (Exception e1) {
                    e1.printStackTrace();
                }
            } catch (InvalidConfigurationException e1) {
                e1.printStackTrace();
            }

        });
        aboutMenuItem.addActionListener(e -> {
        });
        file.add(dataMenuItem);
        file.add(aboutMenuItem);
        file.add(exitMenuItem);
        menubar.add(file);
        w.setJMenuBar(menubar);
        setupGUI(w);
        return data_file;
    }

    private void setupGUI(JFrame w) {
        Container pane = w.getContentPane();
        Insets insets = pane.getInsets();
        pane.setLayout (null);
        // construct the Label component
        Label evolutions = new Label("Evolutions");  
        Label initDepth = new Label("Max init depth"); 
        Label crossoverDepth = new Label("Crossover depth");
        // construct the TextField component
        TextField inDepth = new TextField("0", text_length);
        TextField evolve = new TextField("0", text_length);
        TextField crosDepth = new TextField("0", text_length);
        initDepth.setPreferredSize(new Dimension(length , height));
        evolutions.setPreferredSize(new Dimension(length ,height));
        evolve.setPreferredSize(new Dimension(length ,text_length));
        inDepth.setPreferredSize(new Dimension(length , text_length));
        inDepth.setEditable(true);
        evolve.setEditable(true);
        JCheckBox chkSin = new JCheckBox("Sin");
        chkSin.setHorizontalTextPosition(SwingConstants.LEFT);
        chkSin.setMnemonic(KeyEvent.VK_E);
        chkSin.addActionListener(e -> {
                });
        pane.add (initDepth);
        initDepth.setBounds (insets.left + text_length, insets.top + text_length, initDepth.getPreferredSize().width, initDepth.getPreferredSize().height);
        pane.add (inDepth);
        inDepth.setBounds (initDepth.getX() + initDepth.getWidth() + text_length, insets.top + text_length, inDepth.getPreferredSize().width, inDepth.getPreferredSize().height);
        pane.add (evolutions);
        evolutions.setBounds (insets.left + text_length,initDepth.getY()+ initDepth.getHeight(), evolutions.getPreferredSize().width, evolutions.getPreferredSize().height);
        pane.add (evolve);
        evolve.setBounds (evolutions.getX() + evolutions.getWidth() +text_length , initDepth.getY()+ initDepth.getHeight(), evolve.getPreferredSize().width, evolve.getPreferredSize().height);
        pane.add (crossoverDepth);
        crossoverDepth.setBounds(insets.left + text_length, evolutions.getY() + evolutions.getHeight(), crossoverDepth.getPreferredSize().width, crossoverDepth.getPreferredSize().height);
        pane.add (crosDepth);
        crosDepth.setBounds(crossoverDepth.getX() + evolutions.getWidth() +text_length , evolutions.getY() + evolutions.getHeight(), crosDepth.getPreferredSize().width, crosDepth.getPreferredSize().height);
        pane.add (chkSin);
        chkSin.setBounds(insets.left + text_length, crossoverDepth.getY() + crosDepth.getHeight(), chkSin.getPreferredSize().width, chkSin.getPreferredSize().height);
        setVisible(true);

    }

    private String showFileChooserDemo(JFrame w) {
        final JFileChooser  fileDialog = new JFileChooser();
        int returnVal = fileDialog.showOpenDialog(w);
        if (returnVal == JFileChooser.APPROVE_OPTION) {
            java.io.File file = fileDialog.getSelectedFile();
            return  file.getName();
        }
        else return null;
    }
}
