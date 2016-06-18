/*     */ package com.lagodiuk.gp.symbolic.interpreter;
/*     */ 
/*     */ import java.util.ArrayList;
/*     */ import java.util.Collection;
/*     */ import java.util.Collections;
/*     */ import java.util.HashMap;
/*     */ import java.util.Iterator;
/*     */ import java.util.List;
/*     */ import java.util.Map;
/*     */ import java.util.Random;
/*     */ import java.util.Set;
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ public class Context
/*     */ {
/*  28 */   private Random random = new Random();
/*     */   
/*  30 */   private double minValue = -50.0D;
/*     */   
/*  32 */   private double maxValue = 50.0D;
/*     */   
/*  34 */   private double minMutationValue = -3.0D;
/*     */   
/*  36 */   private double maxMutationValue = 3.0D;
/*     */   
/*  38 */   private Map<String, Double> variables = new HashMap();
/*     */   
/*  40 */   private List<Function> nonTerminalFunctions = new ArrayList();
/*     */   
/*  42 */   private List<Function> terminalFunctions = new ArrayList();
/*     */   
/*  44 */   private int nextRndFunctionIndx = 0;
/*     */   
/*     */   public Context(List<? extends Function> functions, Collection<String> variables) {
/*  47 */     for (Function f : functions) {
/*  48 */       if (f.argumentsCount() == 0) {
/*  49 */         this.terminalFunctions.add(f);
/*     */       } else {
/*  51 */         this.nonTerminalFunctions.add(f);
/*     */       }
/*     */     }
/*  54 */     if (this.terminalFunctions.isEmpty()) {
/*  55 */       throw new IllegalArgumentException("At least one terminal function must be defined");
/*     */     }
/*     */     
/*  58 */     if (variables.isEmpty()) {
/*  59 */       throw new IllegalArgumentException("At least one variable must be defined");
/*     */     }
/*     */     
/*  62 */     for (String variable : variables) {
/*  63 */       setVariable(variable, 0.0D);
/*     */     }
/*     */   }
/*     */   
/*     */   public double lookupVariable(String variable) {
/*  68 */     return ((Double)this.variables.get(variable)).doubleValue();
/*     */   }
/*     */   
/*     */   public void setVariable(String variable, double value) {
/*  72 */     this.variables.put(variable, Double.valueOf(value));
/*     */   }
/*     */   
/*     */   public Function getRandomNonTerminalFunction() {
/*  76 */     return roundRobinFunctionSelection();
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */   private Function roundRobinFunctionSelection()
/*     */   {
/*  86 */     if (this.nextRndFunctionIndx >= this.nonTerminalFunctions.size()) {
/*  87 */       this.nextRndFunctionIndx = 0;
/*  88 */       Collections.shuffle(this.nonTerminalFunctions);
/*     */     }
/*     */     
/*  91 */     return (Function)this.nonTerminalFunctions.get(this.nextRndFunctionIndx++);
/*     */   }
/*     */   
/*     */   public Function getRandomTerminalFunction() {
/*  95 */     int indx = this.random.nextInt(this.terminalFunctions.size());
/*  96 */     Function f = (Function)this.terminalFunctions.get(indx);
/*  97 */     return f;
/*     */   }
/*     */   
/*     */   public List<Function> getTerminalFunctions() {
/* 101 */     return this.terminalFunctions;
/*     */   }
/*     */   
/*     */   public String getRandomVariableName() {
/* 105 */     int indx = this.random.nextInt(this.variables.keySet().size());
/* 106 */     int i = 0;
/* 107 */     for (String varName : this.variables.keySet()) {
/* 108 */       if (i == indx) {
/* 109 */         return varName;
/*     */       }
/* 111 */       i++;
/*     */     }
/*     */     
/* 114 */     return (String)this.variables.keySet().iterator().next();
/*     */   }
/*     */   
/*     */   public double getRandomValue() {
/* 118 */     return this.random.nextDouble() * (this.maxValue - this.minValue) + this.minValue;
/*     */   }
/*     */   
/*     */   public double getRandomMutationValue() {
/* 122 */     return this.random.nextDouble() * (this.maxMutationValue - this.minMutationValue) + this.minMutationValue;
/*     */   }
/*     */   
/*     */   public boolean hasVariables() {
/* 126 */     return !this.variables.isEmpty();
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\interpreter\Context.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */