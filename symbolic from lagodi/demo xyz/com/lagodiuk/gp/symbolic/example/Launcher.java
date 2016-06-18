/*    */ package com.lagodiuk.gp.symbolic.example;
/*    */ 
/*    */ import com.lagodiuk.gp.symbolic.SymbolicRegressionEngine;
/*    */ import com.lagodiuk.gp.symbolic.SymbolicRegressionIterationListener;
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
/*    */ public class Launcher
/*    */ {
/*    */   public static void main(String[] args)
/*    */   {
/* 29 */     SymbolicRegressionEngine sr = new SymbolicRegressionEngine(new TestExpressionFitness2(), list(new String[] { "x", "y" }), list(Functions.values()));
/*    */     
/* 31 */     sr.addIterationListener(new SymbolicRegressionIterationListener() {
/* 32 */       private double prevFitValue = -1.0D;
/*    */       
/*    */       public void update(SymbolicRegressionEngine engine)
/*    */       {
/* 36 */         Expression bestSyntaxTree = engine.getBestSyntaxTree();
/* 37 */         double currFitValue = engine.fitness(bestSyntaxTree);
/* 38 */         if (Double.compare(currFitValue, this.prevFitValue) != 0) {
/* 39 */           System.out.println("Func = " + bestSyntaxTree.print());
/*    */         }
/* 41 */         System.out.println(String.format("%s \t %s", new Object[] { Integer.valueOf(engine.getIteration()), Double.valueOf(currFitValue) }));
/* 42 */         this.prevFitValue = currFitValue;
/* 43 */         if (currFitValue < 10.0D) {
/* 44 */           engine.terminate();
/*    */         }
/*    */         
/*    */       }
/* 48 */     });
/* 49 */     sr.evolve(200);
/* 50 */     System.out.println(sr.getBestSyntaxTree().print());
/*    */   }
/*    */   
/*    */   private static <T> List<T> list(T... items) {
/* 54 */     List<T> list = new LinkedList();
/* 55 */     for (T item : items) {
/* 56 */       list.add(item);
/*    */     }
/* 58 */     return list;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\Launcher.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */