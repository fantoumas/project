import org.jgap.InvalidConfigurationException;
import org.jgap.gp.impl.GPConfiguration;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.text.NumberFormat;
import java.text.ParseException;

/**
 * Created by Christina on 27/6/2016.
 */
public class Screen extends JPanel{

    private int[] counter = new int[5];
    private static int DEFAULT_AMOUNT = 0;
    private static int text_length = 10;
    private static int length = 100;
    private static int height = 30;
    private String data_file;
    private static int MIN_GENERATIONS = 100;
    private static int MAX_GENERATIONS = 10000;
    private static int MAX_CROSSOVER = 8;
    private static int MIN_CROSSOVER = 4;
    private static int MIN_INIT = 2;
    private static int MAX_INIT = 6;
    private NumberFormat integerFormat;
    private JTextField crosDepth;
    private JTextField evolve;
    private JTextField inDepth;
    private MyVerifier verifier = new MyVerifier();


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
//                    fx.start(data_file);
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
        setUpFormats();
        Container pane = w.getContentPane();
        Insets insets = pane.getInsets();
        pane.setLayout (null);
        // construct the Label component
        JButton submit = new JButton();
        JLabel evolutions = new JLabel("Evolutions");
        JLabel initDepth = new JLabel("Max init depth");
        JLabel crossoverDepth = new JLabel("Crossover depth");
        JLabel Functions = new JLabel("Functions:");

        initDepth.setPreferredSize(new Dimension(length , height));
        evolutions.setPreferredSize(new Dimension(length ,height));
        crossoverDepth.setPreferredSize(new Dimension(length ,height));
        Functions.setPreferredSize(new Dimension(length ,height));

        crosDepth = new JTextField(integerFormat.format(DEFAULT_AMOUNT), text_length);
        evolve = new JTextField(integerFormat.format(DEFAULT_AMOUNT), text_length);
        inDepth = new JTextField(integerFormat.format(DEFAULT_AMOUNT), text_length);

        inDepth.setInputVerifier(verifier);
        evolve.setInputVerifier(verifier);
        crosDepth.setInputVerifier(verifier);

        inDepth.setEditable(true);
        crosDepth.setEditable(true);
        evolve.setEditable(true);

        submit.addActionListener(e -> {
            System.out.println(inDepth.getText());
            System.out.println(evolve.getText());
            System.out.println(crosDepth.getText());
        });

        JCheckBox chkSin = new JCheckBox("Sin");
        JCheckBox chkCos = new JCheckBox("Cos");
        JCheckBox chkExp = new JCheckBox("Exp");
        JCheckBox chkPower = new JCheckBox("Power");
        JCheckBox chkMultiply = new JCheckBox("Multiply");
        JCheckBox chkSubtrack = new JCheckBox("Subtract");
        JCheckBox chkSDivide = new JCheckBox("Divide");

        chkCos.addActionListener(e -> {
            counter[1]++;
            if (Math.floorMod(counter[1],2) == 1)
                System.out.println("clicked cos");
        });
        chkSin.addActionListener(e -> {
            counter[0]++;
            if (Math.floorMod(counter[0],2) == 1)
            System.out.println("clicked sin");
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
        pane.add (Functions);
        Functions.setBounds(insets.left + text_length, crossoverDepth.getY() + evolutions.getHeight(), crosDepth.getPreferredSize().width, crosDepth.getPreferredSize().height);
        pane.add (chkSin);
        chkSin.setBounds(insets.left + text_length*3, Functions.getY() + crosDepth.getHeight(), chkSin.getPreferredSize().width, chkSin.getPreferredSize().height);
        pane.add (chkCos);
        chkCos.setBounds(insets.left + text_length*3, chkSin.getY() + chkSin.getHeight(), chkCos.getPreferredSize().width, chkCos.getPreferredSize().height);
        pane.add (chkExp);
        chkExp.setBounds(insets.left + text_length*3, chkCos.getY() + chkCos.getHeight(), chkExp.getPreferredSize().width, chkExp.getPreferredSize().height);
        pane.add (chkPower);
        chkPower.setBounds(insets.left + text_length*4 + chkSin.getWidth(), Functions.getY() + crosDepth.getHeight(), chkPower.getPreferredSize().width, chkPower.getPreferredSize().height);
        pane.add (chkMultiply);
        chkMultiply.setBounds(insets.left + text_length*4 + chkSin.getWidth(), chkSin.getY() + chkSin.getHeight(), chkMultiply.getPreferredSize().width, chkMultiply.getPreferredSize().height);
        pane.add (chkSubtrack);
        chkSubtrack.setBounds(insets.left + text_length*4 + chkSin.getWidth(), chkCos.getY() + chkCos.getHeight(), chkSubtrack.getPreferredSize().width, chkSubtrack.getPreferredSize().height);
        pane.add (chkSDivide);
        chkSDivide.setBounds(insets.left + text_length*4 + chkSin.getWidth(), chkExp.getY() + chkExp.getHeight(), chkSDivide.getPreferredSize().width, chkSDivide.getPreferredSize().height);
        pane.add (submit);
        submit.setBounds(insets.left + text_length, 300, submit.getPreferredSize().width, submit.getPreferredSize().height);
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

    class MyVerifier extends InputVerifier
            implements ActionListener {
        String message = null;

        public boolean shouldYieldFocus(JComponent input) {
            boolean inputOK = verify(input);
            makeItPretty(input);
            if (inputOK) {
                return true;
            }

            //Pop up the message dialog.
            message += ".\nPlease try again.";
            JOptionPane.showMessageDialog(null, //no owner frame
                    message, //text to display
                    "Invalid Value", //title
                    JOptionPane.WARNING_MESSAGE);

            //Reinstall the input verifier.
            input.setInputVerifier(this);

            //Beep and then tell whoever called us that we don't
            //want to yield focus.
            Toolkit.getDefaultToolkit().beep();
            return false;
        }

        //This method checks input, but should cause no side effects.
        public boolean verify(JComponent input) {
            return checkField(input, false);
        }

        protected void makeItPretty(JComponent input) {
            checkField(input, true);
        }

        protected boolean checkField(JComponent input, boolean changeIt) {
            if (input == inDepth) {
                return checkAmountField(inDepth, changeIt, MIN_INIT, MAX_INIT, "initial depth");
            } else if (input == evolve) {
                return checkAmountField(evolve, changeIt, MIN_GENERATIONS, MAX_GENERATIONS, "the generation");
            } else if (input == crosDepth) {
                return checkAmountField(crosDepth, changeIt, MIN_CROSSOVER, MAX_CROSSOVER, "max crossover depth");
            } else {
                return true; //shouldn't happen
            }
        }

        //Checks that the amount field is valid.  If it is valid,
        //it returns true, otherwise it sets the message field and
        //returns false.  If the change argument is true,  set
        //the textfield to the parsed number so that it looks
        //good -- no letters, for example.
        public boolean checkAmountField(JTextField input, boolean change, int min, int max, String Message) {
            boolean wasValid = true;
            double amount;

            //Parse the value.
            try {
                amount = integerFormat.parse(input.getText()).
                        doubleValue();
            } catch (ParseException pe) {
                message = "Invalid format in"+ Message+" field";
                return false;
            }

            //Value was invalid.
            if ((amount < min) || (amount > max)) {
                wasValid = false;
                if (amount < min) {
                    message = Message +" has to be > "
                            + integerFormat.format(min);
                } else { //amount is greater than MAX_AMOUNT
                    message = Message+" has to be < "
                            + integerFormat.format(max);
                }
            }
            //Whether value was valid or not, format it nicely.
            if (change) {
                input.setText(integerFormat.format(amount));
                input.selectAll();
            }
            return wasValid;
        }



        public void actionPerformed(ActionEvent e) {
            JTextField source = (JTextField)e.getSource();
            shouldYieldFocus(source); //ignore return value
            source.selectAll();
        }
    }

    private void setUpFormats() {
        integerFormat = NumberFormat.getIntegerInstance();
    }

}
