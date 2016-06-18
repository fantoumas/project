import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

import static examples.gp.symbolicRegression.SymbolicRegression.ignoreVariables;


/**
 * Created by Christina on 16/6/2016.
 */
public class ReadFile {


    public static ArrayList<Double> constants = new ArrayList<Double>();

    // size of data
    public static int numRows;

    // the data (as Double)
    // Note: the last row is the output variable per default
    protected static Double[][] data;

    // If we have found a perfect solution.
    public static boolean foundPerfect  = false;
    public static int numInputVariables;
    public static Integer outputVariable; // default last
    public static String[] variableNames;

    // standard GP parameters
    public static int minInitDepth      = 2;
    public static int maxInitDepth      = 4;
    public static int populationSize    = 1000;
    public static int maxCrossoverDepth = 8;
    public static int programCreationMaxTries = 5;
    public static int numEvolutions     = 1800;
    public static boolean verboseOutput = true;
    public static int maxNodes          = 21;
    public static double functionProb = 0.9d;
    public static float reproductionProb = 0.1f; // float
    public static float mutationProb = 0.1f; // float
    public static float crossoverProb = 0.9f; // float
    public static float dynamizeArityProb = 0.08f; // float
    public static double newChromsPercent = 0.3d;
    public static int tournamentSelectorSize = 0;
    public static boolean noCommandGeneCloning = true;
    public static boolean strictProgramCreation = false;
    public static boolean useProgramCache = true;

    // lower/upper ranges for the Terminal
    public static double lowerRange     = -10.0d;
    public static double upperRange     = -10.0d;

    // Should the terminal be a whole numbers (integers as double) or not?
    public static boolean terminalWholeNumbers = true;

    public static String returnType = "DoubleClass"; // not used yet
    public static String presentation   = "";

    // Using ADF
    public static int adfArity = 0;
    public static String adfType = "double";
    public static boolean useADF = false;

    // list of functions (as strings)
    public static String[] functions    = {"Multiply","Divide","Add","Subtract"};
    // list of functions for ADF
    public static String[] adfFunctions    = {"Multiply3","Divide","Add3","Subtract"};

    // if the values are too small we may want to scale
    // the error
    public static double scaleError = -1.0d;

    // timing
    public static long startTime;
    public static long endTime;

    // if >= 0.0d, then stop if the fitness is below or equal
    // this value
    public static double stopCriteriaFitness = -1.0d;

    // shows the whole population (sorted by fitness)
    // in all generations. Mainly for debugging purposes.
    public static boolean showPopulation = false;

    // show similiar solutions with the same fitness
    // as the overall best program
    public static boolean showSimiliar = false;

    // 2010-02-27
    // how to sort the similiar solutions.
    // Valid options:
    //   - occurrence (descending, default)
    //   - length (asccending)
    public static String similiarSortMethod = "occurrence";

    // shows progression as generation number
    public static boolean showProgression = false;

    // show results for all generations
    public static boolean showAllGenerations = false;

    // show all the results for the fittest program
    public static boolean showResults = false;
    public static int resultPrecision = 5;

    // take a sample of the data set (if > 0.0)
    public static double samplePCT = 0.0d;

    // hits criteria: if >= 0.0d then collect and show
    // number of fitness values (errors) that is equal
    // or below this value.
    public static double hitsCriteria = -1.0d;

    // withheld a percentage for validation of the
    // of the fittest program
    public static double validationPCT = 0.0d;
    protected static Double[][] validationSet;

    // for testing some values
    public static Double[][] testData;

    // for ModuloReplaceD: replacement for 0
    public static int modReplace = 0;

    // 2010-02-27
    // make time series based on a single sequence
    public static boolean makeTimeSeries = false;
    // 2010-02-27
    // make time series based on a single sequence
    // and adding the index of the instance
    public static boolean makeTimeSeriesWithIndex = false;

    // make a sequence of (ix, number) based on a single sequence
    // public static boolean makeIndexSeq = false;

    // 2010-02-22
    // Error method.
    // Valid options:
    //    totalError (default)
    //    minError
    //    meanError
    //    medianError
    //    maxError
    //
    // Note that hitsCriteria > -1 overrides errorMethod
    //
    public static String errorMethod = "totalError";

    // 2010-02-26: If we don't want to have any Terminals
    public static boolean noTerminals = false;

    // 2010-03-01: Penalty if the number of nodes in a program
    //             is less than minimum required.
    public static int minNodes = -1;
    //  The penalty for less nodes (may be application dependent)
    public static double minNodesPenalty = 0.0d;

    // 2010-03-02: Penalty if the variables are not different
    public static boolean alldifferentVariables = false;
    public static double alldifferentVariablesPenalty = 0.0d;

    public static void readFile(String file) {

        try {

            BufferedReader inr = new BufferedReader(new FileReader(file));
            String str;
            int lineCount = 0;
            boolean gotData = false;
            ArrayList<Double[]> theData = new ArrayList<Double[]>();
            ArrayList<Double[]> theValidationSet = new ArrayList<Double[]>();
            ArrayList<Double[]> theTestData = new ArrayList<Double[]>();

            // read the lines
            while ((str = inr.readLine()) != null) {
                lineCount++;
                str = str.trim();

                // ignore empty lines or comments, i.e. lines starting with either # or %
                // ----------------------------------------------------------------------
                if (str.startsWith("#") || str.startsWith("%") || str.length() == 0) {
                    continue;
                }

                if ("data".equals(str)) {
                    gotData = true;
                    continue;
                }

                if (gotData) {
                    // Read the data rows
                    // ------------------
                    String[] dataRowStr = str.split("[\\s,]+");
                    int len = dataRowStr.length;
                    Double[] dataRow = new Double[len];
                    boolean isTestData = false;
                    for (int i = 0; i < len; i++) {

                        if ("?".equals(dataRowStr[i])) {
                            System.out.println(len);
                            isTestData = true;
                            dataRow[i] = -1.0d; // dummy value
                        } else {
                            dataRow[i] = Double.parseDouble(dataRowStr[i]);
                        }
                    }

                    // check if this row should be in the data
                    // or maybe in the validation set.
                    // A data point may not be in the both data
                    // set and validation set.
                    boolean inData = true;

                    if (isTestData) {
                        inData = false;
                        theTestData.add(dataRow);
                    }

                    // Get sample to use
                    // Keep all the rows where nextFloat is <= samplePCT
                    if (!isTestData && samplePCT > 0.0d) {
                        Random randomGenerator = new Random();
                        float rand = randomGenerator.nextFloat();
                        if (rand > samplePCT) {
                            inData = false;
                        }
                    }

                    // make validation set
                    if (!isTestData && validationPCT > 0.0d) {
                        Random randomGenerator = new Random();
                        float rand = randomGenerator.nextFloat();
                        if (rand < validationPCT) {
                            inData = false;
                            theValidationSet.add(dataRow);
                        }
                    }

                    // put in the data set
                    if (inData) {
                        theData.add(dataRow);
                    }

                } else {

                    // Check for parameters on the form
                    //    parameter: value(s)
                    // --------------------------------
                    if (str.contains(":")) {
                        String row[] = str.split(":\\s*");

                        // Now check each parameter
                        if ("return_type".equals(row[0])) {
                            returnType = row[1];

                        } else if ("presentation".equals(row[0])) {
                            presentation = row[1];

                        } else if ("num_input_variables".equals(row[0])) {
                            int numInputVariables = Integer.parseInt(row[1]);

                        } else if ("num_rows".equals(row[0])) {
                            System.out.println("num_rows is not used anymore; it is calculated by the program.");
                            // numRows = Integer.parseInt(row[1]);

                        } else if ("terminal_range".equals(row[0])) {
                            String[] ranges = row[1].split("\\s+");
                            lowerRange = Double.parseDouble(ranges[0]);
                            upperRange = Double.parseDouble(ranges[1]);

                        } else if ("terminal_wholenumbers".equals(row[0])) {
                            terminalWholeNumbers = Boolean.parseBoolean(row[1]);

                        } else if ("max_init_depth".equals(row[0])) {
                            maxInitDepth = Integer.parseInt(row[1]);

                        } else if ("min_init_depth".equals(row[0])) {
                            minInitDepth = Integer.parseInt(row[1]);

                        } else if ("program_creation_max_tries".equals(row[0])) {
                            programCreationMaxTries = Integer.parseInt(row[1]);

                        } else if ("population_size".equals(row[0])) {
                            populationSize = Integer.parseInt(row[1]);

                        } else if ("max_crossover_depth".equals(row[0])) {
                            maxCrossoverDepth = Integer.parseInt(row[1]);

                        } else if ("function_prob".equals(row[0])) {
                            functionProb = Double.parseDouble(row[1]);

                        } else if ("reproduction_prob".equals(row[0])) {
                            reproductionProb = Float.parseFloat(row[1]);

                        } else if ("mutation_prob".equals(row[0])) {
                            mutationProb = Float.parseFloat(row[1]);

                        } else if ("crossover_prob".equals(row[0])) {
                            crossoverProb = Float.parseFloat(row[1]);

                        } else if ("dynamize_arity_prob".equals(row[0])) {
                            dynamizeArityProb = Float.parseFloat(row[1]);

                        } else if ("new_chroms_percent".equals(row[0])) {
                            newChromsPercent = Double.parseDouble(row[1]);

                        } else if ("num_evolutions".equals(row[0])) {
                            numEvolutions = Integer.parseInt(row[1]);

                        } else if ("max_nodes".equals(row[0])) {
                            maxNodes = Integer.parseInt(row[1]);

                        } else if ("functions".equals(row[0])) {
                            functions = row[1].split("[\\s,]+");

                        } else if ("adf_functions".equals(row[0])) {
                            adfFunctions = row[1].split("[\\s,]+");

                        } else if ("variable_names".equals(row[0])) {
                            variableNames = row[1].split("[\\s,]+");

                        } else if ("output_variable".equals(row[0])) {
                            outputVariable = Integer.parseInt(row[1]);

                        } else if ("ignore_variables".equals(row[0])) {
                            String[] ignoreVariablesS = row[1].split("[\\s,]+");
                            ignoreVariables = new int[ignoreVariablesS.length];
                            // TODO: make it a HashMap instead
                            for (int i = 0; i < ignoreVariablesS.length; i++) {
                                ignoreVariables[i] = Integer.parseInt(ignoreVariablesS[i]);
                            }

                        } else if ("constant".equals(row[0])) {
                            Double constant = Double.parseDouble(row[1]);
                            constants.add(constant);

                        } else if ("adf_arity".equals(row[0])) {
                            adfArity = Integer.parseInt(row[1]);
                            System.out.println("ADF arity " + adfArity);
                            if (adfArity > 0) {
                                useADF = true;
                            }

                        } else if ("adf_type".equals(row[0])) {
                            adfType = row[1];

                        } else if ("tournament_selector_size".equals(row[0])) {
                            tournamentSelectorSize = Integer.parseInt(row[1]);

                        } else if ("scale_error".equals(row[0])) {
                            scaleError = Double.parseDouble(row[1]);

                        } else if ("stop_criteria_fitness".equals(row[0])) {
                            stopCriteriaFitness = Double.parseDouble(row[1]);

                        } else if ("show_population".equals(row[0])) {
                            showPopulation = Boolean.parseBoolean(row[1]);

                        } else if ("show_similiar".equals(row[0]) ||
                                "show_similar".equals(row[0])) {
                            // 2010-02-27:added alternative spelling
                            showSimiliar = Boolean.parseBoolean(row[1]);

                        } else if ("similiar_sort_method".equals(row[0]) ||
                                "similar_sort_method".equals(row[0])) {
                            // 2010-02-27
                            similiarSortMethod = row[1];

                            if (!(
                                    "length".equals(similiarSortMethod) ||
                                            "occurrence".equals(similiarSortMethod))
                                    ) {
                                System.out.println("Unknown similiar_sort_method: " + similiarSortMethod);
                                System.exit(1);
                            }


                        } else if ("show_progression".equals(row[0])) {
                            showProgression = Boolean.parseBoolean(row[1]);

                        } else if ("sample_pct".equals(row[0])) {
                            samplePCT = Float.parseFloat(row[1]);

                        } else if ("validation_pct".equals(row[0])) {
                            validationPCT = Float.parseFloat(row[1]);

                        } else if ("hits_criteria".equals(row[0])) {
                            hitsCriteria = Double.parseDouble(row[1]);
                            errorMethod = "hitsCriteria";

                        } else if ("show_all_generations".equals(row[0])) {
                            showAllGenerations = Boolean.parseBoolean(row[1]);

                        } else if ("strict_program_creation".equals(row[0])) {
                            strictProgramCreation = Boolean.parseBoolean(row[1]);

                        } else if ("no_command_gene_cloning".equals(row[0])) {
                            noCommandGeneCloning = Boolean.parseBoolean(row[1]);

                        } else if ("use_program_cache".equals(row[0])) {
                            useProgramCache = Boolean.parseBoolean(row[1]);

                        } else if ("mod_replace".equals(row[0])) {
                            // this is quite experimental
                            modReplace = Integer.parseInt(row[1]);

                        } else if ("show_results".equals(row[0])) {
                            showResults = Boolean.parseBoolean(row[1]);

                        } else if ("result_precision".equals(row[0])) {
                            resultPrecision = Integer.parseInt(row[1]);

                        } else if ("error_method".equals(row[0])) {
                            errorMethod = row[1];

                            if (!(
                                    "maxError".equals(errorMethod) ||
                                            "minError".equals(errorMethod) ||
                                            "medianError".equals(errorMethod) ||
                                            "meanError".equals(errorMethod) ||
                                            "totalError".equals(errorMethod))) {
                                System.out.println("Unknown errorMethod: " + errorMethod);
                                System.exit(1);
                            }

                        } else if ("no_terminals".equals(row[0])) {
                            // Added 2010-02-26
                            noTerminals = Boolean.parseBoolean(row[1]);

                        } else if ("make_time_series".equals(row[0])) {
                            makeTimeSeries = Boolean.parseBoolean(row[1]);

                        } else if ("make_time_series_with_index".equals(row[0])) {
                            makeTimeSeriesWithIndex = Boolean.parseBoolean(row[1]);

                        } else if ("min_nodes".equals(row[0])) {
                            // 2010-03-01: Added this and min_nodes_penalty
                            String[] opt = row[1].split("[\\s,]+");
                            minNodes = Integer.parseInt(opt[0]);

                            if (minNodes > maxNodes) {
                                System.out.println("minNodes (" + minNodes + ") >  maxNodes (" + maxNodes + ") which is weird. Cannot continue. ");
                                System.exit(1);
                            }
                            minNodesPenalty = Integer.parseInt(opt[1]);

                        } else if ("alldifferent_variables".equals(row[0])) {
                            String[] opt = row[1].split("[\\s,]+");
                            alldifferentVariables = Boolean.parseBoolean(opt[0]);
                            alldifferentVariablesPenalty = Double.parseDouble(opt[1]);
                        } else {
                            System.out.println("Unknown keyword: " + row[0] + " on line " + lineCount);
                            System.exit(1);

                        }
                    }

                } // end if(gotData)

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
