/*     */ import com.lagodiuk.ga.Chromosome;
/*     */ import com.lagodiuk.ga.Fitness;
/*     */ import com.lagodiuk.ga.GeneticAlgorithm;
/*     */ import com.lagodiuk.ga.IterartionListener;
/*     */ import com.lagodiuk.ga.Population;
/*     */
/*     */ import java.util.Arrays;
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
/*     */ public class Demo
/*     */ {
/*     */   public static void main(String[] args)
/*     */   {
/*  29 */     Population<Demo.MyVector> population = createInitialPopulation(5);
/*     */     
/*  31 */     Fitness<Demo.MyVector, Double> fitness = new Demo.MyVectorFitness();
/*     */     
/*  33 */     GeneticAlgorithm<Demo.MyVector, Double> ga = new GeneticAlgorithm<MyVector, Double>(population, fitness);
/*     */     
/*  35 */     addListener(ga);
/*     */     
/*  37 */     ga.evolve(500);
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */   private static Population<Demo.MyVector> createInitialPopulation(int populationSize)
/*     */   {
/*  45 */     Population<Demo.MyVector> population = new Population<MyVector>();
/*  46 */     Demo.MyVector base = new Demo.MyVector();
/*  47 */     for (int i = 0; i < populationSize; i++)
/*     */     {
/*     */ 
/*  50 */       Demo.MyVector chr = base.mutate();
/*  51 */       population.addChromosome(chr);
/*     */     }
/*  53 */     return population;
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */   private static void addListener(GeneticAlgorithm<Demo.MyVector, Double> ga)
/*     */   {
/*  61 */     System.out.println(String.format("%s\t%s\t%s", new Object[] { "iter", "fit", "chromosome" }));
/*     */     
/*     */ 
/*  64 */     ga.addIterationListener(new IterartionListener()
/*     */     {
        @Override
        public void update(GeneticAlgorithm paramGeneticAlgorithm) {

        }

        /*  66 */       private final double threshold = 1.0E-5D;
/*     */       
/*     */ 
/*     */       public void update(GeneticAlgorithm<Demo.MyVector, Double> ga)
/*     */       {
/*  71 */         Demo.MyVector best = (Demo.MyVector)ga.getBest();
/*  72 */         double bestFit = ((Double)ga.fitness(best)).doubleValue();
/*  73 */         int iteration = ga.getIteration();
/*     */         
/*     */ 
/*  76 */         System.out.println(String.format("%s\t%s\t%s", new Object[] { Integer.valueOf(iteration), Double.valueOf(bestFit), best }));
/*     */         
/*     */ 
/*  79 */         getClass(); if (bestFit < 1.0E-5D) {
/*  80 */           ga.terminate();
/*     */         }
/*     */       }
/*     */     });
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */   public static class MyVector
/*     */     implements Chromosome<MyVector>, Cloneable
/*     */   {
/*  91 */     private static final Random random = new Random();
/*     */     
/*  93 */     private final int[] vector = new int[5];
/*     */     
/*     */ 
/*     */ 
/*     */ 
/*     */     public MyVector mutate()
/*     */     {
/* 100 */       MyVector result = clone();
/*     */       
/*     */ 
/*     */ 
/* 104 */       int index = random.nextInt(this.vector.length);
/* 105 */       int mutationValue = random.nextInt(3) - random.nextInt(3);
/* 106 */       result.vector[index] += mutationValue;
/*     */       
/* 108 */       return result;
/*     */     }
/*     */     
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */     public List<MyVector> crossover(MyVector other)
/*     */     {
/* 118 */       MyVector thisClone = clone();
/* 119 */       MyVector otherClone = other.clone();
/*     */       
/*     */ 
/* 122 */       int index = random.nextInt(this.vector.length - 1);
/* 123 */       for (int i = index; i < this.vector.length; i++) {
/* 124 */         int tmp = thisClone.vector[i];
/* 125 */         thisClone.vector[i] = otherClone.vector[i];
/* 126 */         otherClone.vector[i] = tmp;
/*     */       }
/*     */       
/* 129 */       return Arrays.asList(new MyVector[] { thisClone, otherClone });
/*     */     }
/*     */     
/*     */     protected MyVector clone()
/*     */     {
/* 134 */       MyVector clone = new MyVector();
/* 135 */       System.arraycopy(this.vector, 0, clone.vector, 0, this.vector.length);
/* 136 */       return clone;
/*     */     }
/*     */     
/*     */     public int[] getVector() {
/* 140 */       return this.vector;
/*     */     }
/*     */     
/*     */     public String toString()
/*     */     {
/* 145 */       return Arrays.toString(this.vector);
/*     */     }
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */   public static class MyVectorFitness
/*     */     implements Fitness<Demo.MyVector, Double>
/*     */   {
/* 155 */     private final int[] target = { 10, 20, 30, 40, 50 };
/*     */     
/*     */     public Double calculate(Demo.MyVector chromosome)
/*     */     {
/* 159 */       double delta = 0.0D;
/* 160 */       int[] v = chromosome.getVector();
/* 161 */       for (int i = 0; i < 5; i++) {
/* 162 */         delta += sqr(v[i] - this.target[i]);
/*     */       }
/* 164 */       return Double.valueOf(delta);
/*     */     }
/*     */     
/*     */     private double sqr(double x) {
/* 168 */       return x * x;
/*     */     }
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\Demo.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */