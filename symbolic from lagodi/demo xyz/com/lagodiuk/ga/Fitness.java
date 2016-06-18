package com.lagodiuk.ga;

public abstract interface Fitness<C extends Chromosome<C>, T extends Comparable<T>>
{
  public abstract T calculate(C paramC);
}


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\ga\Fitness.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */