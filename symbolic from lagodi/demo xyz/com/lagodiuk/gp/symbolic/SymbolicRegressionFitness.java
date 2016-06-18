/*    */ package com.lagodiuk.gp.symbolic;
/*    */ 
/*    */ import com.lagodiuk.ga.Fitness;
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
/*    */ class SymbolicRegressionFitness
/*    */   implements Fitness<GpChromosome, Double>
/*    */ {
/*    */   private ExpressionFitness expressionFitness;
/*    */   
/*    */   public SymbolicRegressionFitness(ExpressionFitness expressionFitness)
/*    */   {
/* 27 */     this.expressionFitness = expressionFitness;
/*    */   }
/*    */   
/*    */   public Double calculate(GpChromosome chromosome)
/*    */   {
/* 32 */     Expression expression = chromosome.getSyntaxTree();
/* 33 */     Context context = chromosome.getContext();
/* 34 */     return Double.valueOf(this.expressionFitness.fitness(expression, context));
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\SymbolicRegressionFitness.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */