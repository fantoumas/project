from java.awt import Font,Color
from jhplot  import HPlot,H1D,P1D,HFit

# make main canvas
c1 = HPlot("Canvas",600,400)
c1.visible(1)
c1.setAutoRange()


c1.viewHisto(0);  # make sure starts from 0
c1.setGTitle("Make a fit using the FIT PANEL", Color.blue) #put title
c1.setGrid(0,0)
c1.setGrid(1,0)


# make data set
p1 = P1D("My Test 1")
p1.add(1.0,3, 1.0)
p1.add(2.0,2, 1.0)
p1.add(3.0,5, 1.0)
p1.add(4.0,5, 1.0)
p1.add(5.0,7, 2.0)
p1.setErr(1)
# set color blue and transparency level 50%
p1.setErrFillColor(Color.yellow,0.3)
c1.draw(p1)

# fit interactively this histogram
# pass objects and names (for code generation)
a=HFit(c1,p1)

# add a user function if you want to
a.addFunc("User1", "Tooltip", "a*x[0]+b","a,b")
