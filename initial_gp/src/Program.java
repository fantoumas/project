import org.jgap.InvalidConfigurationException;
import org.jgap.gp.CommandGene;
import org.jgap.gp.GPProblem;
import org.jgap.gp.function.*;
import org.jgap.gp.impl.DeltaGPFitnessEvaluator;
import org.jgap.gp.impl.GPConfiguration;
import org.jgap.gp.impl.GPGenotype;
import org.jgap.gp.terminal.Terminal;
import org.jgap.gp.terminal.Variable;

import java.util.Scanner;

/**
 * Created by Christina on 16/6/2016.
 */
public class Program extends GPProblem {

    public static Variable vx;

    public static void main(String[] args) throws Exception {

//        nameOfFile = scanString("Pass the data file");
//            type = scanString("What is the type of the file? Type txt or csv.");
//        ReadFile readData = new ReadFile();
//        readData.readFile(nameOfFile);
        Menu menu = new Menu();
        menu.createMenuAndPrint();

        GPConfiguration config = new GPConfiguration();
        // We use a delta fitness evaluator because we compute a defect rate, not
        // a point score!
        // ----------------------------------------------------------------------
        config.setGPFitnessEvaluator(new DeltaGPFitnessEvaluator());
        config.setMaxInitDepth(6);
        config.setPopulationSize(100);
        config.setMaxCrossoverDepth(8);
        config.setFitnessFunction(new MathProblem.FormulaFitnessFunction());
        config.setStrictProgramCreation(true);
        GPProblem problem = new MathProblem(config);
        GPGenotype gp = problem.create();
        gp.setVerboseOutput(true);
        System.out.println("so far so good");

    }

    public static String scanString(String msg) {
        System.out.println(msg);
        Scanner scan = new Scanner(System.in);
        return scan.nextLine();
    }

    public GPGenotype create()
            throws InvalidConfigurationException {
        GPConfiguration conf = getGPConfiguration();
        Class[] types = {
                // Return type of result-producing chromosome
                CommandGene.FloatClass,
                // ADF-relevant:
                // Return type of ADF 1
                CommandGene.FloatClass};
        // Then, we define the arguments of the GP parts. Normally, only for ADF's
        // there is a specification here, otherwise it is empty as in first case.
        // -----------------------------------------------------------------------
        Class[][] argTypes = {
                // Arguments of result-producing chromosome: none
                {},
                // ADF-relevant:
                // Arguments of ADF1: all 3 are float
                {CommandGene.FloatClass, CommandGene.FloatClass, CommandGene.FloatClass}
        };
        CommandGene[][] nodeSets = { {
                // We use a variable that can be set in the fitness function.
                // ----------------------------------------------------------
                vx = Variable.create(conf, "X", CommandGene.FloatClass),
                new Multiply(conf, CommandGene.FloatClass),
                new Multiply3(conf, CommandGene.FloatClass),
                new Divide(conf, CommandGene.FloatClass),
                new Sine(conf, CommandGene.FloatClass),
                new Exp(conf, CommandGene.FloatClass),
                new Subtract(conf, CommandGene.FloatClass),
                new Pow(conf, CommandGene.FloatClass),
                new Terminal(conf, CommandGene.FloatClass, 2.0d, 10.0d, true),
                // ADF-relevant:
                // Construct a reference to the ADF defined in the second nodeset
                // which has index 1 (second parameter of ADF-constructor).
                // Furthermore, the ADF expects three input parameters (see argTypes[1])
                new ADF(conf, 1 , 3),
        },
                // ADF-relevant:
                // and now the definition of ADF(1)
                {
                        new Add3(conf, CommandGene.FloatClass),
                }
        };
        return GPGenotype.randomInitialGenotype(conf, types, argTypes, nodeSets,
                20, true);    }
}
