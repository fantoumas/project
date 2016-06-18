package com.lagodiuk.gp.symbolic;

import com.lagodiuk.gp.symbolic.interpreter.Context;
import com.lagodiuk.gp.symbolic.interpreter.Expression;

public abstract interface ExpressionFitness
{
  public abstract double fitness(Expression paramExpression, Context paramContext);
}


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\ExpressionFitness.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */