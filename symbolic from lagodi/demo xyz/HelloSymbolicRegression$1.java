/*    */ import com.lagodiuk.gp.symbolic.SymbolicRegressionEngine;
/*    */ import com.lagodiuk.gp.symbolic.SymbolicRegressionIterationListener;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
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
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ final class HelloSymbolicRegression$1
/*    */   implements SymbolicRegressionIterationListener
/*    */ {
/*    */   public void update(SymbolicRegressionEngine engine)
/*    */   {
/* 76 */     Expression bestSyntaxTree = engine.getBestSyntaxTree();
/*    */     
/* 78 */     double currFitValue = engine.fitness(bestSyntaxTree);
/*    */     
/*    */ 
/* 81 */     System.out.println(String.format("iter = %s \t fit = %s \t func = %s", new Object[] { Integer.valueOf(engine.getIteration()), Double.valueOf(currFitValue), bestSyntaxTree.print() }));
/*    */     
/*    */ 
/*    */ 
/*    */ 
/* 86 */     if (currFitValue < 5.0D) {
/* 87 */       engine.terminate();
/*    */     }
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\HelloSymbolicRegression$1.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */