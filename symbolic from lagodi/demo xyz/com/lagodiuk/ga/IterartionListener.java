package com.lagodiuk.ga;

public abstract interface IterartionListener<C extends Chromosome<C>, T extends Comparable<T>>
{
  public abstract void update(GeneticAlgorithm<C, T> paramGeneticAlgorithm);
}


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\ga\IterartionListener.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */