//  Histograms | C | 1.7 | S.Chekanov |  Example using H1D histograms

import java.awt.Color;
import java.util.Random;
import jhplot.*;

class histo1
{
   public static void main(String[] args)
   {
HPlot c1 = new HPlot("Canvas",600,400,1,1);
c1.setGTitle("Global title for F_{2} and x_{&gamma;} "); 
c1.visible(true);
c1.setAutoRange();


H1D h1 = new H1D("Simple1",20, -2.0, 2.0);
Random rand = new Random();
for (int i=0; i<100; i++)  h1.fill(rand.nextGaussian());
     

c1.draw(h1);
h1.setColor(Color.blue);
h1.setPenWidthErr(2);
c1.setNameX("Xaxis");
c1.setNameY("Yaxis");
c1.setName("Canvas title");
c1.drawStatBox(h1);
c1.update();

// make png figure
c1.export("test.png");
 
   }    

  
}
