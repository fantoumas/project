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
/*    */ public class TestExpressionFitness
/*    */   implements ExpressionFitness
/*    */ {
/*    */   public double fitness(Expression expression, Context context)
/*    */   {
/* 26 */     double delt = 0.0D;
/* 27 */     for (int i = -20; i < 20; i++)
/*    */     {
/* 29 */       context.setVariable("x", i);
/*    */       
/* 31 */       double target = i * i * i * 5 + i + 10;
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
/* 42 */       double x = target - expression.eval(context);
/*    */       
/* 44 */       delt += x * x;
/*    */     }
/* 46 */     return delt;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\TestExpressionFitness.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */