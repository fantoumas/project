// java module
// compile it as: "Run-Compile File"

package example3;

import java.awt.*;


public class Estimate
{
 
  // initialise the class
  public  Estimate() {
  
  } 
 

  // do something here
  public double doSomething(int[] tmp) {
   
 double a=0;
   for (int j=0; j<tmp.length; j++)
                            a=a+tmp[j];   
   
   return a;
	}

}
