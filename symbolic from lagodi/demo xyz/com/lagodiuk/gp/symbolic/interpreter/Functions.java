package com.lagodiuk.gp.symbolic.interpreter;

import java.util.LinkedList;
import java.util.List;

public enum Functions
  implements Function
{
  CONSTANT,  VARIABLE,  ADD,  SUB,  MUL,  DIV,  SQRT,  POW,  LN,  SIN,  COS;
  
  private Functions() {}
}


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\interpreter\Functions.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */