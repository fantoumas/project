/*    */ import com.lagodiuk.ga.GeneticAlgorithm;
/*    */ import com.lagodiuk.ga.IterartionListener;
/*    */ import java.io.PrintStream;
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ final class Demo$1
/*    */   implements IterartionListener<Demo.MyVector, Double>
/*    */ {
/* 66 */   private final double threshold = 1.0E-5D;
/*    */   
/*    */ 
/*    */   public void update(GeneticAlgorithm<Demo.MyVector, Double> ga)
/*    */   {
/* 71 */     Demo.MyVector best = (Demo.MyVector)ga.getBest();
/* 72 */     double bestFit = ((Double)ga.fitness(best)).doubleValue();
/* 73 */     int iteration = ga.getIteration();
/*    */     
/*    */ 
/* 76 */     System.out.println(String.format("%s\t%s\t%s", new Object[] { Integer.valueOf(iteration), Double.valueOf(bestFit), best }));
/*    */     
/*    */ 
/* 79 */     getClass(); if (bestFit < 1.0E-5D) {
/* 80 */       ga.terminate();
/*    */     }
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\Demo$1.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */