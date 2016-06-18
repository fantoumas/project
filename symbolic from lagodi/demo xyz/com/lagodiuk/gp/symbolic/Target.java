/*    */ package com.lagodiuk.gp.symbolic;
/*    */ 
/*    */ import java.util.HashMap;
/*    */ import java.util.Map;
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
/*    */ public class Target
/*    */ {
/* 22 */   private Map<String, Double> contextState = new HashMap();
/*    */   private double targetValue;
/*    */   
/*    */   public Target() {}
/*    */   
/*    */   public Target(Map<String, Double> contextState, double targetValue)
/*    */   {
/* 29 */     this.contextState.putAll(contextState);
/* 30 */     this.targetValue = targetValue;
/*    */   }
/*    */   
/*    */   public Target when(String variableName, double variableValue) {
/* 34 */     this.contextState.put(variableName, Double.valueOf(variableValue));
/* 35 */     return this;
/*    */   }
/*    */   
/*    */   public Target targetIs(double targetValue) {
/* 39 */     this.targetValue = targetValue;
/* 40 */     return this;
/*    */   }
/*    */   
/*    */   public double getTargetValue() {
/* 44 */     return this.targetValue;
/*    */   }
/*    */   
/*    */   public Map<String, Double> getContextState() {
/* 48 */     return this.contextState;
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\Target.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */