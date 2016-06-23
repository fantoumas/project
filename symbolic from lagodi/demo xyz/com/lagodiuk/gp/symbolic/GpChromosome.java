/*     */ package com.lagodiuk.gp.symbolic;
/*     */ 
/*     */ import com.lagodiuk.ga.Chromosome;
/*     */ import com.lagodiuk.ga.Fitness;
/*     */ import com.lagodiuk.ga.GeneticAlgorithm;
/*     */ import com.lagodiuk.ga.Population;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.Context;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.Function;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.SyntaxTreeUtils;
/*     */ import java.util.ArrayList;
/*     */ import java.util.Collections;
/*     */ import java.util.Iterator;
/*     */ import java.util.List;
/*     */ import java.util.Random;
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
/*     */ 
/*     */ 
/*     */ 
/*     */ class GpChromosome
/*     */   implements Chromosome<GpChromosome>
/*     */ {
/*     */   private Expression syntaxTree;
/*     */   private Context context;
/*     */   private Fitness<GpChromosome, Double> fitnessFunction;
/*  40 */   private Random random = new Random();
/*     */   
/*     */   public GpChromosome(Context context, Fitness<GpChromosome, Double> fitnessFunction, Expression syntaxTree) {
/*  43 */     this.context = context;
/*  44 */     this.fitnessFunction = fitnessFunction;
/*  45 */     this.syntaxTree = syntaxTree;
/*     */   }
/*     */   
/*     */   public List<GpChromosome> crossover(GpChromosome anotherChromosome)
/*     */   {
/*  50 */     List<GpChromosome> ret = new ArrayList(2);
/*     */     
/*  52 */     GpChromosome thisClone = new GpChromosome(this.context, this.fitnessFunction, this.syntaxTree.clone());
/*  53 */     GpChromosome anotherClone = new GpChromosome(this.context, this.fitnessFunction, anotherChromosome.syntaxTree.clone());
/*     */     
/*  55 */     Expression thisRandomNode = getRandomNode(thisClone.syntaxTree);
/*  56 */     Expression anotherRandomNode = getRandomNode(anotherClone.syntaxTree);
/*     */     
/*  58 */     Expression thisRandomSubTreeClone = thisRandomNode.clone();
/*  59 */     Expression anotherRandomSubTreeClone = anotherRandomNode.clone();
/*     */     
/*  61 */     swapNode(thisRandomNode, anotherRandomSubTreeClone);
/*  62 */     swapNode(anotherRandomNode, thisRandomSubTreeClone);
/*     */     
/*  64 */     ret.add(thisClone);
/*  65 */     ret.add(anotherClone);
/*     */     
/*  67 */     thisClone.optimizeTree();
/*  68 */     anotherClone.optimizeTree();
/*     */     
/*  70 */     return ret;
/*     */   }
/*     */   
/*     */   public GpChromosome mutate()
/*     */   {
/*  75 */     GpChromosome ret = new GpChromosome(this.context, this.fitnessFunction, this.syntaxTree.clone());
/*     */     
/*  77 */     int type = this.random.nextInt(7);
/*  78 */     switch (type) {
/*     */     case 0: 
/*  80 */       ret.mutateByRandomChangeOfFunction();
/*  81 */       break;
/*     */     case 1: 
/*  83 */       ret.mutateByRandomChangeOfChild();
/*  84 */       break;
/*     */     case 2: 
/*  86 */       ret.mutateByRandomChangeOfNodeToChild();
/*  87 */       break;
/*     */     case 3: 
/*  89 */       ret.mutateByReverseOfChildsList();
/*  90 */       break;
/*     */     case 4: 
/*  92 */       ret.mutateByRootGrowth();
/*  93 */       break;
/*     */     case 5: 
/*  95 */       ret.syntaxTree = SyntaxTreeUtils.createTree(2, this.context);
/*  96 */       break;
/*     */     case 6: 
/*  98 */       ret.mutateByReplaceEntireTreeWithAnySubTree();
/*     */     }
/*     */     
/*     */     
/* 102 */     ret.optimizeTree();
/* 103 */     return ret;
/*     */   }
/*     */   
/*     */   private void mutateByReplaceEntireTreeWithAnySubTree() {
/* 107 */     this.syntaxTree = getRandomNode(this.syntaxTree);
/*     */   }
/*     */   
/*     */   private void mutateByRootGrowth() {
/* 111 */     Function function = this.context.getRandomNonTerminalFunction();
/* 112 */     Expression newRoot = new Expression(function);
/* 113 */     newRoot.addChild(this.syntaxTree);
/* 114 */     for (int i = 1; i < function.argumentsCount(); i++) {
/* 115 */       newRoot.addChild(SyntaxTreeUtils.createTree(0, this.context));
/*     */     }
/* 117 */     for (int i = 0; i < function.argumentsCount(); i++) {
/* 118 */       newRoot.addCoefficient(this.context.getRandomValue());
/*     */     }
/* 120 */     this.syntaxTree = newRoot;
/*     */   }
/*     */   
/*     */   private void mutateByRandomChangeOfFunction() {
/* 124 */     Expression mutatingNode = getRandomNode(this.syntaxTree);
/*     */     
/* 126 */     Function oldFunction = mutatingNode.getFunction();
/* 127 */     Function newFunction = null;
/*     */     
/*     */ 
/*     */ 
/*     */ 
/* 132 */     for (int i = 0; i < 3; i++) {
/* 133 */       if (this.random.nextDouble() > 0.5D) {
/* 134 */         newFunction = this.context.getRandomNonTerminalFunction();
/*     */       } else {
/* 136 */         newFunction = this.context.getRandomTerminalFunction();
/*     */       }
/*     */       
/* 139 */       if (newFunction != oldFunction) {
/*     */         break;
/*     */       }
/*     */     }
/*     */     
/* 144 */     mutatingNode.setFunction(newFunction);
/*     */     
/* 146 */     if (newFunction.isVariable()) {
/* 147 */       mutatingNode.setVariable(this.context.getRandomVariableName());
/*     */     }
/*     */     
/* 150 */     int functionArgumentsCount = newFunction.argumentsCount();
/* 151 */     int mutatingNodeChildsCount = mutatingNode.getChilds().size();
/*     */     
/* 153 */     if (functionArgumentsCount > mutatingNodeChildsCount) {
/* 154 */       for (int i = 0; i < functionArgumentsCount - mutatingNodeChildsCount + 1; i++) {
/* 155 */         mutatingNode.getChilds().add(SyntaxTreeUtils.createTree(1, this.context));
/*     */       }
/* 157 */     } else if (functionArgumentsCount < mutatingNodeChildsCount) {
/* 158 */       List<Expression> subList = new ArrayList(functionArgumentsCount);
/* 159 */       for (int i = 0; i < functionArgumentsCount; i++) {
/* 160 */         subList.add(mutatingNode.getChilds().get(i));
/*     */       }
/* 162 */       mutatingNode.setChilds(subList);
/*     */     }
/*     */     
/* 165 */     int functionCoefficientsCount = newFunction.coefficientsCount();
/* 166 */     int mutatingNodeCoefficientsCount = mutatingNode.getCoefficientsOfNode().size();
/* 167 */     if (functionCoefficientsCount > mutatingNodeCoefficientsCount) {
/* 168 */       for (int i = 0; i < functionCoefficientsCount - mutatingNodeCoefficientsCount + 1; i++) {
/* 169 */         mutatingNode.addCoefficient(this.context.getRandomValue());
/*     */       }
/* 171 */     } else if (functionCoefficientsCount < mutatingNodeCoefficientsCount) {
/* 172 */       List<Double> subList = new ArrayList(functionCoefficientsCount);
/* 173 */       for (int i = 0; i < functionCoefficientsCount; i++) {
/* 174 */         subList.add(mutatingNode.getCoefficientsOfNode().get(i));
/*     */       }
/* 176 */       mutatingNode.setCoefficientsOfNode(subList);
/*     */     }
/*     */   }
/*     */   
/*     */   private void mutateByReverseOfChildsList() {
/* 181 */     Expression mutatingNode = getRandomNode(this.syntaxTree);
/* 182 */     Function mutatingNodeFunction = mutatingNode.getFunction();
/*     */     
/* 184 */     if ((mutatingNode.getChilds().size() > 1) && (!mutatingNodeFunction.isCommutative()))
/*     */     {
/*     */ 
/* 187 */       Collections.reverse(mutatingNode.getChilds());
/*     */     }
/*     */     else {
/* 190 */       mutateByRandomChangeOfFunction();
/*     */     }
/*     */   }
/*     */   
/*     */   private void mutateByRandomChangeOfChild() {
/* 195 */     Expression mutatingNode = getRandomNode(this.syntaxTree);
/*     */     
/* 197 */     if (!mutatingNode.getChilds().isEmpty())
/*     */     {
/* 199 */       int indx = this.random.nextInt(mutatingNode.getChilds().size());
/*     */       
/* 201 */       mutatingNode.getChilds().set(indx, SyntaxTreeUtils.createTree(1, this.context));
/*     */     }
/*     */     else {
/* 204 */       mutateByRandomChangeOfFunction();
/*     */     }
/*     */   }
/*     */   
/*     */   private void mutateByRandomChangeOfNodeToChild() {
/* 209 */     Expression mutatingNode = getRandomNode(this.syntaxTree);
/*     */     
/* 211 */     if (!mutatingNode.getChilds().isEmpty())
/*     */     {
/* 213 */       int indx = this.random.nextInt(mutatingNode.getChilds().size());
/*     */       
/* 215 */       Expression child = (Expression)mutatingNode.getChilds().get(indx);
/*     */       
/* 217 */       swapNode(mutatingNode, child.clone());
/*     */     }
/*     */     else {
/* 220 */       mutateByRandomChangeOfFunction();
/*     */     }
/*     */   }
/*     */   
/*     */   private Expression getRandomNode(Expression tree) {
/* 225 */     List<Expression> allNodesOfTree = tree.getAllNodesAsList();
/* 226 */     int allNodesOfTreeCount = allNodesOfTree.size();
/* 227 */     int indx = this.random.nextInt(allNodesOfTreeCount);
/* 228 */     return (Expression)allNodesOfTree.get(indx);
/*     */   }
/*     */   
/*     */   private void swapNode(Expression oldNode, Expression newNode) {
/* 232 */     oldNode.setChilds(newNode.getChilds());
/* 233 */     oldNode.setFunction(newNode.getFunction());
/* 234 */     oldNode.setCoefficientsOfNode(newNode.getCoefficientsOfNode());
/* 235 */     oldNode.setVariable(newNode.getVariable());
/*     */   }
/*     */   
/*     */   public void optimizeTree() {
/* 239 */     optimizeTree(70);
/*     */   }
/*     */   
/*     */   public void optimizeTree(int iterations)
/*     */   {
/* 244 */     SyntaxTreeUtils.cutTree(this.syntaxTree, this.context, 6);
/* 245 */     SyntaxTreeUtils.simplifyTree(this.syntaxTree, this.context);
/*     */     
/* 247 */     List<Double> coefficientsOfTree = this.syntaxTree.getCoefficientsOfTree();
/*     */     
/* 249 */     if (coefficientsOfTree.size() > 0) {
/* 250 */       CoefficientsChromosome initialChromosome = new CoefficientsChromosome(coefficientsOfTree, 0.6D);
/* 251 */       Population<CoefficientsChromosome> population = new Population();
/* 252 */       for (int i = 0; i < 5; i++) {
/* 253 */         population.addChromosome(initialChromosome.mutate());
/*     */       }
/* 255 */       population.addChromosome(initialChromosome);
/*     */       
/* 257 */       Fitness<CoefficientsChromosome, Double> fit = new CoefficientsFitness();
/*     */       
/* 259 */       GeneticAlgorithm<CoefficientsChromosome, Double> env = new GeneticAlgorithm(population, fit);
/*     */       
/* 261 */       env.evolve(iterations);
/*     */       
/* 263 */       List<Double> optimizedCoefficients = ((CoefficientsChromosome)env.getBest()).getCoefficients();
/*     */       
/* 265 */       this.syntaxTree.setCoefficientsOfTree(optimizedCoefficients);
/*     */     }
/*     */   }
/*     */   
/*     */   public Context getContext() {
/* 270 */     return this.context;
/*     */   }
/*     */   
/*     */   public void setContext(Context context) {
/* 274 */     this.context = context;
/*     */   }
/*     */   
/*     */   public Expression getSyntaxTree() {
/* 278 */     return this.syntaxTree;
/*     */   }
/*     */   
/*     */   private class CoefficientsChromosome
/*     */     implements Chromosome<CoefficientsChromosome>, Cloneable
/*     */   {
/*     */     private double pMutation;
/*     */     private double pCrossover;
/*     */     private List<Double> coefficients;
/*     */     
/*     */     public CoefficientsChromosome(List<Double> coefficients, double arg4)
/*     */     {
/* 290 */       this.coefficients = coefficients;
/* 291 */       this.pMutation = pMutation;
/* 292 */       this.pCrossover = pCrossover;
/*     */     }
/*     */     
/*     */     public List<CoefficientsChromosome> crossover(CoefficientsChromosome anotherChromosome)
/*     */     {
/* 297 */       List<CoefficientsChromosome> ret = new ArrayList(2);
/*     */       
/* 299 */       CoefficientsChromosome thisClone = clone();
/* 300 */       CoefficientsChromosome anotherClone = anotherChromosome.clone();
/*     */       
/* 302 */       for (int i = 0; i < thisClone.coefficients.size(); i++) {
/* 303 */         if (GpChromosome.this.random.nextDouble() > this.pCrossover) {
/* 304 */           thisClone.coefficients.set(i, anotherChromosome.coefficients.get(i));
/* 305 */           anotherClone.coefficients.set(i, this.coefficients.get(i));
/*     */         }
/*     */       }
/* 308 */       ret.add(thisClone);
/* 309 */       ret.add(anotherClone);
/*     */       
/* 311 */       return ret;
/*     */     }
/*     */     
/*     */     public CoefficientsChromosome mutate()
/*     */     {
/* 316 */       CoefficientsChromosome ret = clone();
/* 317 */       for (int i = 0; i < ret.coefficients.size(); i++) {
/* 318 */         if (GpChromosome.this.random.nextDouble() > this.pMutation) {
/* 319 */           double coeff = ((Double)ret.coefficients.get(i)).doubleValue();
/* 320 */           coeff += GpChromosome.this.context.getRandomMutationValue();
/* 321 */           ret.coefficients.set(i, Double.valueOf(coeff));
/*     */         }
/*     */       }
/* 324 */       return ret;
/*     */     }
/*     */     
/*     */     protected CoefficientsChromosome clone()
/*     */     {
/* 329 */       List<Double> ret = new ArrayList(this.coefficients.size());
/* 330 */       for (Iterator i$ = this.coefficients.iterator(); i$.hasNext();) { double d = ((Double)i$.next()).doubleValue();
/* 331 */         ret.add(Double.valueOf(d));
/*     */       }
/* 333 */       return new CoefficientsChromosome(ret, this.pMutation);
/*     */     }
/*     */     
/*     */     public List<Double> getCoefficients() {
/* 337 */       return this.coefficients;
/*     */     }
/*     */   }
/*     */   
/*     */   private class CoefficientsFitness implements Fitness<GpChromosome.CoefficientsChromosome, Double>
/*     */   {
/*     */     private CoefficientsFitness() {}
/*     */     
/*     */     public Double calculate(GpChromosome.CoefficientsChromosome chromosome) {
/* 346 */       GpChromosome.this.syntaxTree.setCoefficientsOfTree(chromosome.getCoefficients());
/* 347 */       return (Double)GpChromosome.this.fitnessFunction.calculate(GpChromosome.this);
/*     */     }
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\GpChromosome.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */