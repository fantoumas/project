# Physics/HEP | C | 1.7 | S.Chekanov | A typical world's summary plot

from jhplot import HPlot,HLabel,P1D
from java.awt import Color, Font

c1=HPlot("summary plot",550,650)
c1.setGTitle("B_{2} summary")
f=Font("Lucida Sans", Font.BOLD, 20)
c1.setNameX("Centre-of-mass energy (GeV)", f, Color.black)
c1.setNameY("B_{2} GeV^{-2}",f, Color.black)

c1.setRange(0.1,1000,0.0001,0.2)
c1.setLogScale(0,1)
c1.setLogScale(1,1)
c1.setGrid(0,0)
c1.setGrid(1,0)
c1.visible()

c=Color(100,10,200)
p1=P1D("&gamma; p #bar{d} (ep, H1)")
p1.setSymbolSize(8)
p1.setSymbol(7)
p1.setPenWidthErr(2)
p1.setErrColor(c)
p1.setColor(c)
p1.add(210, 0.01, 0.0, 0.0, 0.001,0.001, 0.0, 0.0, 0.002,0.002)

c=Color.black
p2=P1D("DIS #bar{d}(ep, ZEUS)")
p2.setErrColor(c)
p2.setSymbolSize(8)
p2.setPenWidthErr(2)
p2.setColor(c)
p2.setErr(1)
p2.setErrSys(1)
p2.setPenWidthErr(3)
p2.setPenWidthErrSys(1)
p2.add(175, 0.0088, 0.0, 0.0, 0.0014,0.0014, 0.0, 0.0, 0.0015,0.0015)

p3=P1D("DIS d  (ep, ZEUS)")
p3.setErrColor(c)
p3.setErr(1)
p3.setErrSys(1)
p3.setSymbol(5)
p3.setColor(c)
p3.setSymbolSize(8)
p3.setPenWidthErr(3)
p3.setPenWidthErrSys(1)
# p3.add(175, 0.0328, 0.0, 0.0, 0.0034,0.0034, 0.0, 0.0, 0.0098,0.0098)
p3.add(175, 0.0328, 0.0, 0.0, 0.0034,0.0034, 0.0, 0.0, 0.0098,0.0098)

lab5=HLabel("HERA",0.75,0.84, "NDC")
lab5.setColor(c)
c1.add(lab5)


p4=P1D("e^{+}e^{-} #bar{d} (ALEPH)")
p4.setLegend(0)
c=Color.blue
lab1=HLabel(" #bar{d}(e^{+}e^{-} Z decay)",3.37,0.0035)
lab1.setColor(c)
c1.add(lab1)
p4.setErrColor(c)
p4.setSymbolSize(7)
p4.setPenWidthErr(2)
p4.setColor(c)
p4.add(91, 0.0033, 0.0013,0.0013)


p5=P1D("Heavy-ion experiments d,#bar{d}")
c=Color(210,100,20)
lab=HLabel("d,#bar{d} (Heavy-ion experiments)",0.3,0.15, "NDC")
lab3=HLabel("RHIC",0.76,0.37, "NDC")
lab.setColor(c)
lab3.setColor(c)
c1.add(lab)
c1.add(lab3)
p5.setLegend(0)
p5.setErrColor(c)
p5.setSymbolSize(7)
p5.setPenWidthErr(2)
p5.setColor(c)
p5.add(4.7, 0.0013, 0.0008,0.0005)
p5.add(8.8, 0.001,  0.0004,0.0004)
p5.add(12, 0.0007,  0.00012,0.0001)
p5.add(16, 0.00046,  0.00008,0.00008)
p5.add(18, 0.000447,  0.00012,0.00012)
p5.add(130, 0.000447,  0.0001,0.0001)
p5.add(203, 0.000567,  0.00007,0.00006)

p6=P1D("pp,pA d, #bar{d}")
c=Color(80,200,70)
p6.setLegend(0)
lab2=HLabel("d,#bar{d} (pp,pA)",2.07,0.026)
lab2.setColor(c)
c1.add(lab2)
p6.setErrColor(c)
p6.setSymbolSize(7);
p6.setPenWidthErr(2);
p6.setColor(c)
p6.add(2.04, 0.02, 0.002,0.002)
p6.add(5.01, 0.019,  0.002,0.002)
p6.add(16, 0.020,  0.002,0.002)
p6.add(53, 0.017,  0.002,0.003)
p6.add(61.6, 0.013,  0.002,0.003)


p7=P1D("pp,pA d, #bar{d}")
c=Color.blue
p7.setLegend(0)
lab2=HLabel(" #bar{d}(&Upsilon;(1,2S))",0.6,0.007)
lab2.setColor(c)
c1.add(lab2)
p7.setErrColor(c)
p7.setSymbolSize(7);
p7.setPenWidthErr(2);
p7.setColor(c)
p7.add(10., 0.0063, 0.002,0.002)






c1.draw(p2)
c1.draw(p3)
c1.draw(p1)
c1.draw(p4)
c1.draw(p5)
c1.draw(p6)
c1.draw(p7)
