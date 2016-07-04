/**
 * Created by Christina on 04/7/2016.
 */
import java.awt.*;
import javax.swing.*;

import org.scilab.forge.jlatexmath.TeXConstants;
import org.scilab.forge.jlatexmath.TeXFormula;
import org.scilab.forge.jlatexmath.TeXIcon;

public class JLatex {

	public JLabel printEquation(String equation) {

		String latex ;
//        latex        = "\\begin{equation}\\label{xx}\n" +
//                "\\begin{split}"+"y =x^2+c/(e+sin(a))-d\\\\\n"+" \\quad +e-f\\\\\n" +
//                " =g+h\\\\\n" +
//                " =i"+"\\end{split}\n" +
//                "\\end{equation}";
//
        latex = "\\begin{align}\n" +
                "a_1& =b_1+c_1\\\\\n" +
                "a_2& =b_2+c_2-d_2+e_2\n" +
                "\\end{align}";
//		latex += "\\end{equation}";

////
		TeXFormula formula = new TeXFormula(latex);
		TeXIcon icon = formula.createTeXIcon(TeXConstants.STYLE_DISPLAY, 20);


		final JLabel label = new JLabel(icon);
//		label.setMaximumSize(new Dimension(200, 300));
//		label.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        label.setBounds (10,10, label.getWidth(), label.getHeight());

        return label;
	}
}
