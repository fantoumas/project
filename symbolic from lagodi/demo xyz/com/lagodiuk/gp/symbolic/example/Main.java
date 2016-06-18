/*     */ package com.lagodiuk.gp.symbolic.example;
/*     */ 
/*     */ import com.lagodiuk.gp.symbolic.SymbolicRegressionEngine;
/*     */ import com.lagodiuk.gp.symbolic.SymbolicRegressionIterationListener;
/*     */ import com.lagodiuk.gp.symbolic.TabulatedFunctionFitness;
/*     */ import com.lagodiuk.gp.symbolic.Target;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.Expression;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.Function;
/*     */ import com.lagodiuk.gp.symbolic.interpreter.Functions;
/*     */ import java.io.BufferedReader;
/*     */ import java.io.FileInputStream;
/*     */ import java.io.FileNotFoundException;
/*     */ import java.io.InputStreamReader;
/*     */ import java.io.PrintStream;
/*     */ import java.io.PrintWriter;
/*     */ import java.text.NumberFormat;
/*     */ import java.util.ArrayList;
/*     */ import java.util.Date;
/*     */ import java.util.HashSet;
/*     */ import java.util.LinkedList;
/*     */ import java.util.List;
/*     */ import java.util.Locale;
/*     */ import java.util.Set;
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
/*     */ public class Main
/*     */ {
/*  42 */   private static NumberFormat numberFormat = NumberFormat.getInstance(Locale.US);
/*     */   
/*     */   private static FileInputStream fileIn;
/*     */   
/*     */   private static PrintWriter fileOut;
/*     */   
/*  48 */   private static int iteration = 1;
/*     */   
/*  50 */   private static boolean evolved = false;
/*     */   
/*  52 */   private static double threshold = 10.0D;
/*     */   
/*     */   public static void main(String[] args) throws Exception {
/*  55 */     System.out.println("Symbolic regression solver");
/*     */     
/*  57 */     configureInputOutput(args);
/*  58 */     BufferedReader inputReader = new BufferedReader(new InputStreamReader(fileIn));
/*     */     
/*  60 */     List<Function> functions = getFunctions(inputReader);
/*  61 */     List<String> variables = getVariables(inputReader);
/*  62 */     TabulatedFunctionFitness fitness = getTrainingData(inputReader, variables);
/*     */     
/*  64 */     SymbolicRegressionEngine engine = new SymbolicRegressionEngine(fitness, variables, functions);
/*     */     
/*  66 */     String prefix = makePrefix(variables);
/*  67 */     engine.addIterationListener(new SymbolicRegressionIterationListener() {
/*  68 */       private double prevFitValue = -1.0D;
/*     */       
/*     */       public void update(SymbolicRegressionEngine engine)
/*     */       {
/*  72 */         Expression bestSyntaxTree = engine.getBestSyntaxTree();
/*  73 */         double currFitValue = engine.fitness(bestSyntaxTree);
/*  74 */         if (Double.compare(currFitValue, this.prevFitValue) != 0) {
/*  75 */           Main.access$000();
/*  76 */           Main.outPrintln(this.val$prefix + bestSyntaxTree.print());
/*     */         }
/*     */         
/*  79 */         Main.outPrintln(String.format("%s \t %s", new Object[] { Integer.valueOf(Main.iteration), Double.valueOf(currFitValue) }));
/*  80 */         Main.access$204();
/*  81 */         this.prevFitValue = currFitValue;
/*  82 */         if (currFitValue < Main.threshold) {
/*  83 */           engine.terminate();
/*  84 */           Main.access$402(true);
/*     */         }
/*     */         
/*     */       }
/*  88 */     });
/*  89 */     outPrintln();
/*  90 */     outPrintln(String.format("Start time is: %s", new Object[] { new Date() }));
/*     */     
/*  92 */     BufferedReader systemIn = new BufferedReader(new InputStreamReader(System.in));
/*     */     for (;;) {
/*  94 */       engine.evolve(50);
/*  95 */       boolean terminate = true;
/*  96 */       if (!evolved) {
/*  97 */         System.out.println("Continue? (50 iterations) Y/N (don't forget to press Enter)");
/*  98 */         String s = systemIn.readLine();
/*  99 */         if ("y".equalsIgnoreCase(s)) {
/* 100 */           terminate = false;
/*     */         }
/*     */       }
/* 103 */       if (terminate) {
/*     */         break;
/*     */       }
/*     */     }
/*     */     
/* 108 */     outPrintln();
/* 109 */     outPrintln("Best function is:");
/* 110 */     outPrintln(prefix + engine.getBestSyntaxTree().print());
/* 111 */     outPrintln();
/* 112 */     outPrintln(String.format("End time is: %s", new Object[] { new Date() }));
/* 113 */     outPrintln();
/*     */     
/* 115 */     closeInOut();
/*     */   }
/*     */   
/*     */   private static String makePrefix(List<String> variables) {
/* 119 */     String vars = variables.toString();
/* 120 */     vars = vars.substring(1, vars.length() - 1);
/* 121 */     return String.format("f(%s) = ", new Object[] { vars });
/*     */   }
/*     */   
/*     */   private static List<String> getVariables(BufferedReader inputReader) throws Exception {
/* 125 */     List<String> variables = new ArrayList();
/* 126 */     String s = inputReader.readLine();
/* 127 */     while ((s.startsWith("#")) || (s.trim().isEmpty())) {
/* 128 */       s = inputReader.readLine();
/*     */     }
/* 130 */     s = s.replaceAll("f\\((.*)\\).*", "$1").trim();
/* 131 */     for (String variableName : s.split("\\,")) {
/* 132 */       variables.add(variableName.trim());
/*     */     }
/* 134 */     return variables;
/*     */   }
/*     */   
/*     */   private static List<Function> getFunctions(BufferedReader inputReader) throws Exception {
/* 138 */     Set<Function> functions = new HashSet();
/* 139 */     functions.add(Functions.CONSTANT);
/* 140 */     functions.add(Functions.VARIABLE);
/* 141 */     String s = inputReader.readLine();
/* 142 */     while ((s.startsWith("#")) || (s.trim().isEmpty())) {
/* 143 */       s = inputReader.readLine();
/*     */     }
/* 145 */     for (String functionName : s.split("\\s+")) {
/* 146 */       Function f = Functions.valueOf(functionName);
/* 147 */       functions.add(f);
/*     */     }
/* 149 */     List<Function> functionsList = new ArrayList(functions);
/* 150 */     return functionsList;
/*     */   }
/*     */   
/*     */   private static TabulatedFunctionFitness getTrainingData(BufferedReader inputReader, List<String> variables) throws Exception
/*     */   {
/* 155 */     List<Target> targets = new LinkedList();
/* 156 */     String s = inputReader.readLine();
/* 157 */     while ((s.startsWith("#")) || (s.trim().isEmpty())) {
/* 158 */       s = inputReader.readLine();
/*     */     }
/* 160 */     int variablesCount = variables.size();
/* 161 */     while (s != null)
/* 162 */       if ((s.startsWith("#")) || (s.trim().isEmpty())) {
/* 163 */         s = inputReader.readLine();
/*     */ 
/*     */ 
/*     */       }
/* 167 */       else if (s.matches("[Tt]hreshold.*")) {
/* 168 */         s = s.replaceAll("[Tt]hreshold\\s*=(.*)", "$1").trim();
/* 169 */         threshold = numberFormat.parse(s).doubleValue();
/* 170 */         s = inputReader.readLine();
/*     */       }
/*     */       else
/*     */       {
/* 174 */         String[] split = s.split("=");
/* 175 */         String left = split[1].trim();
/* 176 */         String right = split[0].trim();
/* 177 */         right = right.replaceAll("f\\((.*)\\)", "$1");
/*     */         
/* 179 */         double targetValue = numberFormat.parse(left).doubleValue();
/*     */         
/* 181 */         String[] values = right.split("\\,");
/* 182 */         Target target = new Target();
/* 183 */         for (int i = 0; i < variablesCount; i++) {
/* 184 */           double value = numberFormat.parse(values[i].trim()).doubleValue();
/* 185 */           target.when((String)variables.get(i), value);
/*     */         }
/* 187 */         target.targetIs(targetValue);
/* 188 */         targets.add(target);
/*     */         
/* 190 */         s = inputReader.readLine();
/*     */       }
/* 192 */     return new TabulatedFunctionFitness(targets);
/*     */   }
/*     */   
/*     */   private static void configureInputOutput(String[] args) throws FileNotFoundException {
/* 196 */     switch (args.length) {
/*     */     case 1: 
/* 198 */       fileIn = new FileInputStream(args[0]);
/* 199 */       break;
/*     */     
/*     */     case 2: 
/* 202 */       fileIn = new FileInputStream(args[0]);
/* 203 */       fileOut = new PrintWriter(args[1]);
/*     */     }
/*     */   }
/*     */   
/*     */   private static void outPrintln()
/*     */   {
/* 209 */     System.out.println();
/* 210 */     if (fileOut != null) {
/* 211 */       fileOut.println();
/*     */     }
/*     */   }
/*     */   
/*     */   private static void outPrintln(String message) {
/* 216 */     System.out.println(message);
/* 217 */     if (fileOut != null) {
/* 218 */       fileOut.println(message);
/*     */     }
/*     */   }
/*     */   
/*     */   private static void closeInOut() throws Exception {
/* 223 */     if (fileIn != null) {
/* 224 */       fileIn.close();
/*     */     }
/* 226 */     if (fileOut != null) {
/* 227 */       fileOut.close();
/*     */     }
/*     */   }
/*     */ }


/* Location:              C:\Users\Christina\Desktop\Uni\Project\symbolic from lagodi\genetic-programming\symbolic_regression_1.0.jar!\com\lagodiuk\gp\symbolic\example\Main.class
 * Java compiler version: 6 (50.0)
 * JD-Core Version:       0.7.1
 */