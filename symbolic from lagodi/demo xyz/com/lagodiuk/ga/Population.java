/*    */ package com.lagodiuk.ga;
/*    */ 
/*    */ import java.util.ArrayList;
/*    */ import java.util.Collections;
/*    */ import java.util.Comparator;
/*    */ import java.util.Iterator;
/*    */ import java.util.List;
/*    */ import java.util.Random;
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
/*    */ public class Population<C extends Chromosome<C>>
/*    */   implements Iterable<C>
/*    */ {
/*    */   private static final int DEFAULT_NUMBER_OF_CHROMOSOMES = 32;
/* 29 */   private List<C> chromosomes = new ArrayList(32);
/*    */   
/* 31 */   private final Random random = new Random();
/*    */   
/*    */   public void addChromosome(C chromosome) {
/* 34 */     this.chromosomes.add(chromosome);
/*    */   }
/*    */   
/*    */   public int getSize() {
/* 38 */     return this.chromosomes.size();
/*    */   }
/*    */   
/*    */   public C getRandomChromosome() {
/* 42 */     int numOfChromosomes = this.chromosomes.size();
/*    */     
/*    */ 
/* 45 */     int indx = this.random.nextInt(numOfChromosomes);
/* 46 */     return (Chromosome)this.chromosomes.get(indx);
/*    */   }
/*    */   
/*    */   public C getChromosomeByIndex(int indx) {
/* 50 */     return (Chromosome)this.chromosomes.get(indx);
/*    */   }
/*    */   
/*    */   public void sortPopulationByFitness(Comparator<C> chromosomesComparator) {
/* 54 */     Collections.shuffle(this.chromosomes);
/* 55 */     Collections.sort(this.chromosomes, chromosomesComparator);
/*    */   }
/*    */   
/*    */ 
/*    */ 
/*    */   public void trim(int len)
/*    */   {
/* 62 */     this.chromosomes = this.chromosomes.subList(0, len);
/*    */   }
/*    */   
/*    */   public Iterator<C> iterator()
/*    */   {
/* 67 */     return this.chromosomes.iterator();
/*    */   }
/*    */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\ga\Population.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */