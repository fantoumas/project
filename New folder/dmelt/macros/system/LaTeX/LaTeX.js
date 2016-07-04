// This is a part of the BeanShell macro script LaTeX.bsh (the extension .bsh
// has been replaced by .js in order to avoid this file to be an entry of the
// macro menu and in order to preserve colored syntax).

////////////////////////////////////////////////////////////////////////////////
// Miscellaneous definitions
////////////////////////////////////////////////////////////////////////////////

// Dialog window name can be replaced
   JDialog frame = new JDialog();

// Size of the dialog window
   int d_width = 150;
   int d_height = 450;

// Position "left", "right" or "bottom"
   String d_position = "right";

// Maximum number of button per panel and of panels
// 6 for less than 6 panels in the jFrame
// 70 for less than 70 buttons in each JTabbedPane
   JComponent[][] f = new JComponent[6][70];

// Number of rows of buttons per pannel
   int nbrow = 16;

// Relative path to icons from directory containing this macro
   String path2icons = "imagescol";

// Definition of the strings appearing on the tabs
   String[] tabn = {"Gene1","Gene2","Math1","Math2","Greek","Cmds","Tab7","Tab8"};

////////////////////////////////////////////////////////////////////////////////
// Customization of paths to standard LaTeX commands.
// * WINDOWS: change "isMiktex = true" to "isMiktex = false" if you don't use
// MiKTeX. Mind your AcroRd32 version.
// * MAC: change "isFink" to "true" if you installed LaTeX via Fink.
// Unfortunately I cannot check the validity of the paths in this section.
// * UNIX-LINUX: tune the command names (e.g. kdvi instead of xdvi, gpdf instead
// of xpdf...). In some cases, write the full path to latex, pdflatex, bibtex,
// dvips and xdvi (e.g. FreeBSD/TeXLive) even if these commands are in the path.
////////////////////////////////////////////////////////////////////////////////

   String osname = System.getProperty( "os.name" );
   if (osname.substring(0,3).equals("Win")) {
   /////////////////////////////////////////////////////////////////////////////
   // WINDOWS
   /////////////////////////////////////////////////////////////////////////////
     boolean isMiktex = true;
     if (isMiktex) {
     // Windows MiKTeX
        latexString = "\"C:\\texmf\\miktex\\bin\\latex\" -interaction nonstopmode -c-style-errors |";
        pdflatexString = "\"C:\\texmf\\miktex\\bin\\pdflatex\" -interaction nonstopmode -c-style-errors |";
        bibtexString = "\"C:\\texmf\\miktex\\bin\\bibtex\" |";
        dvipsString = "\"C:\\texmf\\miktex\\bin\\dvips\" -o |.ps |";
        xdviString = "\"C:\\texmf\\miktex\\bin\\yap\" | &";
        ps2pdfString = "\"C:\\texmf\\miktex\\bin\\ps2pdf\" |.ps &";
        ghostviewString = "\"C:\\Program Files\\Ghostgum\\gsview\\gsview32\" |.ps &";
        //acroreadString = "\"C:\\Program Files\\Adobe\\Acrobat 5.0\\Reader\\AcroRd32\" |.pdf &";
        //acroreadString = "\"C:\\Program Files\\Adobe\\Acrobat 6.0\\Reader\\AcroRd32\" |.pdf &";
        acroreadString = "\"C:\\Program Files\\Adobe\\Acrobat 7.0\\Reader\\AcroRd32\" |.pdf &";
        pdfString = "\"C:\\Program Files\\Ghostgum\\gsview\\gsview32\" |.pdf &";
     } else {
     // Windows TeXLive
        latexString = "latex -interaction nonstopmode -file-line-error-style |";
        pdflatexString = "pdflatex -interaction nonstopmode -file-line-error-style |";
        bibtexString = "bibtex |";
        dvipsString = "dvips -o |.ps |";
        xdviString = "windvi | &";
        ps2pdfString = "";
        ghostviewString = "\"C:\\Program Files\\Ghostgum\\gsview\\gsview32\" |.ps &";
        //acroreadString = "\"C:\\Program Files\\Adobe\\Acrobat 5.0\\Reader\\AcroRd32\" |.pdf &";
        //acroreadString = "\"C:\\Program Files\\Adobe\\Acrobat 6.0\\Reader\\AcroRd32\" |.pdf &";
        acroreadString = "\"C:\\Program Files\\Adobe\\Acrobat 7.0\\Reader\\AcroRd32\" |.pdf &";
        pdfString = "\"C:\\Program Files\\Ghostgum\\gsview\\gsview32\" |.pdf &";
     }

   } else if (osname.substring(0,3).equals("Mac")) {
   /////////////////////////////////////////////////////////////////////////////
   // MAC
   /////////////////////////////////////////////////////////////////////////////
      boolean isFink = false;
      if (isFink) {
         latexString = "/sw/bin/latex -interaction nonstopmode -file-line-error-style |";
         pdflatexString = "/sw/bin/pdflatex -interaction nonstopmode -file-line-error-style |";
         bibtexString = "/sw/bin/bibtex -interaction nonstopmode -file-line-error-style |";
         dvipsString = "/sw/bin/dvips -interaction nonstopmode -file-line-error-style |";
         xdviString = "open |.dvi &";
         ps2pdfString = "";
         ghostviewString = "open -a Preview.app |.ps &";
         acroreadString = "acroread |.pdf &";
         //acroreadString = "open |.pdf &";
         pdfString = "open -a Preview.app |.pdf &";
      } else {
         latexString = "/usr/local/teTeX/bin/powerpc-apple-darwin6.6/latex -interaction nonstopmode -file-line-error-style |";
         pdflatexString = "/usr/local/teTeX/bin/powerpc-apple-darwin6.6/pdflatex -interaction nonstopmode -file-line-error-style |";
         bibtexString = "/usr/local/teTeX/bin/powerpc-apple-darwin6.6/bibtex |";
         dvipsString = "/usr/local/teTeX/bin/powerpc-apple-darwin6.6/dvips -o |.ps |";
         xdviString = "open |.dvi &";
         ps2pdfString = "";
         ghostviewString = "open -a Preview.app |.ps &";
         acroreadString = "acroread |.pdf &";
         //acroreadString = "open |.pdf &";
         pdfString = "open -a Preview.app |.pdf &";
      }

   } else {
   /////////////////////////////////////////////////////////////////////////////
   // UNIX - LINUX
   /////////////////////////////////////////////////////////////////////////////
  //    latexString = "latex -interaction nonstopmode -file-line-error-style |";
      latexString = "latex   |";
      pdflatexString = "pdflatex -interaction nonstopmode -file-line-error-style |";
      bibtexString = "bibtex |";
      dvipsString = "dvips -o |.ps |";
      xdviString = "xdvi | &";
      ps2pdfString = "ps2pdfwr |.ps &";
      //xdviString = "kdvi | &";
      //ghostviewString = "ghostview |.ps &";
      //ghostviewString = "kghostview |.ps &";
      ghostviewString = "gv |.ps &";
      //ghostviewString = "gg |.ps &";
      acroreadString = "acroread |.pdf &";
      pdfString = "xpdf |.pdf &";
      //pdfString = "gpdf |.pdf &";
   }

////////////////////////////////////////////////////////////////////////////////
// Customization of paths to other commands
////////////////////////////////////////////////////////////////////////////////

   // You can customize the file latexIndex.ist (same directory as LaTeX.js) or replace
   // this file by yours located elsewhere ->
   // indexString = "makeindex -s <ABSOLUTE_PATH>/<YOUR_IST_FILE.ist> |";
   indexString = "makeindex -s " + scriptDir + "latexIndex.ist |";

   // Jabref : java GUI for LaTeX bobliography, see http://jabref.sourceforge.net/
   jabrefString = "Macros.message(view,\"<html>Downnload and install Jabref.<br>Click the <b>Edit macro</b> button which will open LaTeX.js<br>Define <b>jabrefString</b> as suggested in LaTeX.js</html>\")";
   // Replace above string by:
   // jabrefString = "java -jar <PATH_TO_JAR_FILE>/JabRef-2.1b.jar &"; // All platforms
   // jabrefString = "\"C:\\Program Files\\JabRef 2.0.1\\JabRef.exe\" &"; // Windows, adapt directory name

   // jPicEdt : java GUI for LaTeX pictures, see http://jpicedt.sourceforge.net/
   jpicedtString = "Macros.message(view,\"<html>Downnload and install jPicEdt.<br>Click the <b>Edit macro</b> button which will open LaTeX.js<br>Define <b>jpicedtString</b> as suggested in LaTeX.js</html>\")";
   // Replace above string by:
   // jpicedtString = "jpicedt &"; // Assuming that you installed the launcher script in your path
   // jpicedtString = "\"C:\\jPicEdt\\jpicedt\" &";  // Windows: where you installed the shortcut jpicedt.bat

   // Printer
   printString = "Macros.message(view,\"<html>Click the <b>Edit macro</b> button which will open LaTeX.js<br>Define <b>printString</b> as suggested in LaTeX.js</html>\")";
   // Replace above string by:
   // printString = "lp -dlg |.ps"; // Unix/Linux, replace "lg" by printer name
   // printString = don't know !; // Windows

   // Aspell
   aspellEnString = "Macros.message(view,\"<html>Click the <b>Edit macro</b> button which will open LaTeX.js<br>Define <b>aspellEnString</b> as suggested in LaTeX.js</html>\")";
   // Replace above string by:
   // aspellEnString = "xterm -sb -bg black -fg white -e aspell -d english -t -c $f"; // Unix ($f is the active buffer file)
   // aspellEnString = "konsole --noclose -e aspell -d francais -t -c $f"; // Linux KDE
   // aspellEnString = "start /D \"C:\\Program files\\Aspell\\bin\" aspell -d english -t -c $f &"; // Windows XP, osdefault shell

////////////////////////////////////////////////////////////////////////////////
// Customization of the commands/clipper panels. Each row contains 3 to 5 strings.
// 1st string: "et", "ei", "ct", "ci", "lt", "li", "st" or "si"
//   "e" means empty, "c" clipper command, "l" local command, "s" system command
//   "t" means text, "i" "icon".
// 2nd string: command that can be of "clipper", "local" or "system" type
//   "clipper" example "{\\bf |}" (| will be replaced by the selected text)
//   "local"   example "frame.dispose()"
//   "system"  example "dvips -o |.ps |" (| will be replaced by master doc)
// 3rd string: "text" or "icon" name (.gif) to apear on button
// 4th string: optional, foreground color (case "t") or background color (case "i")
// 5th string: optional, background color (case "t")
////////////////////////////////////////////////////////////////////////////////

String[][][] tabx =
  {
     { // TAB GENE_1
       {"ct","\\documentclass[twoside,a4paper,12pt]{article}\n\n% Packages\n\\usepackage{graphicx}\n\\usepackage[hypertexnames=false]{hyperref}\n\\usepackage{amsfonts,amsmath,amsthm,amssymb}\n%\\usepackage{color}\n%\\usepackage{float}\n%\\usepackage[T1]{fontenc}\n%\\usepackage[latin1]{inputenc}\n\n% Page layout\n\\voffset-25mm \n\\hoffset-25mm\n\\textwidth170mm \n\\textheight240mm\n\\footskip10mm\n\\topmargin10mm\n\\oddsidemargin1.9cm \n\\evensidemargin1.9cm \n\\setcounter{page}{1}\n\n% Numbering of theorems, lemmas...\n\\newtheorem{teo}{Theorem}[section]\n\\newtheorem{lem}{Lemma}[section]\n\\newtheorem{cor}{Corollary}[section]\n\\newtheorem{defi}{Definition}[section]\n\\newtheorem{pro}{Properties}[section]\n\\newtheorem{proc}{Procedure}[section]\n\\newtheorem{rem}{Remark}[section]\n\n\\pagestyle{myheadings}\n\n% Document\n\\begin{document}\n\\date{}\n\n\\title{Title}\n\\author{Author}\n\\date{}\n\\maketitle\n\n\\markboth{Left}{Right}\n\n% Abstract\n\\begin{abstract}\nAbstract here\n\\end{abstract}\n\n% -------------------------------------------------------------------------------\n% Insert text here e.g. \\input{texte.tex}\n|\n%-------------------------------------------------------------------------------\n\n% Bibliography\n\\bibliographystyle{unsrt}\n%\\bibliography{biblio/article}\n\n\\end{document}\n","Article","black","orange"},
       {"ct","\\documentclass[a4paper,10pt]{letter}\n\\setlength{\\textheight}{20cm}\n\\begin{document}\n\n\\begin{letter}{Name\\\\Address}\n\\address{MyName\\\\MyAddress}\n\\opening{\\vspace{10mm}Dear Sir,}\n\n\\vspace{10mm}\n%-------------------------------------------------------------------------------\n% Insert text here \n%-------------------------------------------------------------------------------\n\n\\signature{MyName}\n\\closing{\\vspace{10mm}Yours sincerely}\n\n% Enclosure\n%\\encl{}\n\n\\end{letter}\n\\end{document}","Letter","black","orange"},
       {"ct","\\part{|}\n\\label{part-}","Part","blue"},
       {"ct","\\chapter{|}\n\\label{chap-}","Chapt","blue"},
       {"ct","\\section{|}\n\\label{sec-}","Sec","blue"},
       {"ct","\\subsection{|}\n\\label{ssec-}","Ssec","blue"},
       {"ct","\\subsubsection{|}\n\\label{sssec-}","Sssec","blue"},
       {"ct","\\paragraph{|}","Paragr","blue"},
       {"ct","{\\tiny |}","tiny"},
       {"ct","{\\footnotesize |}","footnote"},
       {"ct","{\\small |}","small"},
       {"ct","{\\normalsize |}","norm"},
       {"ct","{\\large |}","large"},
       {"ct","{\\Large |}","Large"},
       {"ct","{\\huge |}","huge"},
       {"lt","Macros.getMacro(\"LaTeX/latexBrowseAndLink\").invoke(view);","Link","red"},
       {"ct","\\documentclass[brown]{beamer}\n\\usepackage{beamerthemeshadow}\n\\usepackage{graphicx}\n\\usepackage{amsfonts,amsmath,amsthm,amssymb}\n%\\usepackage[T1]{fontenc}\n%\\usepackage[latin1]{inputenc}\n\n\\beamertemplateshadingbackground{yellow!50}{orange!50}\n\\beamertemplatetransparentcovereddynamic\n\n\\title{Title}\n\\author{Author}\n\\date{\\today}\n\n%\\logo{\\includegraphics[width=1cm]{logo.pdf}}\n\n\\begin{document}\n\n\\frame{\\titlepage}\n\n\\section[Outline]{}\n\\frame{\\tableofcontents}\n\n\\section{}\n\\frame\n{\n\\frametitle{}\n}\n\n\\frame{}\n\\end{document}","Beamer","black","orange"},
       {"lt","tutBeamer();","Tutorial","black","orange"},
       {"ct","\\frame\n{   \n\\frametitle{|}\n}","frame"},
       {"ct","\\begin{itemize}\n   \\item<+-> |\n   \\item<+->\n\\end{itemize}","itemize"},
       {"ct","\n   \\item<+-> |","item"},
       {"ct","\\pause\n","pause"},
       {"ct","<|->","from ovlay"},
       {"ct","\\only<|>","only"},
       {"ct","<-|>","to ovlay"},
       {"ct","\\transdissolve","dissolve"},
       {"ct","\begin{columns}[t]\n   \\begin{column}{5cm}\n   |\n   \\end{column}\n   \\begin{column}{5cm}\n   \n\\end{column}\n\\end{columns}","columns"},
       {"ct","\\begin{beamerboxesrounded}[shadow=true]{title}|\\end{beamerboxesrounded}","round box"},
       {"lt","latexColPick()","def color","red"},
       {"ct","{\\color{mycolor} |}","txt color"},
       {"ct","\\setlength{\\fboxrule}{0.5mm}\n\\fcolorbox{red}{white}{\\textcolor{black}{|}}","box color"},
     } ,
     { // TAB GENE_2
       {"ct","\\newline","newline","red"},
       {"ct","\\noindent","noindent","red"},
       {"ct","\\clearpage","clear pge","red"},
       {"ct","\\cleardoublepage","clear 2p","red"},
       {"ct","\n\\vspace{2mm}","v. space","red"},
       {"ct","\n\\vspace{2mm}\\noindent\\textbf{|}","paragr.","red"},
       {"ct","\\begin{center}\n|\n\\end{center}","center"},
       {"ct","\\footnote{|}","footnote"},
       {"ct","\\begin{table}[htbp]\n\\begin{center}\n\\begin{tabular}{\\|c\\|}  \\hline\n   |\n\\\\ \\hline\n\n\\\\ \\hline \\end{tabular}\n\\end{center}\n\\caption{\\label{tab-}}\n\\end{table}","tabular"},
       {"ct","\\verb\"|\"","verb"},
       {"ct","\\begin{verbatim}\n|\n\\end{verbatim}","verbatim"},
       {"ct","\\end{verbatim}\n|\n\\begin{verbatim}","antiverb"},
       {"ct","\\begin{quote}\n|\n\\end{quote}","quote"},
       {"ct","\\begin{figure}\\begin{center}\n\\includegraphics[width=10cm,height=10cm,angle=0]{|}\n\\caption{\\label{fig-}}\n\\end{center}\\end{figure}","figure"},
       {"ct","\\begin{itemize}\n\\item |\n\\end{itemize}","itemize","blue"},
       {"ct","\\begin{enumerate}\n\\item |\n\\end{enumerate}","enumer.","blue"},
       {"ct","\\begin{description}\n\\item |\n\\end{description}","descr.","blue"},
       {"ct","\n\\item","item","blue"},
       {"ct","(\\ref{|})","(ref)","red"},
       {"ct","\\S\\ref{|}","sec ref","red"},
       {"ct","page \\pageref{|}","pge ref","red"},
       {"ct","\\cite{|}","cite","red"},
       {"ct","\\emph{|}","em","blue"},
       {"ct","\\textrm{|}","rm","blue"},
       {"ct","\\textbf{|}","bf","blue"},
       {"ct","\\textsf{|}","sf","blue"},
       {"ct","\\texttt{|}","tt","blue"},
       {"ct","\\textmd{|}","md","blue"},
       {"ct","\\textit{|}","it","blue"},
       {"ct","\\textsc{|}","sc","blue"},
       {"ct","\\textsl{|}","sl","blue"},
       {"ct"," |\\index{|}","index","red"},
     } ,
     { // TAB MATH_1
       {"ct","\\begin{equation}\n\\label{eq-}\n|\n\\end{equation}","equ","black","orange"},
       {"ct","\\begin{eqnarray}\n\\label{eqn1-}\n%\\nonumber\n|\\\\\n\\label{eqn2-}\n\\end{eqnarray}","eqn","black","orange"},
       {"ct","\\[\n|\n\\]","\\[  \\]","black","orange"},
       {"ct","$|$","$$","black","orange"},
       {"ci","\\begin{array}{cc}\n | &\n\\\\\n  &\n\\end{array}","mat1"},
       {"ci","\\left[\\begin{array}{cc}\n | &\n\\\\\n  &\n\\end{array}\\right]","mat2"},
       {"ci","\\left(\\begin{array}{cc}\n | &\n\\\\\n  &\n\\end{array}\\right)","mat3"},
       //{"ci","\\left\\{\\begin{array}{cc}\n | &\n\\\\\n  &\n\\end{array}\\right\\}","mat4"},
       {"ci","\\left\\|\\begin{array}{cc}\n | &\n\\\\\n  &\n\\end{array}\\right\\|","det"},
       {"ci","\\left\\\\|\\begin{array}{cc}\n | &\n\\\\\n  &\n\\end{array}\\right\\\\|","norm"},
       //{"ci","\\left[\\begin{array}{cc}\n | \n\\\\\n  \n\\end{array}\\right.","mat5"},
       //{"ci","\\left.\\begin{array}{cc}\n | \n\\\\\n  \n\\end{array}\\right]","mat8"},
       //{"ci","\\left(\\begin{array}{cc}\n | \n\\\\\n  \n\\end{array}\\right.","mat6"},
       //{"ci","\\left.\\begin{array}{cc}\n | \n\\\\\n  \n\\end{array}\\right)","mat9"},
       {"ci","\\left\\{\\begin{array}{cc}\n | \n\\\\\n  \n\\end{array}\\right.","mat7"},
       {"ci","\\left.\\begin{array}{cc}\n | \n\\\\\n  \n\\end{array}\\right\\}","mat10"},
       {"ct","\\{|\\}","{ }"},
       {"ci","\\sum_{|}^{}","sum"},
       {"ci","\\prod_{|}^{}","prod"},
       {"ci","\\int_{|}^{}","int"},
       //{"ci","\\oint","oint"},
       {"ci","\\iint","iint"},
       //{"ci","\\iiint","iiint"},
       {"ct","\\frac{d |}{dt}","d/dt"},
       {"ci","\\partial","partial"},
       {"ci","\\nabla","nabla"},
       {"ci","\\triangle","triangle"},
       {"ci","\\widetilde{|}","widetilde"},
       {"ci","\\widehat{|}","widehat"},
       //{"ci","\\overleftarrow{|}","overleftarrow"},
       {"ci","\\dot{|}","dot"},
       {"ci","\\overrightarrow{|}","overrightarrow"},
       {"ci","\\overline{|}","overline"},
       {"ci","\\sqrt{|}","sqrt"},
       //{"ci","\\sqrt[n]{|}","sqrtn"},
       {"ci","|^{-1}","inv"},
       {"ci","\\frac{|}{}","frac"},
       {"ci","^{|}","power"},
       {"ci","_{|}","indice"},
       {"ci","\\forall","forall"},
       {"ci","\\exists","exists"},
       {"ci","\\nexists","nexists"},
       {"ci","\\mathbb{R}","mathbbr"},
       {"ci","\\mathbb{R}^{| \\times }","mathbbRpower"},
       {"ci","\\mathbb{C}","mathbbc"},
       {"ci","\\mathbb{C}^{| \\times }","mathbbCpower"},
       {"ci","\\Re","mRe"},
       {"ci","\\Im","mIm"},
       {"ci","\\complement","complement"},
       {"ci","\\ldots","ldots"},
       {"ci","\\cdots","cdots"},
       {"ci","\\ddots","ddots"},
       {"ci","\\vdots","vdots"},
       {"ci","\\subset","subset"},
       {"ci","\\in","in"},
       {"ci","\\notin","notin"},
       {"ci","\\cap","cap"},
       {"ci","\\equiv","equiv"},
       {"ci","\\simeq","simeq"},
       {"ci","\\approx","approx"},
       {"ci","\\neq","neq"},
       {"ci","\\triangleq","triangleq"},
       {"ci","\\pm","pm"},
       {"ci","\\wedge","wedge"},
       {"ci","\\vee","vee"},
       {"ci","\\times","times"},
       {"ci","\\ast","ast"},
       {"ci","\\circ","circ"},
       {"ci","\\bullet","bullet"},
       {"ci","\\oplus","oplus"},
       {"ci","\\otimes","otimes"},
       {"ci","\\odot","odot"},
       {"ci","\\infty","infty"},
     } ,
     { // TAB MATH_2
       {"ct","\\mathbf{|}","bf","black","orange"},
       {"ct","\\mathcal{|}","cal","black","orange"},
       {"ct","\\mathrm{|}","rm","black","orange"},
       {"ct","\\mathmm{|}","mm","black","orange"},
       {"ci","\\leq","leq"},
       {"ci","\\ll","ll"},
       {"ci","\\geq","geq"},
       {"ci","\\gg","gg"},
       {"ci","\\subset","subset"},
       {"ci","\\subseteq","subseteq"},
       {"ci","\\in","in"},
       {"ci","\\notin","notin"},
       {"ci","\\supset","supset"},
       {"ci","\\supseteq","supseteq"},
       {"ci","\\ni","ni"},
       {"ci","\\cap","cap"},
       {"ci","\\cup","cup"},
       {"ci","\\bigcup","bigcup"},
       {"ci","\\bigcap","bigcap"},
       {"ci","\\emptyset","emptyset"},
       //{"ci","\\coprod","coprod"},
       //{"ci","\\bigsqcup","bigsqcup"},
       //{"ci","\\bigvee","bigvee"},
       //{"ci","\\bigwedge","bigwedge"},
       //{"ci","\\bigodot","bigodot"},
       //{"ci","\\bigotimes","bigotimes"},
       //{"ci","\\bigoplus","bigoplus"},
       //{"ci","\\biguplus","biguplus"},
       {"ci","\\longrightarrow","longrightarrow"},
       {"ci","\\longleftarrow","longleftarrow"},
       {"ci","\\longleftrightarrow","longleftrightarrow"},
       {"ci","\\longmapsto","longmapsto"},
       {"ci","\\hookleftarrow","hookleftarrow"},
       {"ci","\\hookrightarrow","hookrightarrow"},
       {"ci","\\Longrightarrow","mLongrightarrow"},
       {"ci","\\Longleftarrow","mLongleftarrow"},
       {"ci","\\Longleftrightarrow","mLongleftrightarrow"},
       {"ci","\\nRightarrow","nmRightarrow"},
       {"ci","\\nLeftarrow","nmLeftarrow"},
       {"ci","\\nLeftrightarrow","nmLeftrightarrow"},
       {"ci","\\Downarrow","mDownarrow"},
       {"ci","\\Uparrow","mUparrow"},
       {"ci","\\Updownarrow","mUpdownarrow"},
       //{"ct","\\mbox{Im}","Im","red"},
       //{"ct","\\mbox{Ker}","Ker","red"},
       {"ct","\\mbox{|}","mbox","black","orange"},
       {"ct","\\arccos","acos","orange"},
       {"ct","\\arcsin","asin","orange"},
       {"ct","\\arctan","atan","orange"},
       {"ct","\\arg","arg","blue"},
       {"ct","\\cos","cos","orange"},
       {"ct","\\cosh","cosh","red"},
       //{"ct","\\cot","cot","blue"},
       {"ct","\\coth","coth","red"},
       //{"ct","\\csc","csc","blue"},
       {"ct","\\deg","deg","blue"},
       {"ct","\\det","det","blue"},
       {"ct","\\dim","dim","blue"},
       {"ct","\\exp","exp","blue"},
       //{"ct","\\gcd","gcd","blue"},
       //{"ct","\\hom","hom","blue"},
       {"ct","\\mbox{Im}","Im"},
       {"ct","\\inf","inf","black"},
       {"ct","\\mbox{Ker}","Ker"},
       //{"ct","\\lg","lg","blue"},
       {"ct","\\lim","lim","blue"},
       //{"ct","\\liminf","l.inf","blue"},
       //{"ct","\\limsup","l.sup","blue"},
       {"ct","\\ln","ln","blue"},
       {"ct","\\log","log","blue"},
       {"ct","\\max","max","black"},
       {"ct","\\min","min","black"},
       //{"ct","\\Pr","Pr","blue"},
       //{"ct","\\sec","sec","blue"},
       {"ct","\\sin","sin","orange"},
       {"ct","\\sinh","sinh","red"},
       {"ct","\\sup","sup","black"},
       {"ct","\\tan","tan","orange"},
       {"ct","\\tanh","tanh","red"},
       {"ci","\\angle","angle"},
       //{"ci","\\neg","neg"},
       //{"ci","\\surd","surd"},
       {"ci","\\top","top"},
       {"ci","\\bot","bot"},
       {"ci","\\backslash","backslash"},
     } ,
     { // TAB GREEK
       {"ci","\\alpha","alpha"},
       {"ci","\\beta","beta"},
       {"ci","\\gamma","gamma"},
       {"ci","\\delta","delta"},
       {"ci","\\epsilon","epsilon"},
       {"ci","\\varepsilon","varepsilon"},
       {"ci","\\zeta","zeta"},
       {"ci","\\eta","eta"},
       {"ci","\\theta","theta"},
       {"ci","\\vartheta","vartheta"},
       {"ci","\\iota","iota"},
       {"ci","\\kappa","kappa"},
       {"ci","\\lambda","lambda"},
       {"ci","\\mu","mu"},
       {"ci","\\nu","nu"},
       {"ci","\\xi","xi"},
       {"ci","\\pi","pi"},
       {"ci","\\varpi","varpi"},
       {"ci","\\rho","rho"},
       {"ci","\\varrho","varrho"},
       {"ci","\\sigma","sigma"},
       {"ci","\\varsigma","varsigma"},
       {"ci","\\tau","tau"},
       {"ci","\\upsilon","upsilon"},
       {"ci","\\phi","phi"},
       {"ci","\\varphi","varphi"},
       {"ci","\\chi","chi"},
       {"ci","\\psi","psi"},
       {"ci","\\omega","omega"},
       {"ci","\\Gamma","mGamma"},
       {"ci","\\Delta","mDelta"},
       {"ci","\\Theta","mTheta"},
       {"ci","\\Lambda","mLambda"},
       {"ci","\\Xi","mXi"},
       {"ci","\\Pi","mPi"},
       {"ci","\\Sigma","mSigma"},
       {"ci","\\Upsilon","mUpsilon"},
       {"ci","\\Phi","mPhi"},
       {"ci","\\Psi","mPsi"},
       {"ci","\\Omega","mOmega"},
       {"ci","\\aleph","aleph"},
     } ,
     // { // Non ascii characters
     //   {"ci","\\\"a","auml"},
     //   {"ci","\\\"A","mAuml"},
     //   {"ci","\\^a","acirc"},
     //   {"ci","\\^A","mAcirc"},
     //   {"ci","\\`a","aacute"},
     //   {"ci","\\`A","mAacute"},
     //   {"ci","\\aa{}","aring"},
     //   {"ci","\\AA{}","mAring"},
     //   {"ci","\\ae{}","aelig"},
     //   {"ci","\\AE{}","mAelig"},
     //   {"ci","\\\"e","eulm"},
     //   {"ci","\\'E","mEulm"},
     //   {"ci","\\'e","eacute"},
     //   {"ci","\\'E","mEacute"},
     //   {"ci","\\`e","egrave"},
     //   {"ci","\\`E","mEgrave"},
     //   {"ci","\\^e","ecirc"},
     //   {"ci","\\^E","mEcirc"},
     //   {"ci","\\\"{\\i}","iulm"},
     //   {"ci","\\^i","icirc"},
     //   {"ci","\\^I","mIcirc"},
     //   {"ci","\\\"o","ouml"},
     //   {"ci","\\\"O","mOuml"},
     //   {"ci","\\^o","ocirc"},
     //   {"ci","\\^O","mOcirc"},
     //   {"ci","\\o{}","oslash"},
     //   {"ci","\\O{}","mOslash"},
     //   {"ci","\\oe{}","oelig"},
     //   {"ci","\\OE{}","mOelig"},
     //   {"ci","\\\"u","uulm"},
     //   {"ci","\\\"U","mUulm"},
     //   {"ci","\\`u","ugrave"},
     //   {"ci","\\`U","mUgrave"},
     //   {"ci","\\^u","ucirc"},
     //   {"ci","\\^U","mUcirc"},
     //   {"ci","\\ss{}","szlig"},
     //   {"ci","\\~n","ntilde"},
     //   {"ci","\\c{c}","ccedil"}
     // }
     { // TAB COMMANDS
        // Examples of buttons
        //    1- Button for diplaying information in HTML format
        //    {"lt","Macros.message(view,\"<html><b>Information</b><br>Item 1<br>Item 2</html>\")","Title","black","orange"},
        //    2- Button with different fonts: "print" black, "dlxr" red/bold
        //    {"st","lp -dlxr |.ps &","<html><font color=\"black\">Print</font> <b>dlxr</b></html>","red"},
        // Examples of labels
        //    {"et","","<html><b>PRINT</b></html>","black","orange"},
        //    {"ei","","alpha","orange"},
        //    {"et","",""},

        // Title : project
        {"et","","<html><b>Project</b></html>","black","white"},
        // Master document
        {"lt","setMasterFile();","Master file","black"},
        // Label parser
        {"lt","Macros.getMacro(\"LaTeX/latexLabelParser\").invoke(view);","Parse","black"},
        // Label Go to macro
        {"lt","Macros.getMacro(\"LaTeX/latexGoto\").invoke(view);","Go to","black"},
        {"et","",""},
        {"et","",""},

        // Title : actions on the LaTeX master file
        {"et","","<html><b>Compil.</b></html>","black","white"},
        // Basic LaTeX commands
        {"st",latexString,"LaTeX"},
        {"st",pdflatexString,"pdfTeX"},
        {"st",bibtexString,"BibTeX"},
        {"st",indexString,"Index -s"},
        // Transformation dvi-> ps
        {"st",dvipsString,"Dvips"},
        // Transformation ps -> pdf (works on Unix/tetex Windows/MiKTeX other ?)
        {"st",ps2pdfString,"Ps2pdf","black"},
        {"et",""," "},

        // Title : viewers
        {"et","","<html><b>Viewers</b></html>","black","white"},
        {"st",xdviString,"Xdvi"},
        {"st",ghostviewString,"Ghostv"},
        {"st",acroreadString,"Acrobat"},
        {"et","",""},
        {"et","",""},

        // Title :External programs
        {"et","","<html><b>Ext. Progs</b></html>","black","white"},
        //{"st","\"C:\\Program Files\\JabRef 1.5\\JabRef.exe\" &","Jabref","red"},
        {"st",jabrefString,"Jabref"},
        {"st","xfig &","Xfig"},
        {"st",jpicedtString,"jPicEdt"},
        // Print
        {"st",printString,"Print"},
        // Aspell
        {"st",aspellEnString,"<html><font color=\"black\">Aspell</font> <b>en</b></html>"},
        {"et","",""},
        {"et","",""},

        // Title : This macro
        {"et","","<html><b>ThisMacro</b></html>","black","white"},
        {"lt","help();","Help","black"},
        {"lt","jEdit.openFile(view,scriptPath2);","Edit macro","black"},
        {"lt","frame.dispose();","<html><b>Close</b></html>","black"},
     },
  };

////////////////////////////////////////////////////////////////////////////////
// User defined actions
////////////////////////////////////////////////////////////////////////////////

   void setMasterFile() {
      // Master document: interactive definition in Emacs style
      String buffername = textArea.buffer.name.toLowerCase();
      int testTex = buffername.indexOf(".tex");
      if (testTex > 0) {
         main = Macros.input(view,"Name of master document \n(without \".tex\" extension)");
         if(main != null){
            textArea.goToBufferEnd(false);
            textArea.setSelectedText("\n\n%%% Local Variables:\n%%% mode: latex\n%%% TeX-master: \""+main+"\"\n%%% End:");
         }
      } else {
         Macros.message(view,"The file: " + textArea.buffer.name + " is a not a LaTeX file");
      }
   }

   void help() {


      // Help
      fullPath = scriptPath;
      for (i = 0; i < fullPath.length(); i++){
         if (fullPath.substring(i,i+1).equals("\\"))
            fullPath = fullPath.substring(0,i) + "/" +  fullPath.substring(i+1,fullPath.length());
         if (fullPath.substring(i,i+1).equals("/"))
            fp0 = fullPath.substring(0,i);
      };
      fullURL = "file:///" + fp0 + "/doc/help.html";
 //     infoviewer.InfoViewerPlugin.openURL(view, fullURL);
   
 }



   void tutBeamer() {
      

// Beamer tutorial
//       jEdit.newFile(view);
//     \section{Dynamic text}\n\\frame\n{\n   \\frametitle{Dynamic text}\n   Before\n   \\only<1>{\\textbf{Text appearing in \\underline{1st} overlay}}\n   \\only<2>{\\textbf{Text appearing in \\underline{2nd} overlay}}\n   \\only<3>{\\textbf{Text appearing in \\underline{3rd} overlay}}\n   \\only<4>{\\textbf{Text appearing in \\underline{4th} overlay}}\n   After\n}\n\n%===  Colors (and \\color<i>)\n\\section{Playing with colors}\n\\frame\n{  \n   \\frametitle{Colors}\n   \n   %===  package color\n   \\definecolor{myred}{rgb}{0.71,0.14,0.07}\n   \\textcolor{myred}{User defined color}\n   \\setlength{\\fboxrule}{0.5mm}\n   \\fcolorbox{myred}{black}{\\textcolor{white}{Now with a box}}\n   \n   \\vspace{2mm}\n   or\n \n   %===  package xcolor\n   \\vspace{2mm}\n   \\colorlet{mygreen}{green!80!black}\n   {\\color{mygreen} Other user defined color}\n   \n   \\vspace{10mm}\n   Now, colors only applied to 3rd overlay\n \n   \\vspace{2mm}  \n   \\begin{itemize}\n   \\item<+-> {\\color<3>{mygreen} First item}\n   \\item<+-> {\\color<3>{mygreen} Second item}\n   \\item<+-> {\\color<3>{myred} 3rd item}.      \n   \\end{itemize}\n   \n}\n\n%===  Colums and transition\n\\section{Playing with columns and transitions}\n\\frame\n{  \n   \\frametitle{Two columns and transitions}\n\n   %=== Most transitions only visible in full screen mode\n   %=== \\transxxxx<2>[Duration=3] means 2nd overlay, 3 seconds\n   %\\transsplithorizontalout\n   %\\transsplithorizontalin\n   %\\transsplitverticalout\n   %\\transsplitverticalin\n   %\\transblindshorizontal\n   %\\transblindsvertical\n   %\\transboxout\n   %\\transboxin[Duration=3]\n   \\transdissolve\n   %\\transwipe[direction=90]\n   %\\transglitter\n   \n   \\begin{columns}[t]\n      \\begin{column}<1>{5cm}\n      \\textbf{Column 1} \\\\ Line 1.1 \\\\ Line 1.2 \\\\ Line 1.3 \n      \\end{column}\n\n      \\begin{column}<2>{5cm}\n      \\textbf{Column 2} \\\\ Line 2.1 \\\\ Line 2.2 \\\\ Line 2.3 \n      \\end{column}\n   \\end{columns}\n}\n\n\\frame{}\n\n\\end{document}");
   }

   void latexColPick() {
      color = null;
      color = JColorChooser.showDialog(view, "LaTeX Color Picker", color);

      if (color != null){

         String mycolorstr = color.toString();
         mycolorstr = mycolorstr.substring(15,mycolorstr.length()-1);
         String[] rgb = mycolorstr.split(",");

         eval(rgb[0]);
         eval(rgb[1]);
         eval(rgb[2]);

         r = Math.round(0.3922*r)/100.0;
         g = Math.round(0.3922*g)/100.0;
         b = Math.round(0.3922*b)/100.0;

         String mycolor = Macros.input(view,"Enter color name");
         String towrite =  "\\definecolor{"+ mycolor +"}{rgb}{" + r.toString() + "," + g.toString() + "," + b.toString()+"}";

         textArea.setSelectedText(towrite);
      }
   }

