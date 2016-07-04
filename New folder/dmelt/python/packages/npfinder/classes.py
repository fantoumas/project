class Point:

    """
    Point object class
    
    Attributes:
        point_number = number of given point
        x -> point x coordinate
        y -> point y coordinate
        x_err_low -> low error in x
        x_err_high -> high error in x
        y_err_low -> low error in y
        y_err_high -> high error in y
        in_peak -> True if point is in a peak; False if point is not in a peak 
        alpha1 -> angle between this point and previous neighboring point, assigned with SetAlpha1
        alpha2 -> angle between this point and next neighboring point, assigned with SetAlpha2
        
    All attributes are accessible via their respective 'Get _____' method. See below.
    
    All attributes can be set via their respective 'Set ____' method. See below.  
    """
    
    def __init__(self, point_number, x_pos, y_pos):
        """Initialization function for Point class"""
        self.point_number = point_number
        self.x = x_pos
        self.y = y_pos
    
    def GetPointNumber(self):
        point_number = self.point_number
        return point_number
    
    def GetX(self):
        x = self.x
        return x
    
    def GetY(self):
        y = self.y
        return y
    
    def GetXErrLow(self):
        x_err_low = self.x_err_low
        return x_err_low
    
    def GetXErrHigh(self):
        x_err_high = self.x_err_high
        return x_err_high
        
    def GetYErrLow(self):
        y_err_low = self.y_err_low
        return y_err_low
    
    def GetYErrHigh(self):
        y_err_high = self.y_err_high
        return y_err_high
        
    def GetAlpha1(self):
        alpha1 = self.alpha1
        return alpha1
        
    def GetAlpha2(self):
        alpha2 = self.alpha2
        return alpha2
    
    def SetX(self, new_x):
        """Set new x value for point"""
        self.x = new_x
        
    def SetY(self, new_y):
        """Set new y value for point"""
        self.y = new_y
    
    def SetXErrLow(self, new_x_err_low):
        """Set new x_err_low for point"""
        self.x_err_low = new_x_err_low
        
    def SetXErrHigh(self, new_x_err_high):
        """Set new x_err_high for point"""
        self.x_err_high = new_x_err_high
    
    def SetYErrLow(self, new_y_err_low):
        """Set new y_err_low value for point"""
        self.y_err_low = new_y_err_low
    
    def SetYErrHigh(self, new_y_err_high):
        """Set new y_err_high for point"""
        self.y_err_high = new_y_err_high
        
    def SetAlpha1(self, alpha1):
        self.alpha1 = alpha1
    
    def SetAlpha2(self, alpha2):
        self.alpha2 = alpha2
        
class Peak:
    """
    Peak object class
    
    Peak attributes:
        -> peak_number - number of the peak
        -> points - list of points in the peak
        -> linreg_points - list of linearly regressed background points for the peal
        -> residuals - list of residuals for each point in the peak compared to respective background point
        -> stat_sig - statistical significance of the peak
    
    All attributes (and a few more properties of the peak) can be accessed by their respective 'Get ____' method. See below.
   
    Some attributes may be set using their 'Add ___' or 'Set ____' methods. See below.
    
    
    """
    
    def __init__(self, peak_number):
        self.peak_number = peak_number
        self.points = []
        self.linreg_points = []
        self.residuals = []
        self.stat_sig = 0
    
    def AddLinRegPoint(self, point):
        self.linreg_points.append(point)
    
    def AddPoint(self, point):
        self.points.append(point)
        
    def AddResidual(self, value):
        self.residuals.append(value)
    
    def GetLinRegPoints(self):
        linreg_points = self.linreg_points
        return linreg_points
        
    def GetNumberOfPoints(self):
        num_points = len(self.points)
        return num_points
    
    def GetPeakEnd(self):
        peak_end = self.points[len(self.points) - 1]
        return peak_end
        
    def GetPeakNumber(self):
        peak_number = self.peak_number
        return peak_number
            
    def GetPeakStart(self):
        peak_start = self.points[0]
        return peak_start
        
    def GetPoints(self):
        points = self.points
        return points
        
    def GetResiduals(self):
        residuals = self.residuals
        return residuals
        
    def GetStatSig(self):
        stat_sig = self.stat_sig
        return stat_sig
        
    def SetStatSig(self, stat_sig):
        self.stat_sig = stat_sig
    
    def toString(self):
        return 'Peak:'+str(self.peak_number)+' Start:'+str(self.points[0].x)+' End:'+str(self.points[len(self.points) - 1].x)+' Sign:'+str(self.stat_sig) 
    
    
    
    
    
