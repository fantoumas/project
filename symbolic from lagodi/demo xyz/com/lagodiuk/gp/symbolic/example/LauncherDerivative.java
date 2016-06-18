/*    */ package com.lagodiuk.gp.symbolic.example;
/*    */ 
/*    */ import com.lagodiuk.gp.symbolic.DerivativeFitness;
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
/*    */ public class LauncherDerivative
/*    */ {
/*    */   public static void main(String[] args)
/*    */   {
/* 30 */     DerivativeFitness fitnessFunc = new DerivativeFitness()
/*    */     {
/*    */       public double f(double x) {
/* 33 */         return x * x * x + 10.0D * x + Math.pow(3.0D, x);
/*    */       }
/* 35 */     };
/* 36 */     fitnessFunc.setLeft(-10.0D).setRight(10.0D).setStep(0.5D).setDx(0.01D);
/* 37 */     SymbolicRegressionEngine engine = new SymbolicRegressionEngine(fitnessFunc, list(new String[] { "x" }), list(Functions.values()));
/* 38 */     engine.addIterationListener(new SymbolicRegressionIterationListener() {
/* 39 */       private double prevFitValue = -1.0D;
/*    */       
/*    */       public void update(SymbolicRegressionEngine engine)
/*    */       {
/* 43 */         Expression bestSyntaxTree = engine.getBestSyntaxTree();
/* 44 */         double currFitValue = engine.fitness(bestSyntaxTree);
/* 45 */         if (Double.compare(currFitValue, this.prevFitValue) != 0) {
/* 46 */           System.out.println("Func = " + bestSyntaxTree.print());
/*    */         }
/* 48 */         System.out.println(String.format("%s \t %s", new Object[] { Integer.valueOf(engine.getIteration()), Double.valueOf(currFitValue) }));
/* 49 */         this.prevFitValue = currFitValue;
/* 50 */         if (currFitValue < 10.0D) {
/* 51 */           engine.terminate();
/*    */         }
/*    */         
/*    */       }
/* 55 */     });
/* 56 */     engine.evolve(200);
/* 57 */     System.out.println(engine.getBestSyntaxTree().print());
/*    */   }
/*    */   
/*    */   private static <T> List<T> list(T... items) {
/* 61 */     List<T> list = new LinkedList();
/* 62 */     for (T item : items) {
/* 63 */       list.add(item);
/*    */     }
/* 65 */     return list;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\LauncherDerivative.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */