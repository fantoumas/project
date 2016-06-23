/*    */ package com.lagodiuk.gp.symbolic;
/*    */ 
/*    */ import com.lagodiuk.ga.Fitness;
/*    */ import com.lagodiuk.ga.GeneticAlgorithm;
/*    */ import com.lagodiuk.ga.IterartionListener;
/*    */ import com.lagodiuk.ga.Population;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Context;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.Function;
/*    */ import com.lagodiuk.gp.symbolic.interpreter.SyntaxTreeUtils;
/*    */ import java.util.Collection;
/*    */ import java.util.List;
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
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ 
/*    */ public class SymbolicRegressionEngine
/*    */ {
/*    */   private static final int INITIAL_PARENT_CHROMOSOMES_SURVIVE_COUNT = 1;
/*    */   private static final int DEFAULT_POPULATION_SIZE = 5;
/*    */   private static final int MAX_INITIAL_TREE_DEPTH = 1;
/*    */   private GeneticAlgorithm<GpChromosome, Double> environment;
/*    */   private Context context;
/*    */   private ExpressionFitness expressionFitness;
/*    */   
/*    */   public SymbolicRegressionEngine(ExpressionFitness expressionFitness, Collection<String> variables, List<? extends Function> baseFunctions)
/*    */   {
/* 45 */     this.context = new Context(baseFunctions, variables);
/* 46 */     this.expressionFitness = expressionFitness;
/* 47 */     SymbolicRegressionFitness fitnessFunction = new SymbolicRegressionFitness(this.expressionFitness);
/* 48 */     Population<GpChromosome> population = createPopulation(this.context, fitnessFunction, 5);
/* 49 */     this.environment = new GeneticAlgorithm<GpChromosome, Double>(population, fitnessFunction);
/* 50 */     this.environment.setParentChromosomesSurviveCount(1);
/*    */   }
/*    */   
/*    */   private Population<GpChromosome> createPopulation(Context context, Fitness<GpChromosome, Double> fitnessFunction, int populationSize) {
/* 54 */     Population<GpChromosome> population = new Population<GpChromosome>();
/* 55 */     for (int i = 0; i < populationSize; i++) {
/* 56 */       GpChromosome chromosome = new GpChromosome(context, fitnessFunction, SyntaxTreeUtils.createTree(1, context));
/*    */       
/* 58 */       population.addChromosome(chromosome);
/*    */     }
/* 60 */     return population;
/*    */   }
/*    */   
/*    */   public void addIterationListener(final SymbolicRegressionIterationListener listener) {
/* 64 */     this.environment.addIterationListener(new IterartionListener()
/*    */     {
        @Override
        public void update(GeneticAlgorithm paramGeneticAlgorithm) {

        }

        /*    */       public void update(GeneticAlgorithm<GpChromosome, Double> environment) {
/* 67 */         listener.update(SymbolicRegressionEngine.this);
/*    */       }
/*    */     });
/*    */   }
/*    */   
/*    */   public void evolve(int itrationsCount) {
/* 73 */     this.environment.evolve(itrationsCount);
/*    */   }
/*    */   
/*    */   public Context getContext() {
/* 77 */     return this.context;
/*    */   }
/*    */   
/*    */   public Expression getBestSyntaxTree() {
/* 81 */     return ((GpChromosome)this.environment.getBest()).getSyntaxTree();
/*    */   }
/*    */   
/*    */   public double fitness(Expression expression) {
/* 85 */     return this.expressionFitness.fitness(expression, this.context);
/*    */   }
/*    */   
/*    */   public void terminate() {
/* 89 */     this.environment.terminate();
/*    */   }
/*    */   
/*    */   public int getIteration() {
/* 93 */     return this.environment.getIteration();
/*    */   }
/*    */   
/*    */   public void setParentsSurviveCount(int n) {
/* 97 */     this.environment.setParentChromosomesSurviveCount(n);
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\SymbolicRegressionEngine.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */