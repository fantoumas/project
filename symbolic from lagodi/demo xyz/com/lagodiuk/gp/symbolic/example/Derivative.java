/*    */ package com.lagodiuk.gp.symbolic.example;
/*    */ 
/*    */ import com.lagodiuk.gp.symbolic.ExpressionFitness;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Context;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
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
/*    */ public class Derivative
/*    */   implements ExpressionFitness
/*    */ {
/* 24 */   private static double dx = 1.0E-5D;
/*    */   
/*    */   public double fitness(Expression expression, Context context)
/*    */   {
/* 28 */     double delt = 0.0D;
/*    */     
/* 30 */     for (int x = -10; x < 11; x++) {
/* 31 */       double target = (f(x + dx) - f(x)) / dx;
/*    */       
/* 33 */       context.setVariable("x", x);
/* 34 */       double exprVal = expression.eval(context);
/*    */       
/* 36 */       delt += sqr(target - exprVal);
/*    */     }
/*    */     
/* 39 */     return delt;
/*    */   }
/*    */   
/*    */   private double f(double x) {
/* 43 */     return x * x * x;
/*    */   }
/*    */   
/*    */   private double sqr(double x) {
/* 47 */     return x * x;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\Derivative.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */