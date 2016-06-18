/*    */ package com.lagodiuk.gp.symbolic.example;
/*    */ 
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
/*    */ public class Launcher2
/*    */ {
/*    */   public static void main(String[] args)
/*    */   {
/* 31 */     TabulatedFunctionFitness fitnessFunction = new TabulatedFunctionFitness(new Target[] { new Target().when("x", 0.0D).targetIs(0.0D), new Target().when("x", 1.0D).targetIs(2.0D), new Target().when("x", 2.0D).targetIs(6.0D), new Target().when("x", 3.0D).targetIs(12.0D), new Target().when("x", 4.0D).targetIs(20.0D), new Target().when("x", 5.0D).targetIs(30.0D), new Target().when("x", 6.0D).targetIs(42.0D) });
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 40 */     SymbolicRegressionEngine engine = new SymbolicRegressionEngine(fitnessFunction, list(new String[] { "x" }), list(Functions.values()));
/*    */     
/* 42 */     engine.addIterationListener(new SymbolicRegressionIterationListener() {
/* 43 */       private double prevFitValue = -1.0D;
/*    */       
/*    */       public void update(SymbolicRegressionEngine engine)
/*    */       {
/* 47 */         Expression bestSyntaxTree = engine.getBestSyntaxTree();
/* 48 */         double currFitValue = engine.fitness(bestSyntaxTree);
/* 49 */         if (Double.compare(currFitValue, this.prevFitValue) != 0) {
/* 50 */           System.out.println("Func = " + bestSyntaxTree.print());
/*    */         }
/* 52 */         System.out.println(String.format("%s \t %s", new Object[] { Integer.valueOf(engine.getIteration()), Double.valueOf(currFitValue) }));
/* 53 */         this.prevFitValue = currFitValue;
/* 54 */         if (currFitValue < 10.0D) {
/* 55 */           engine.terminate();
/*    */         }
/*    */         
/*    */       }
/* 59 */     });
/* 60 */     engine.evolve(200);
/* 61 */     System.out.println(engine.getBestSyntaxTree().print());
/*    */   }
/*    */   
/*    */   private static <T> List<T> list(T... items) {
/* 65 */     List<T> list = new LinkedList();
/* 66 */     for (T item : items) {
/* 67 */       list.add(item);
/*    */     }
/* 69 */     return list;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\Launcher2.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */