/*     */ import com.lagodiuk.ga.Chromosome;
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
/*     */ public class MyVector
/*     */   implements Chromosome<MyVector>, Cloneable
/*     */ {
/*  91 */   private static final Random random = new Random();
/*     */   
/*  93 */   private final int[] vector = new int[5];
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */   public MyVector mutate()
/*     */   {
/* 100 */     MyVector result = clone();
/*     */     
/*     */ 
/*     */ 
/* 104 */     int index = random.nextInt(this.vector.length);
/* 105 */     int mutationValue = random.nextInt(3) - random.nextInt(3);
/* 106 */     result.vector[index] += mutationValue;
/*     */     
/* 108 */     return result;
/*     */   }
/*     */   
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */ 
/*     */   public List<MyVector> crossover(MyVector other)
/*     */   {
/* 118 */     MyVector thisClone = clone();
/* 119 */     MyVector otherClone = other.clone();
/*     */     
/*     */ 
/* 122 */     int index = random.nextInt(this.vector.length - 1);
/* 123 */     for (int i = index; i < this.vector.length; i++) {
/* 124 */       int tmp = thisClone.vector[i];
/* 125 */       thisClone.vector[i] = otherClone.vector[i];
/* 126 */       otherClone.vector[i] = tmp;
/*     */     }
/*     */     
/* 129 */     return Arrays.asList(new MyVector[] { thisClone, otherClone });
/*     */   }
/*     */   
/*     */   protected MyVector clone()
/*     */   {
/* 134 */     MyVector clone = new MyVector();
/* 135 */     System.arraycopy(this.vector, 0, clone.vector, 0, this.vector.length);
/* 136 */     return clone;
/*     */   }
/*     */   
/*     */   public int[] getVector() {
/* 140 */     return this.vector;
/*     */   }
/*     */   
/*     */   public String toString()
/*     */   {
/* 145 */     return Arrays.toString(this.vector);
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\Demo$MyVector.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */