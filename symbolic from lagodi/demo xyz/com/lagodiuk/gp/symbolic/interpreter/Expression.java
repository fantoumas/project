/*     */ package com.lagodiuk.gp.symbolic.interpreter;
/*     */ 
/*     */ import java.util.ArrayList;
/*     */ import java.util.Collections;
/*     */ import java.util.Deque;
/*     */ import java.util.LinkedList;
/*     */ import java.util.List;
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
/*     */ 
/*     */ public class Expression
/*     */   implements Cloneable
/*     */ {
/*  26 */   private List<Expression> childs = new ArrayList();
/*     */   
/*  28 */   private List<Double> coefficients = new ArrayList();
/*     */   
/*     */   private String variable;
/*     */   private Function function;
/*     */   
/*     */   public Expression(Function function)
/*     */   {
/*  35 */     this.function = function;
/*     */   }
/*     */   
/*     */   public double eval(Context context) {
/*  39 */     return this.function.eval(this, context);
/*     */   }
/*     */   
/*     */   public String print() {
/*  43 */     return this.function.print(this);
/*     */   }
/*     */   
/*     */   public List<Expression> getChilds() {
/*  47 */     return this.childs;
/*     */   }
/*     */   
/*     */   public Expression setChilds(List<Expression> childs) {
/*  51 */     this.childs = childs;
/*  52 */     return this;
/*     */   }
/*     */   
/*     */   public void addChild(Expression child) {
/*  56 */     this.childs.add(child);
/*     */   }
/*     */   
/*     */   public void removeChilds() {
/*  60 */     this.childs.clear();
/*     */   }
/*     */   
/*     */   public List<Double> getCoefficientsOfNode() {
/*  64 */     return this.coefficients;
/*     */   }
/*     */   
/*     */   public Expression setCoefficientsOfNode(List<Double> coefficients) {
/*  68 */     this.coefficients = coefficients;
/*  69 */     return this;
/*     */   }
/*     */   
/*     */   public void addCoefficient(double coefficient) {
/*  73 */     this.coefficients.add(Double.valueOf(coefficient));
/*     */   }
/*     */   
/*     */   public void removeCoefficients() {
/*  77 */     if (this.coefficients.size() > 0) {
/*  78 */       this.coefficients.clear();
/*     */     }
/*     */   }
/*     */   
/*     */   public String getVariable() {
/*  83 */     return this.variable;
/*     */   }
/*     */   
/*     */   public Expression setVariable(String variable) {
/*  87 */     this.variable = variable;
/*  88 */     return this;
/*     */   }
/*     */   
/*     */   public Function getFunction() {
/*  92 */     return this.function;
/*     */   }
/*     */   
/*     */   public void setFunction(Function function) {
/*  96 */     this.function = function;
/*     */   }
/*     */   
/*     */   public Expression clone()
/*     */   {
/* 101 */     Expression cloned = new Expression(this.function);
/* 102 */     if (this.variable != null) {
/* 103 */       cloned.variable = new String(this.variable);
/*     */     }
/* 105 */     for (Expression c : this.childs) {
/* 106 */       cloned.childs.add(c.clone());
/*     */     }
/* 108 */     for (Double d : this.coefficients) {
/* 109 */       cloned.coefficients.add(d);
/*     */     }
/* 111 */     return cloned;
/*     */   }
/*     */   
/*     */   public List<Double> getCoefficientsOfTree() {
/* 115 */     LinkedList<Double> coefficients = new LinkedList();
/* 116 */     getCoefficientsOfTree(coefficients);
/* 117 */     Collections.reverse(coefficients);
/* 118 */     return coefficients;
/*     */   }
/*     */   
/*     */   private void getCoefficientsOfTree(Deque<Double> coefficients) {
/* 122 */     List<Double> coeffs = this.function.getCoefficients(this);
/* 123 */     for (Double d : coeffs) {
/* 124 */       coefficients.push(d);
/*     */     }
/* 126 */     for (int i = 0; i < this.childs.size(); i++) {
/* 127 */       ((Expression)this.childs.get(i)).getCoefficientsOfTree(coefficients);
/*     */     }
/*     */   }
/*     */   
/*     */   public void setCoefficientsOfTree(List<Double> coefficients) {
/* 132 */     setCoefficientsOfTree(coefficients, 0);
/*     */   }
/*     */   
/*     */   private int setCoefficientsOfTree(List<Double> coefficients, int index) {
/* 136 */     this.function.setCoefficients(this, coefficients, index);
/* 137 */     index += this.function.coefficientsCount();
/* 138 */     if (this.childs.size() > 0) {
/* 139 */       for (int i = 0; i < this.childs.size(); i++) {
/* 140 */         index = ((Expression)this.childs.get(i)).setCoefficientsOfTree(coefficients, index);
/*     */       }
/*     */     }
/* 143 */     return index;
/*     */   }
/*     */   
/*     */   public List<Expression> getAllNodesAsList() {
/* 147 */     List<Expression> nodes = new LinkedList();
/* 148 */     getAllNodesBreadthFirstSearch(nodes);
/* 149 */     return nodes;
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */   private void getAllNodesBreadthFirstSearch(List<Expression> nodesList)
/*     */   {
/* 156 */     int indx = 0;
/* 157 */     nodesList.add(this);
/*     */     
/* 159 */     while (indx < nodesList.size()) {
/* 160 */       Expression node = (Expression)nodesList.get(indx++);
/* 161 */       for (Expression child : node.childs) {
/* 162 */         nodesList.add(child);
/*     */       }
/*     */     }
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\interpreter\Expression.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */