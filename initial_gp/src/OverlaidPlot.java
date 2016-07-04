/**
 * Created by Christina on 03/7/2016.
 */
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.axis.NumberTickUnit;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.plot.DatasetRenderingOrder;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYBubbleRenderer;
import org.jfree.chart.renderer.xy.XYItemRenderer;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.xy.IntervalXYDataset;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import javax.swing.*;


public class OverlaidPlot
{
    final XYSeries series1 = new XYSeries("Graph1");
    final XYSeries series2 = new XYSeries("Graph2");
    final ChartPanel panel;

    public OverlaidPlot(final String title) {
        final JFreeChart chart = createOverlaidChart(title);
        panel = new ChartPanel(chart, true, true, true, true, true);
        panel.setPreferredSize(new java.awt.Dimension(400, 200));
    }

    public void addElem1(double x, double y) {
        this.series1.add(x, y);
    }

    public void addElem2(double x, double y) {
        this.series2.add(x, y);
    }


    private JFreeChart createOverlaidChart(String title)
    {
        final NumberAxis domainAxis = new NumberAxis("Speed (m/s)");
        final ValueAxis rangeAxis = new NumberAxis("Power (kw)");

        // create plot ...
        // change "new XYBarRenderer(0.20)" to "StandardXYItemRenderer()" if you want to change  type of graph

        // add a second dataset and renderer...
        final IntervalXYDataset data1 = createDataset1();
        final XYLineAndShapeRenderer renderer1 = new XYLineAndShapeRenderer(false, true);
        final XYPlot plot = new XYPlot(data1, domainAxis, rangeAxis, renderer1);
        // arguments of new XYLineAndShapeRenderer are to activate or deactivate the display of points or line. Set first argument to true if you want to draw lines between the points for e.g.
        plot.setDataset(1, data1);
        plot.setRenderer(1, renderer1);

        // add a third dataset and renderer...
        final IntervalXYDataset data2 = createDataset2();
        final XYLineAndShapeRenderer renderer2 = new XYLineAndShapeRenderer(true, true);
        // arguments of new XYLineAndShapeRenderer are to activate or deactivate the display of points or line. Set first argument to true if you want to draw lines between the points for e.g.
        plot.setDataset(1, data2);
        plot.setRenderer(1, renderer2);

        plot.setDatasetRenderingOrder(DatasetRenderingOrder.FORWARD);
        NumberAxis domain = (NumberAxis) plot.getDomainAxis();
        domain.setRange(0.00, 30);

//        domain.setTickUnit(new NumberTickUnit(0.5));
        // return a new chart containing the overlaid plot...
        return new JFreeChart(title, JFreeChart.DEFAULT_TITLE_FONT, plot, true);
    }

    private IntervalXYDataset createDataset1() {
        // create dataset 1...
        final XYSeriesCollection coll1 = new XYSeriesCollection(series1);
        return coll1;
    }

    private IntervalXYDataset createDataset2() {
        // create dataset 2...
        final XYSeriesCollection coll2 = new XYSeriesCollection(series2);

        return coll2;
    }

    public ChartPanel start(OverlaidPlot demo) {
        demo.addElem2(4,5);
        demo.addElem2(4.5464,5.65798);
        demo.addElem2(1.84984,3.98798);
        demo.addElem2(-2,2.64654);
        demo.addElem2(0.56454,1.5494);
        demo.addElem1(4.2,4.9);
        demo.addElem1(4.3,5.65798);
        demo.addElem1(2,3);
        demo.addElem1(-2.2,2.24654);
        demo.addElem1(0.76454,1.0494);
        return panel;
    }

    public void plot(JPanel panel) {
        final XYPlot plot = new XYPlot();
        JFreeChart xylineChart = ChartFactory.createXYLineChart(
                "represantion of solution" ,
                "Category" ,
                "Score" ,
                createDataset00() ,
                PlotOrientation.VERTICAL ,
                true , true , false);
        JFreeChart lineChart = ChartFactory.createLineChart(
                "somehitng",
                "Years","Number of Schools",
                createDataset22(),
                PlotOrientation.VERTICAL,
                true,true,false);

        ChartPanel[] chartPanels = new ChartPanel[2];
        ChartPanel chartPanel = new ChartPanel( xylineChart );
        ChartPanel chartPanel2 = new ChartPanel( lineChart );
        chartPanels[0] = chartPanel;
        chartPanels[1] = chartPanel2;
        chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
    }

