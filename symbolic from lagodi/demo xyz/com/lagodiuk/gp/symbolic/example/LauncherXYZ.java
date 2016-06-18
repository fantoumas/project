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
/*    */ 
/*    */ 
/*    */ 
/*    */ public class LauncherXYZ
/*    */ {
/*    */   public static void main(String[] args)
/*    */   {
/* 34 */     TabulatedFunctionFitness fitnessFunction = new TabulatedFunctionFitness(new Target[] { new Target().when("x", 26.0D).when("y", 35.0D).when("z", 1.0D).targetIs(830.0D), new Target().when("x", 8.0D).when("y", 24.0D).when("z", -11.0D).targetIs(130.0D), new Target().when("x", 20.0D).when("y", 1.0D).when("z", 10.0D).targetIs(477.0D), new Target().when("x", 33.0D).when("y", 11.0D).when("z", 2.0D).targetIs(1217.0D), new Target().when("x", 37.0D).when("y", 16.0D).when("z", 7.0D).targetIs(1524.0D) });
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 41 */     SymbolicRegressionEngine engine = new SymbolicRegressionEngine(fitnessFunction, list(new String[] { "x", "y", "z" }), list(new Functions[] { Functions.ADD, Functions.SUB, Functions.MUL, Functions.VARIABLE, Functions.CONSTANT }));
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 47 */     addListener(engine);
/*    */     
/* 49 */     engine.evolve(200);
/* 50 */     System.out.println(engine.getBestSyntaxTree().print());
/*    */   }
/*    */   
/*    */   private static void addListener(SymbolicRegressionEngine engine) {
/* 54 */     engine.addIterationListener(new SymbolicRegressionIterationListener() {
/* 55 */       private double prevFitValue = -1.0D;
/*    */       
/*    */       public void update(SymbolicRegressionEngine engine)
/*    */       {
/* 59 */         Expression bestSyntaxTree = engine.getBestSyntaxTree();
/* 60 */         double currFitValue = engine.fitness(bestSyntaxTree);
/* 61 */         if (Double.compare(currFitValue, this.prevFitValue) != 0) {
/* 62 */           System.out.println("Func = " + bestSyntaxTree.print());
/*    */         }
/* 64 */         System.out.println(String.format("%s \t %s", new Object[] { Integer.valueOf(engine.getIteration()), Double.valueOf(currFitValue) }));
/* 65 */         this.prevFitValue = currFitValue;
/* 66 */         if (currFitValue < 5.0D) {
/* 67 */           engine.terminate();
/*    */         }
/*    */       }
/*    */     });
/*    */   }
/*    */   
/*    */   private static <T> List<T> list(T... items) {
/* 74 */     List<T> list = new LinkedList();
/* 75 */     for (T item : items) {
/* 76 */       list.add(item);
/*    */     }
/* 78 */     return list;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\LauncherXYZ.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */