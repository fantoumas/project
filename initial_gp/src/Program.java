import javax.swing.*;
import java.awt.*;


/**
 * Created by Christina on 16/6/2016.
 */
public class Program {

    public static void main(String[] args) {
        Program player = new Program();
        SwingUtilities.invokeLater(() -> {
            try {
                player.run();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    private void run() throws Exception {

        JFrame frame = new JFrame("Demo");
        Screen screen = new Screen();
        frame.setDefaultCloseOperation(frame.EXIT_ON_CLOSE);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);
        screen.addComponentToPane(frame);
        screen.createMenuBar(frame);
//        OverlaidPlot plot = new OverlaidPlot("son");

//        frame.add(plot);
    }
}