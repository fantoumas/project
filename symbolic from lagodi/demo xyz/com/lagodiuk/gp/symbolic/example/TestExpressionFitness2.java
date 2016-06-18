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
/*    */ public class TestExpressionFitness2
/*    */   implements ExpressionFitness
/*    */ {
/*    */   public double fitness(Expression expression, Context context)
/*    */   {
/* 26 */     double delt = 0.0D;
/* 27 */     for (int x = -10; x < 10; x += 2) {
/* 28 */       context.setVariable("x", x);
/* 29 */       for (int y = -10; y < 10; y += 2) {
/* 30 */         context.setVariable("y", y);
/*    */         
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/* 36 */         double target = x * x + y * y;
/*    */         
/* 38 */         double val = target - expression.eval(context);
/*    */         
/* 40 */         delt += val * val;
/*    */       }
/*    */     }
/* 43 */     return delt;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\TestExpressionFitness2.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */