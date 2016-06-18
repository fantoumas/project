/*    */ import com.lagodiuk.gp.symbolic.SymbolicRegressionEngine;
/*    */ import com.lagodiuk.gp.symbolic.SymbolicRegressionIterationListener;
/*    */ import com.lagodiuk.gp.symbolic.TabulatedFunctionFitness;
/*    */ import com.lagodiuk.gp.symbolic.Target;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Functions;
/*    */ import java.io.PrintStream;
/*    */ import java.util.LinkedList;
/*    */ import java.util.List;
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
/*    */ public class HelloSymbolicRegression
/*    */ {
/*    */   public static void main(String[] args)
/*    */   {
/* 44 */     TabulatedFunctionFitness fitness = new TabulatedFunctionFitness(new Target[] { new Target().when("x", 0.0D).targetIs(0.0D), new Target().when("x", 1.0D).targetIs(11.0D), new Target().when("x", 2.0D).targetIs(24.0D), new Target().when("x", 3.0D).targetIs(39.0D), new Target().when("x", 4.0D).targetIs(56.0D), new Target().when("x", 5.0D).targetIs(75.0D), new Target().when("x", 6.0D).targetIs(96.0D) });
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 54 */     SymbolicRegressionEngine engine = new SymbolicRegressionEngine(fitness, list(new String[] { "x" }), list(new Functions[] { Functions.ADD, Functions.SUB, Functions.MUL, Functions.VARIABLE, Functions.CONSTANT }));
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 62 */     addListener(engine);
/*    */     
/*    */ 
/* 65 */     engine.evolve(200);
/*    */   }
/*    */   
/*    */ 
/*    */ 
/*    */   private static void addListener(SymbolicRegressionEngine engine)
/*    */   {
/* 72 */     engine.addIterationListener(new SymbolicRegressionIterationListener()
/*    */     {
/*    */       public void update(SymbolicRegressionEngine engine)
/*    */       {
/* 76 */         Expression bestSyntaxTree = engine.getBestSyntaxTree();
/*    */         
/* 78 */         double currFitValue = engine.fitness(bestSyntaxTree);
/*    */         
/*    */ 
/* 81 */         System.out.println(String.format("iter = %s \t fit = %s \t func = %s", new Object[] { Integer.valueOf(engine.getIteration()), Double.valueOf(currFitValue), bestSyntaxTree.print() }));
/*    */         
/*    */ 
/*    */ 
/*    */ 
/* 86 */         if (currFitValue < 5.0D) {
/* 87 */           engine.terminate();
/*    */         }
/*    */       }
/*    */     });
/*    */   }
/*    */   
/*    */   private static <T> List<T> list(T... items) {
/* 94 */     List<T> list = new LinkedList();
/* 95 */     for (T item : items) {
/* 96 */       list.add(item);
/*    */     }
/* 98 */     return list;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\HelloSymbolicRegression.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */