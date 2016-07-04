import java.applet.*;
import java.awt.*;
import java.util.Random;
import jhplot.*;

public class Example1 
   extends Applet implements Runnable { 

 private static final long serialVersionUID = 1L;
 private HPlot c1;
 private Thread thread;
 private Random rand;
 private H1D h1;
 private int i;

 public void init() {

 c1 = new HPlot("Canvas",600,400,1,1);
 c1.setGTitle("Gaussian random numbers");
 c1.visible(true);
 c1.setAutoRange();
 h1 = new H1D("Random numbers",20, -2.0, 2.0);
 h1.setColor(Color.blue);
 h1.setPenWidthErr(2);
 h1.setFill(true);
 h1.setFillColor(Color.green);
 c1.setNameX("X axis");
 c1.setNameY("Y axis");
 c1.setName("100 numbers and statistics");
 rand = new Random();
 i=0;
}

 public void start() {
    (thread = new Thread(this)).start();
 }

 public void stop() {
    thread = null;
    c1.drawStatBox(h1);
 }

public void run() {
 try {
     while (thread == Thread.currentThread()) {
 	  Thread.sleep(50);
	  h1.fill(rand.nextGaussian());
	  c1.clearData(); 
	  c1.draw(h1); 
	  i++;
	  if (i >100) stop();
     }
   } catch (Exception e) {} 
 }


}
