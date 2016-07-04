Version 19-May-2006

The main macro of this macro bundle is LaTeX.bsh. The other macros
(latexBrowseAndLink.bsh, latexColPick.bsh and latexLabelParser.bsh
latexGoto.bsh) can be invoked via LaTeX.bsh

LaTeX.bsh is a macro similar to the clipper/Xinsert pluggings but all
commands can be reached with at most two mouse clicks. A command panel
permits the user to launch latex, pdflatex etc....

It has been tested on Windows XP/2000, various Linux/x86, Free BSD/x86
and Solaris/sparc, Mac, java versions "1.4.2" and higher, Jedit 4.2final.

This version is for use with LaTeX, but the file "LaTeX.js" can be
duplicated and easily customized, for example for HTML.

More details in doc/help.html or http://jfmagni.free.fr/doc/help.html

INSTALLATION

Unzip the tarball LaTeX.zip in "~/.jedit/macros". All files and directories must
be in the same sub-directory of "~/.jedit/macros" (all files are invoked by
LaTeX.bsh).

Rescan macros and select "LaTeX" from the "macro" menu of Jedit, click the "Cmds"
tab, then the "Help" button.

Minimum customization. Check and adapt to your system the default paths to standard
LaTeX commands and viewers: click the "Edit macro" button (the clip library and
all commands can also be customized as explained in the help file).

% IMPORTANT %
At the time this macro is published, the current console plugin (version
4.2.6.1) doesn't work properly. If the command panel of LaTeX.bsh doesn't
work I suggest three possibilities for fixing this problem:
1- Replace the console plugin by an older version, download:
   http://jfmagni.free.fr/doc/Console.jar
   and overwrite the Console.jar file in ~/.jedit/jars.
2- On Unix platforms, change the "shell prefix" to bash:
   Plugins -> Plugins options -> Console -> General -> Shell Prefix
3- If you don't want to use bash, with sh you can still use this macro but
   you must modify two files: LaTeX.bsh and latexLabelParser.bsh (search
   the line containing BASH and comment/uncomment the relevant lines.

Note that the label parser is a Perl script that will work only if Perl is
installed. The "Go to" macro depends also on the Perl parser.

If you change the name of the directory "LaTeX" that contains all the files
of this tarball you will have to edit LaTeX.js for adapting the following strings:
{"lt","Macros.getMacro(\"LaTeX/latexBrowseAndLink\").invoke(view);","Link"}
{"lt","Macros.getMacro(\"LaTeX/latexLabelParser\").invoke(view);","Parse doc"},
etc...


LIST OF FILES and DIRECTORIES

LaTeX.bsh                Main macro
LaTeX.js                 Part of the main macro that can be customized
README.txt               This file
doc/                     HTML documentation
imagescol/               Cliparts for the dialog window
latexGoto.bsh            Invoked by LaTeX.bsh (for navigation in a LaTeX project)
latexBrowseAndLink.bsh   Invoked by LaTeX.bsh (for linking figures and other files)
latexColPick.bsh         Invoked by LaTeX.bsh (color picker for LaTeX)
latexLabelParser.bsh     Invoked by LaTeX.bsh (elementary label parser)
latexLabelParser.pl      Perl script invoked by the above macro
latexIndex.ist           Index customization (see button "Index -s")

FEEDBACK TO

jfmagni_at_free_dot_fr
