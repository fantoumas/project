
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>DMelt example jaida_Chi2Fit.java </title>
<script type="text/javascript" src="syntax/scripts/shCore.js"></script>
<script type="text/javascript" src="syntax/scripts/shBrushRuby.js"></script>
<link type="text/css" rel="stylesheet" href="syntax/styles/shCoreDefault.css"/>
<script type="text/javascript">SyntaxHighlighter.all();</script>
</head>
<body style="background: white; font-family: Helvetica">
<center>
<b><font color="green">Fitting a histogram with the Chi2 method</font></b><br>
Code: jaida_Chi2Fit.java, Type: ruby,  Version 1. Last modified: 12/07/2015. License: <font color="red">Pro</font> <br>
<a href="http://jwork.org/dmelt/code/cache/jaida_Chi2Fit_6399.java">http://jwork.org/dmelt/code/cache/jaida_Chi2Fit_6399.java</a>
<br>
<small><i>To run this script using the DMelt IDE,
copy the above URL link to the menu [File]&#8594;[Read script from URL] of the DMelt IDE.
</small><i>
<br>
</center>

<hr>
<pre class='brush: ruby'>

import hep.aida.*;
import java.util.Random;

public class jaida_Chi2Fit
{
   public static void main(String[] args)
   {
      // Create factories
      IAnalysisFactory analysisFactory = IAnalysisFactory.create();
      IHistogramFactory histogramFactory = analysisFactory.createHistogramFactory(analysisFactory.createTreeFactory().create());
      IPlotter plotter = analysisFactory.createPlotterFactory().create("Plot");
      IFitFactory fitFactory = analysisFactory.createFitFactory();
      
      // Create 1D histogram
      IHistogram1D h1d = histogramFactory.createHistogram1D("Gaussian Distribution",100,-5,5);
      
      // Fill 1D histogram with Gaussian
      Random r = new Random();
      for (int i=0; i<5000; i++)
         h1d.fill(r.nextGaussian());
      
      // Do Fit
      IFitter fitter = fitFactory.createFitter("chi2");
      IFitResult result = fitter.fit(h1d,"g");
      
      // Show results
      plotter.createRegions(1,1,0);
      plotter.destroyRegions();
      plotter.region(0).plot(h1d);
      plotter.region(0).plot(result.fittedFunction());
      plotter.show();
   }
}
</pre>
<hr>
</html>