    public void tryAgain(JPanel panel) {
// Create a single plot containing both the scatter and line
        XYPlot plot = new XYPlot();


// Create the scatter data, renderer, and axis
        XYDataset collection1 = createDataset1();
        XYItemRenderer renderer1 = new XYBubbleRenderer();   // Shapes only
        ValueAxis domain1 = new NumberAxis("Domain1");
        ValueAxis range1 = new NumberAxis("Range1");

// Set the scatter data, renderer, and axis into plot
        plot.setDataset(0, collection1);
        plot.setRenderer(0, renderer1);
        plot.setDomainAxis(0, domain1);
        plot.setRangeAxis(0, range1);

// Map the scatter to the first Domain and first Range
        plot.mapDatasetToDomainAxis(0, 0);
        plot.mapDatasetToRangeAxis(0, 0);

/* SETUP LINE */

// Create the line data, renderer, and axis
        XYDataset collection2 = createDataset00();
        XYItemRenderer renderer2 = new XYLineAndShapeRenderer(true, false);   // Lines only
        ValueAxis domain2 = new NumberAxis("Domain2");
        ValueAxis range2 = new NumberAxis("Range2");

// Set the line data, renderer, and axis into plot
        plot.setDataset(1, collection2);
        plot.setRenderer(1, renderer2);
        plot.setDomainAxis(1, domain2);
        plot.setRangeAxis(1, range2);

// Map the line to the second Domain and second Range
        // Map the line to the FIRST Domain and second Range
        plot.mapDatasetToDomainAxis(1, 0);
        plot.mapDatasetToRangeAxis(1, 1);

// Create the chart with the plot and a legend
        JFreeChart chart = new JFreeChart("Multi Dataset Chart", JFreeChart.DEFAULT_TITLE_FONT, plot, true);
        java.awt.image.BufferedImage image = chart.createBufferedImage(600,400);
        JLabel label = new JLabel(new ImageIcon(image));

        panel.add(label);    }


    private DefaultCategoryDataset createDataset22( )
    {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset( );
        dataset.addValue( 15 , "schools" , "1970" );
        dataset.addValue( 30 , "schools" , "1980" );
        dataset.addValue( 60 , "schools" ,  "1990" );
        dataset.addValue( 120 , "schools" , "2000" );
        dataset.addValue( 240 , "schools" , "2010" );
        dataset.addValue( 300 , "schools" , "2014" );
        return dataset;
    }

    private XYDataset createDataset00( )
    {
        final XYSeries firefox = new XYSeries( "Firefox" );
        firefox.add( 1.0 , 1.0 );
        firefox.add( 2.0 , 4.0 );
        firefox.add( 3.0 , 3.0 );
        final XYSeries chrome = new XYSeries( "Chrome" );
        chrome.add( 1.0 , 4.0 );
        chrome.add( 2.0 , 5.0 );
        chrome.add( -3.0 , 6.0 );
        final XYSeries iexplorer = new XYSeries( "InternetExplorer" );
        iexplorer.add( 3.0 , 4.0 );
        iexplorer.add( 4.0 , 5.0 );
        iexplorer.add( 5.0 , -4.0 );
        final XYSeriesCollection dataset = new XYSeriesCollection( );
        dataset.addSeries( firefox );
        dataset.addSeries( chrome );
        dataset.addSeries( iexplorer );
        return dataset;
    }

    private XYDataset createDataset11( )
    {
        final XYSeries firefox = new XYSeries( "Firefox" );
        firefox.add( 1.0 , 1.0 );
        firefox.add( 2.0 , 4.6 );
        firefox.add( 3.3 , 3.0 );
        final XYSeries chrome = new XYSeries( "Chrome" );
        chrome.add( 1.0 , 4.0 );
        chrome.add( 2.2 , 5.0 );
        chrome.add( -2.0 , 6.0 );
        final XYSeries iexplorer = new XYSeries( "InternetExplorer" );
        iexplorer.add( 3.0 , 4.0 );
        iexplorer.add( 4.0 , 5.0 );
        iexplorer.add( 5.0 , -3.0 );
        final XYSeriesCollection dataset = new XYSeriesCollection( );
        dataset.addSeries( firefox );
        dataset.addSeries( chrome );
        dataset.addSeries( iexplorer );
        return dataset;
    }
}