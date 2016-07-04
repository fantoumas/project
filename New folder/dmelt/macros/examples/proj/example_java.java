import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.net.*;

// import from the library classes.jar
import example2.*;

class example_java
{  
        public static void main(String args[])
        {
           System.out.println("Hello World!");

           // get class from example2 
            Calc a=new Calc();
            int[] array=a.doSomething();
            for (int j=0; j<array.length; j++) 
                              System.out.println(array[j]+" ");
        }

}
