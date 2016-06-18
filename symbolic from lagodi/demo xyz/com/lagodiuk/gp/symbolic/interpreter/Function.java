package com.lagodiuk.gp.symbolic.interpreter;

import java.util.List;

public abstract interface Function
{
  public abstract double eval(Expression paramExpression, Context paramContext);
  
  public abstract int argumentsCount();
  
  public abstract boolean isVariable();
  
  public abstract boolean isNumber();
  
  public abstract boolean isCommutative();
  
  public abstract String print(Expression paramExpression);
  
  public abstract List<Double> getCoefficients(Expression paramExpression);
  
  public abstract void setCoefficients(Expression paramExpression, List<Double> paramList, int paramInt);
  
  public abstract int coefficientsCount();
}


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\interpreter\Function.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */