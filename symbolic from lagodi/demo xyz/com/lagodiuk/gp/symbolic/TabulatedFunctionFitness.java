/*    */ package com.lagodiuk.gp.symbolic;
/*    */ 
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Context;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
/*    */ import java.util.LinkedList;
/*    */ import java.util.List;
/*    */ import java.util.Map;
/*    */ import java.util.Map.Entry;
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
/*    */ public class TabulatedFunctionFitness
/*    */   implements ExpressionFitness
/*    */ {
/* 27 */   private List<Target> targets = new LinkedList();
/*    */   
/*    */   public TabulatedFunctionFitness(Target... targets) {
/* 30 */     for (Target target : targets) {
/* 31 */       this.targets.add(target);
/*    */     }
/*    */   }
/*    */   
/*    */   public TabulatedFunctionFitness(List<Target> targets) {
/* 36 */     this.targets.addAll(targets);
/*    */   }
/*    */   
/*    */   public double fitness(Expression expression, Context context)
/*    */   {
/* 41 */     double diff = 0.0D;
/*    */     
/* 43 */     for (Target target : this.targets) {
/* 44 */       for (Map.Entry<String, Double> e : target.getContextState().entrySet()) {
/* 45 */         String variableName = (String)e.getKey();
/* 46 */         Double variableValue = (Double)e.getValue();
/* 47 */         context.setVariable(variableName, variableValue.doubleValue());
/*    */       }
/* 49 */       double targetValue = target.getTargetValue();
/* 50 */       double calculatedValue = expression.eval(context);
/* 51 */       diff += sqr(targetValue - calculatedValue);
/*    */     }
/*    */     
/* 54 */     return diff;
/*    */   }
/*    */   
/*    */   private double sqr(double x) {
/* 58 */     return x * x;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\TabulatedFunctionFitness.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */