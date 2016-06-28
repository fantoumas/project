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
        JFrame w = new JFrame("Demo");
        Screen screen = new Screen();
        w.setDefaultCloseOperation(w.EXIT_ON_CLOSE);
        w.setPreferredSize(new Dimension(800, 662));
        w.pack();
        w.setLocationByPlatform(true);
        w.setVisible(true);
        screen.createMenuBar(w);
    }
}