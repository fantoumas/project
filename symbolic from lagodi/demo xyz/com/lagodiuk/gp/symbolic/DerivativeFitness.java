/*    */ package com.lagodiuk.gp.symbolic;
/*    */ 
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
/*    */ public abstract class DerivativeFitness
/*    */   implements ExpressionFitness
/*    */ {
/* 23 */   private double left = -10.0D;
/*    */   
/* 25 */   private double right = 10.0D;
/*    */   
/* 27 */   private double dx = 1.0E-5D;
/*    */   
/* 29 */   private double step = 1.0D;
/*    */   
/*    */   public abstract double f(double paramDouble);
/*    */   
/*    */   public double fitness(Expression expression, Context context)
/*    */   {
/* 35 */     double delt = 0.0D;
/*    */     
/* 37 */     for (double x = this.left; x <= this.right; x += this.step) {
/* 38 */       double target = (f(x + this.dx) - f(x)) / this.dx;
/*    */       
/* 40 */       context.setVariable("x", x);
/* 41 */       double exprVal = expression.eval(context);
/*    */       
/* 43 */       delt += sqr(target - exprVal);
/*    */     }
/*    */     
/* 46 */     return delt;
/*    */   }
/*    */   
/*    */   private double sqr(double x) {
/* 50 */     return x * x;
/*    */   }
/*    */   
/*    */   public double getLeft() {
/* 54 */     return this.left;
/*    */   }
/*    */   
/*    */   public DerivativeFitness setLeft(double left) {
/* 58 */     this.left = left;
/* 59 */     return this;
/*    */   }
/*    */   
/*    */   public double getRight() {
/* 63 */     return this.right;
/*    */   }
/*    */   
/*    */   public DerivativeFitness setRight(double right) {
/* 67 */     this.right = right;
/* 68 */     return this;
/*    */   }
/*    */   
/*    */   public double getDx() {
/* 72 */     return this.dx;
/*    */   }
/*    */   
/*    */   public DerivativeFitness setDx(double dx) {
/* 76 */     this.dx = dx;
/* 77 */     return this;
/*    */   }
/*    */   
/*    */   public double getStep() {
/* 81 */     return this.step;
/*    */   }
/*    */   
/*    */   public DerivativeFitness setStep(double step) {
/* 85 */     this.step = step;
/* 86 */     return this;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\DerivativeFitness.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */