package jhplot.math.pca.tests;

import jhplot.math.pca.*;
import jhplot.math.pca.covmatrixevd.*;
import jhplot.math.pca.*;
import java.io.IOException;
import java.io.InputStream;

import Jama.Matrix;
import junit.framework.TestCase;


public abstract class TemplatePCATest extends TestCase {
	private final double precision;
	private final CovarianceMatrixEVDCalculator evdCalc;
	
	public TemplatePCATest(double precision, 
			CovarianceMatrixEVDCalculator evdCalc){
		this.precision = precision;
		this.evdCalc = evdCalc;
	}
	
	protected void checkPCATransformation(String trainingDataPath,
			String testingDataPath, 
			String expectedRotatedDataPath, String expectedWhitenedDataPath) 
	throws IOException{
		checkPCATransformation(trainingDataPath, testingDataPath,
			expectedRotatedDataPath, expectedWhitenedDataPath, true);
	}
	
	protected void checkPCATransformation(String trainingDataPath,
			String testingDataPath, 
			String expectedRotatedDataPath, String expectedWhitenedDataPath,
			boolean center) 
	throws IOException{
		Matrix training = DataReader.read(getFile(trainingDataPath), false);
		Matrix testing = DataReader.read(getFile(testingDataPath), false);
		Matrix expectedRotated = DataReader.read(
				getFile(expectedRotatedDataPath), false);
		PCA pca = createPCA(training, center);
		Matrix actualRotated = 
				pca.transform(testing, PCA.TransformationType.ROTATION);
		assertTrue(equalColumnsWithSignAccuracy(
				expectedRotated, actualRotated, precision));
		Matrix expectedWhitened = DataReader.read(
				getFile(expectedWhitenedDataPath), false);
		Matrix actualWhitened = 
			pca.transform(testing, PCA.TransformationType.WHITENING);
		assertTrue(equalColumnsWithSignAccuracy(
				expectedWhitened, actualWhitened, precision));	
	}
	
	protected void checkOutliers(String allDataFile, 
			String outliersDataFile, String nonOutliersDataFile) throws IOException{
		Matrix pts = DataReader.read(getFile(allDataFile), false);
		PCA pca = createPCA(pts, true);
		Matrix outliers = DataReader.read(getFile(outliersDataFile), false);
		for(int r = 0; r < outliers.getRowDimension(); r++){
			Matrix vector = outliers.getMatrix(
					r, r, 0, outliers.getColumnDimension()-1);
			assertFalse(pca.belongsToGeneratedSubspace(vector));
		}
		Matrix nonOutliers = DataReader.read(
				getFile(nonOutliersDataFile), false);
		for(int r = 0; r < nonOutliers.getRowDimension(); r++){
			Matrix vector = nonOutliers.getMatrix(
					r, r, 0, nonOutliers.getColumnDimension()-1);
			assertTrue(pca.belongsToGeneratedSubspace(vector));
		}	
	}
	
	protected void checkDimsReduction(String filePath, int inputDimsNo,
			int outputDimsNo) throws IOException{
		Matrix pts = DataReader.read(getFile(filePath), false);
		PCA pca = createPCA(pts, true);
		assertEquals(inputDimsNo, pca.getInputDimsNo());		
		assertEquals(outputDimsNo, pca.getOutputDimsNo());
	}
	
	protected InputStream getFile(String filePath){
		return getClass().getResourceAsStream(filePath);
	}
	
	private static boolean equalColumnsWithSignAccuracy(
			Matrix expected, Matrix actual, double precision){
		if(expected.getColumnDimension() != actual.getColumnDimension() ||
				expected.getRowDimension() != actual.getRowDimension())
			return false;
		for(int c = 0; c < expected.getColumnDimension(); c++){
			Matrix expectedColumn = expected.getMatrix(
					0, expected.getRowDimension()-1, c, c);
			Matrix actualColumn = actual.getMatrix(
					0, expected.getRowDimension()-1, c, c);
			Matrix negatedActualColumn = actualColumn.times(-1);
			if(!(areEqual(expectedColumn, actualColumn, precision) || 
					areEqual(expectedColumn, negatedActualColumn, precision)))
				return false;
		}
		return true;
	}
	
	private static boolean areEqual(Matrix m0, Matrix m1, 
			double precision){
		if(m0.getColumnDimension() != m1.getColumnDimension() ||
				m0.getRowDimension() != m1.getRowDimension())
			return false;
		for(int c = 0; c < m0.getColumnDimension(); c++){
			for(int r = 0; r < m0.getRowDimension(); r++){
				if(Math.abs(m0.get(r, c) - m1.get(r, c)) > precision)
					return false;
			}
		}
		return true;
	}
	
	private PCA createPCA(Matrix pts, boolean center){
		return new PCA(pts, evdCalc, center);
	}
}
