/*     */ package com.lagodiuk.ga;
/*     */ 
/*     */ import java.util.Comparator;
/*     */ import java.util.LinkedList;
/*     */ import java.util.List;
/*     */ import java.util.Map;
/*     */ import java.util.WeakHashMap;
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
/*     */ public class GeneticAlgorithm<C extends Chromosome<C>, T extends Comparable<T>>
/*     */ {
/*     */   private static final int ALL_PARENTAL_CHROMOSOMES = Integer.MAX_VALUE;
/*     */   private final GeneticAlgorithm<C, T>.ChromosomesComparator chromosomesComparator;
/*     */   private final Fitness<C, T> fitnessFunc;
/*     */   private Population<C> population;
/*     */   
/*     */   private class ChromosomesComparator
/*     */     implements Comparator<C>
/*     */   {
/*  30 */     private final Map<C, T> cache = new WeakHashMap();
/*     */     
/*     */     private ChromosomesComparator() {}
/*     */     
/*  34 */     public int compare(C chr1, C chr2) { T fit1 = fit(chr1);
/*  35 */       T fit2 = fit(chr2);
/*  36 */       int ret = fit1.compareTo(fit2);
/*  37 */       return ret;
/*     */     }
/*     */     
/*     */     public T fit(C chr) {
/*  41 */       T fit = (T) this.cache.get(chr);
/*  42 */       if (fit == null) {
/*  43 */         fit = GeneticAlgorithm.this.fitnessFunc.calculate(chr);
/*  44 */         this.cache.put(chr, fit);
/*     */       }
/*  46 */       return fit;
/*     */     }
/*     */     
/*     */     public void clearCache() {
/*  50 */       this.cache.clear();
/*     */     }
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*  61 */   private final List<IterartionListener<C, T>> iterationListeners = new LinkedList();
/*     */   
/*  63 */   private boolean terminate = false;
/*     */   
/*     */ 
/*     */ 
/*  67 */   private int parentChromosomesSurviveCount = Integer.MAX_VALUE;
/*     */   
/*  69 */   private int iteration = 0;
/*     */   
/*     */   public GeneticAlgorithm(Population<C> population, Fitness<C, T> fitnessFunc) {
/*  72 */     this.population = population;
/*  73 */     this.fitnessFunc = fitnessFunc;
/*  74 */     this.chromosomesComparator = new ChromosomesComparator();
/*  75 */     this.population.sortPopulationByFitness(this.chromosomesComparator);
/*     */   }
/*     */   
/*     */   public void evolve() {
/*  79 */     int parentPopulationSize = this.population.getSize();
/*     */     
/*  81 */     Population<C> newPopulation = new Population();
/*     */     
/*  83 */     for (int i = 0; (i < parentPopulationSize) && (i < this.parentChromosomesSurviveCount); i++) {
/*  84 */       newPopulation.addChromosome(this.population.getChromosomeByIndex(i));
/*     */     }
/*     */     
/*  87 */     for (int i = 0; i < parentPopulationSize; i++) {
/*  88 */       C chromosome = this.population.getChromosomeByIndex(i);
/*  89 */       C mutated = chromosome.mutate();
/*     */       
/*  91 */       C otherChromosome = this.population.getRandomChromosome();
/*  92 */       List<C> crossovered = chromosome.crossover(otherChromosome);
/*     */       
/*  94 */       newPopulation.addChromosome(mutated);
/*  95 */       for (C c : crossovered) {
/*  96 */         newPopulation.addChromosome(c);
/*     */       }
/*     */     }
/*     */     
/* 100 */     newPopulation.sortPopulationByFitness(this.chromosomesComparator);
/* 101 */     newPopulation.trim(parentPopulationSize);
/* 102 */     this.population = newPopulation;
/*     */   }
/*     */   
/*     */   public void evolve(int count) {
/* 106 */     this.terminate = false;
/*     */     
/* 108 */     for (int i = 0; i < count; i++) {
/* 109 */       if (this.terminate) {
/*     */         break;
/*     */       }
/* 112 */       evolve();
/* 113 */       this.iteration = i;
/* 114 */       for (IterartionListener<C, T> l : this.iterationListeners) {
/* 115 */         l.update(this);
/*     */       }
/*     */     }
/*     */   }
/*     */   
/*     */   public int getIteration() {
/* 121 */     return this.iteration;
/*     */   }
/*     */   
/*     */   public void terminate() {
/* 125 */     this.terminate = true;
/*     */   }
/*     */   
/*     */   public Population<C> getPopulation() {
/* 129 */     return this.population;
/*     */   }
/*     */   
/*     */   public C getBest() {
/* 133 */     return this.population.getChromosomeByIndex(0);
/*     */   }
/*     */   
/*     */   public C getWorst() {
/* 137 */     return this.population.getChromosomeByIndex(this.population.getSize() - 1);
/*     */   }
/*     */   
/*     */   public void setParentChromosomesSurviveCount(int parentChromosomesCount) {
/* 141 */     this.parentChromosomesSurviveCount = parentChromosomesCount;
/*     */   }
/*     */   
/*     */   public int getParentChromosomesSurviveCount() {
/* 145 */     return this.parentChromosomesSurviveCount;
/*     */   }
/*     */   
/*     */   public void addIterationListener(IterartionListener<C, T> listener) {
/* 149 */     this.iterationListeners.add(listener);
/*     */   }
/*     */   
/*     */   public void removeIterationListener(IterartionListener<C, T> listener) {
/* 153 */     this.iterationListeners.remove(listener);
/*     */   }
/*     */   
/*     */   public T fitness(C chromosome) {
/* 157 */     return this.chromosomesComparator.fit(chromosome);
/*     */   }
/*     */   
/*     */   public void clearCache() {
/* 161 */     this.chromosomesComparator.clearCache();
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\ga\GeneticAlgorithm.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */