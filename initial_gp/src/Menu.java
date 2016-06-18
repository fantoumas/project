/**
 * Created by Christina on 16/6/2016.
 */
public class Menu {

    public void createMenuAndPrint()
    {
        String[] menu = new String[12];
        menu[0] = "variables names";
        menu[1] = "output varibles";
        menu[2] = "input varibles";
        menu[3] = "num of rows";
        menu[4] = "functions included";
        menu[5] = "terminal range as to avoid errors";
        menu[6] = "max initial depth";
        menu[7] = "population size";
        menu[8] = "number of evolutions";
        menu[9] = "max nodes";
        menu[10] = "mutation";
        menu[11] = "crossover";
        for( int i = 0; i<menu.length; i++) {
            System.out.print(i+"." +menu[i]+ "  ");
        }
        System.out.println();
    }
}
