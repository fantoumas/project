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
/*    */ public class Antiderivative
/*    */   implements ExpressionFitness
/*    */ {
/* 24 */   private static double dx = 0.01D;
/*    */   
/*    */   public double fitness(Expression expression, Context context)
/*    */   {
/* 28 */     double delt = 0.0D;
/*    */     
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 34 */     for (double x = -10.0D; x < 10.0D; x += 1.0D)
/*    */     {
/* 36 */       double target = targetDerivative(x);
/*    */       
/* 38 */       double exprDerivative = expressionDerivative(expression, context, x);
/*    */       
/* 40 */       delt += sqr(target - exprDerivative);
/*    */     }
/*    */     
/* 43 */     return delt;
/*    */   }
/*    */   
/*    */   private double expressionDerivative(Expression expression, Context context, double x) {
/* 47 */     context.setVariable("x", x);
/* 48 */     double exprX = expression.eval(context);
/*    */     
/* 50 */     context.setVariable("x", x + dx);
/* 51 */     double exprXPlusdX = expression.eval(context);
/*    */     
/* 53 */     return (exprXPlusdX - exprX) / dx;
/*    */   }
/*    */   
/*    */   private double targetDerivative(double x) {
/* 57 */     return x * Math.sin(x);
/*    */   }
/*    */   
/*    */   private double sqr(double x) {
/* 61 */     return x * x;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\Antiderivative.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */