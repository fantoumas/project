package com.lagodiuk.ga;

import java.util.List;

public abstract interface Chromosome<C extends Chromosome<C>>
{
  public abstract List<C> crossover(C paramC);
  
  public abstract C mutate();
}


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\ga\Chromosome.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       0.7.1
 */