/*     */ package com.lagodiuk.gp.symbolic.interpreter;
/*     */ 
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
/*     */ public class SyntaxTreeUtils
/*     */ {
/*     */   public static Expression createTree(int depth, Context context)
/*     */   {
/*  23 */     if (depth > 0) {
/*     */       Function f;
/*     */       Function f;
/*  26 */       if (Math.random() >= 0.5D) {
/*  27 */         f = context.getRandomNonTerminalFunction();
/*     */       } else {
/*  29 */         f = context.getRandomTerminalFunction();
/*     */       }
/*     */       
/*  32 */       Expression expr = new Expression(f);
/*     */       
/*  34 */       if (f.argumentsCount() > 0)
/*     */       {
/*  36 */         for (int i = 0; i < f.argumentsCount(); i++) {
/*  37 */           Expression child = createTree(depth - 1, context);
/*  38 */           expr.addChild(child);
/*     */         }
/*     */         
/*     */ 
/*     */       }
/*  43 */       else if (f.isVariable())
/*     */       {
/*  45 */         String varName = context.getRandomVariableName();
/*  46 */         expr.setVariable(varName);
/*     */       }
/*     */       
/*     */ 
/*     */ 
/*     */ 
/*  52 */       for (int i = 0; i < f.coefficientsCount(); i++) {
/*  53 */         expr.addCoefficient(context.getRandomValue());
/*     */       }
/*     */       
/*  56 */       return expr;
/*     */     }
/*     */     
/*     */ 
/*  60 */     Function f = context.getRandomTerminalFunction();
/*  61 */     Expression expr = new Expression(f);
/*     */     
/*  63 */     if (f.isVariable())
/*     */     {
/*  65 */       String varName = context.getRandomVariableName();
/*  66 */       expr.setVariable(varName);
/*     */     }
/*     */     
/*     */ 
/*  70 */     for (int i = 0; i < f.coefficientsCount(); i++) {
/*  71 */       expr.addCoefficient(context.getRandomValue());
/*     */     }
/*     */     
/*  74 */     return expr;
/*     */   }
/*     */   
/*     */ 
/*     */   public static void simplifyTree(Expression tree, Context context)
/*     */   {
/*  80 */     if (hasVariableNode(tree)) {
/*  81 */       for (Expression child : tree.getChilds()) {
/*  82 */         simplifyTree(child, context);
/*     */       }
/*     */     } else {
/*  85 */       double value = tree.eval(context);
/*  86 */       tree.addCoefficient(value);
/*  87 */       tree.removeChilds();
/*  88 */       List<Function> terminalFunctions = context.getTerminalFunctions();
/*  89 */       for (Function f : terminalFunctions) {
/*  90 */         if (f.isNumber()) {
/*  91 */           tree.setFunction(f);
/*  92 */           break;
/*     */         }
/*     */       }
/*     */     }
/*     */   }
/*     */   
/*     */   public static void cutTree(Expression tree, Context context, int depth) {
/*  99 */     if (depth > 0) {
/* 100 */       for (Expression child : tree.getChilds()) {
/* 101 */         cutTree(child, context, depth - 1);
/*     */       }
/*     */     } else {
/* 104 */       tree.removeChilds();
/* 105 */       tree.removeCoefficients();
/* 106 */       Function func = context.getRandomTerminalFunction();
/* 107 */       tree.setFunction(func);
/* 108 */       if (func.isVariable()) {
/* 109 */         tree.setVariable(context.getRandomVariableName());
/*     */       } else {
/* 111 */         tree.addCoefficient(context.getRandomValue());
/*     */       }
/*     */     }
/*     */   }
/*     */   
/*     */   public static boolean hasVariableNode(Expression tree) {
/* 117 */     boolean ret = false;
/*     */     
/* 119 */     if (tree.getFunction().isVariable()) {
/* 120 */       ret = true;
/*     */     } else {
/* 122 */       for (Expression child : tree.getChilds()) {
/* 123 */         ret = hasVariableNode(child);
/* 124 */         if (ret) {
/*     */           break;
/*     */         }
/*     */       }
/*     */     }
/*     */     
/* 130 */     return ret;
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\interpreter\SyntaxTreeUtils.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */