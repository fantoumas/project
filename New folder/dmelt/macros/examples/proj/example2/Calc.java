// java module
// compile it as: "Run-Compile File"

package example2;

import java.awt.*;


public class Calc
{
 
  // initialise the class
  public  Calc() {
  } 
 


  // do something here
  public int[] doSomething() {
   
   int[] tmp= new int[10];
   for (int j=0; j<tmp.length; j++)
                            tmp[j]=j*2;   
   
   return tmp;
	}

}
