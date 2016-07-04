import java.applet.*;
import java.util.Random;
import jhplot.*;

public class Example2 
   extends Applet implements Runnable { 

 private static final long serialVersionUID = 1L;
 private HPlot3D c1;
 private Thread thread;
 private Random rand;
 private H2D h1;
 private F2D f1;
 private int i;

 public void init() {

 c1 = new HPlot3D("Canvas",600,400,2,1);
 c1.setGTitle("HPlot3D canvas tests");
 c1.visible(true);
 h1 = new H2D("My 2D Test1",30,-4.0, 4.0, 30, -4.0, 4.0); 
 f1 = new F2D("cos(x*y)*(x*x-y*y)", -2.0, 2.0, -2.0, 2.0); 
 rand = new Random();
 i=0;
}

 public void start() {
    (thread = new Thread(this)).start();
 }

 public void stop() {
    thread = null;

   c1.cd(1,1); 
   c1.draw(h1); 
   c1.setScaling(8); 
   c1.setRotationAngle(10); 
   c1.update(); 
 
   c1.cd(2,1); 
   c1.draw(f1); 
   c1.setScaling(8); 
   c1.setRotationAngle(30); 
   c1.update(); 
   
 }

public void run() {
 try {
     while (thread == Thread.currentThread()) {
          h1.fill(rand.nextGaussian(),0.5*rand.nextGaussian()); 
	  i++;
	  if (i >2000) stop();
     }
   } catch (Exception e) {} 
 }


}
