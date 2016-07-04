#!/usr/bin/perl
# This perl script is invoked by the Jedit BeanShell script latexLabelParser.bsh
# Version 18-May-2006.
#
# This script parses the files of a LaTeX project. There are some restrictions,
# briefly, uses basix LaTeX (or use LaTeX like I do ;-).
# For example
#     - do not replace \begin{equation} e.g., by \begequ otherwise, labels inside
#     an equation field will not be treated as expected or will be ignored.
#     similar for other fields.
#     - for an exotic field "foo", put the \label{..} just after \begin{foo},
#     possibly on the following line.
#     - use extension .tex, not .TEX (Windows),
#     - don't use blanks in file names,
#     - if possible, put project files in the same directory, however some
#     flexibility is offered but with some limitations.
#     - bibliography assumed to be defined in the master file
#     - and so on.
#
# Invokation of this script:
#    perl latexLabelParser.pl /full_path_to/foo.tex
# if foo.tex is not the master file it must contain a line of the form
#    %%% TeX-master: "master_file_name"
#
# Copyright (C) 2006 Jean-Francois Magni
# E-mail: jfmagni_at_free_dot_fr

################################################################################
#  MASTER FILE IF ANY
################################################################################

# File name and file dir
   $fileName = $ARGV[0];
   $dirName = $fileName;
   unless ($dirName =~ m/(.*?)(([\w\.]+)\.(tex|TEX))/) {
     die "The considered file is not a LaTeX file";
   }
   $dirName = $1;
   $masterDoc = $3;
   $projectFiles = " \% Project Files:";

# Read file contents and Look for master document
   open(FICH_OPEN, "$fileName") or die "Cannot open $fileName for read :$!";
   @contents = <FICH_OPEN>;
   close(FICH_OPEN);
   # Remove comments and join
   $jointMasterDocContents = join("\n",@contents);
   $jointMasterDocContents =~ s/%+.*?\n//g;

   $isMain = 0; # = 0 for isolated file, = 1 if exists a master document
   foreach $ligne (@contents) {
      if ($ligne =~ m/%{3,3} *TeX\-master\: *\"([\w \-\:\.]*)\"/) {
         $masterDoc = $1;
         $isMain = 1;
      }
      if ($ligne =~ m/%{3,3} *TeX\-single\: *\"([\w \-\:\.]*)\"/) {
         # Test useful if it is .labelTeX.tex which was parsed
         $masterDoc = $1;
         $isMain = 0;
      }
   }

# Read master doc contents
   print "Master doc = $masterDoc\n";
   if ($isMain == 1) {
      open(FICH_OPEN, "$dirName$masterDoc.tex") or die "Cannot open master doc $dirName$masterDoc.tex :$!";
      @masterDocContents = <FICH_OPEN>;
      close(FICH_OPEN);
      $projectFiles = " \% Project Files:\n : \"$dirName$masterDoc.tex\"";
      # Join, remove comments
      $jointMasterDocContents = join("\n",@masterDocContents);
      $jointMasterDocContents =~ s/%+.*?\n//g;
   }

# Biblio files (if in master doc)
   if ($jointMasterDocContents =~ /\\bibliography\{(.*)\}/){
      #$biblioFiles = " \"$1\.bib\"";
      #$biblioFiles =~ s/,/\.bib\"\n \"/g;
      @biblioFiles = split(/,/,$1);
      for ($i=0;$i<=$#biblioFiles;$i++){
         # Treats absolute paths
         unless ($biblioFiles[$i] =~ /^[\/]/) {
            $biblioFiles[$i] = "$dirName$biblioFiles[$i]";
         }
         # Replace // by /
         $fn =~ s#//#/#g; # Unix
         # Replace /foo1/../foo2 by /foo2
         $biblioFiles[$i] =~ s/\/[^\/]*?\/\.\.\//\//g; # Unix
         $biblioFiles[$i] =~ s/\\[^\\]*?\\\.\.\\/\\/g; # Windows
      }
      $biblioFiles = join("\.bib\"\n : \"",@biblioFiles);
      $biblioFiles = " : \"$biblioFiles\.bib\"";
   }

################################################################################
#  OTHER FILES AND LINE NUMBERING AT LABELS
################################################################################

# Look for \include{file}, \input{file.tex} or \include{../file} or \include{/foo/file} or etc... and concatenate all files
   $Imax = 100; # Limited to $Imax files (in case the while loop doesn't end)
   $I = 0;
   $prevInfoFile = "";
   # Remove some newcommands (only in master doc) which might interfere with doc parsing
   $jointMasterDocContents =~ s/\\newcommand.*\\begin\{equation\}.*\n//g;
   $jointMasterDocContents =~ s/\\newcommand.*\\begin\{eqnarray\}.*\n//g;
   $jointMasterDocContents =~ s/\\newcommand.*\\begin\{figure\}.*\n//g;
   $jointMasterDocContents =~ s/\\newcommand.*\\begin\{table\}.*\n//g;
   # For a single isolated file, replace its content by \input{the_isolated_file}
   # then treatment in the while loop
   if ($isMain == 0){
      $jointMasterDocContents = "\\input\{$masterDoc\}";
   }
   # Search , instert, treat
   while ($jointMasterDocContents =~ m/(\\input\{([\.\/\\\w]+?)(\.tex)?\})/ || $jointMasterDocContents =~ m/(\\include\{([\.\/\\\w]+?)\})/) {
      $childFileName = "$2.tex";
      $toBeReplaced = $1;

      # Treats absolute paths
      if ($childFileName =~ /^[\\\/]/) {
         $fn = "$childFileName";
      } else {
         $fn = "$dirName$childFileName";
      }
      # Replace // by /
      $fn =~ s#//#/#g; # Unix
      # Replace /foo1/../foo2 by /foo2
      $fn =~ s/\/[^\/]*?\/\.\.\//\//g; # Unix
      $fn =~ s/\\[^\\]*?\\\.\.\\/\\/g; # Windows
      print "Child file = $fn\n";
      $projectFiles = "$projectFiles\n : \"$fn\"";

      # Read $f
      open(FICH_OPEN, "$fn") or die "Cannot open $fn for read :$!";
      @contentsi = <FICH_OPEN>;
      close(FICH_OPEN);

      # Add line number (as in LN_333_NL) just after \label{xxxx}
      for ($i=0;$i<$#contentsi;$i++){
         $ip=$i+1;
         unless($contentsi[$i]=~/\\\w+\{[^{}]+\}/) { # \w might not contain letters with accents
            # Remove lines without \xxx{yyy}
            $contentsi[$i]="";
         } else {
            # Add line number (as in LN_333_NL)
            $strline = "LN_".$ip."_NL";
            $contentsi[$i]=~s/(\\label\{.*?\})/$1$strline/g;
         }
      };

      # Remove comments and join
      $jointcontentsi = join("\n",@contentsi);
      $jointcontentsi =~ s/%+.*?\n//g;

      # For robustness, remove my own key words.
      # I assume that LN_\d+_NL cannot appear in original text
      $jointcontentsi =~ s/CUT_HERE/Cut_here/g;
      $jointcontentsi =~ s/HERE_CUT/Here_cut/g;

      # Include new file contents
      $infoFile = "CUT_HEREFILE$childFileName\'\' : \"$fn\" HERE_CUT";
      $jointMasterDocContents =~ s/$toBeReplaced/$infoFile.$jointcontentsi$prevInfoFile/;
      $prevInfoFile = $infoFile;
      $I++;
      if ($I == $Imax) {return};
   }

################################################################################
#  TREATMENT OF LABELS
################################################################################

# Text of interest wiil be between CUT_HERE and HERE_CUT
   $jointContents = $jointMasterDocContents;
   $jointContents =~ s/\n//g;
   $jointContents =~ s/\\begin\{equation\}.*?\\label\{(.*?)\}LN_(\d+)_NL(.*?)\\end\{equation\}/CUT_HERE$2 "equ" \(\\ref\{$1\}\)HERE_CUT$3/g;
   $jointContents =~ s/\\begin\{eqnarray\}.*?\\label\{(.*?)\}LN_(\d+)_NL(.*?)\\end\{eqnarray\}/CUT_HERE$2 "eqn" \(\\ref\{$1\}\)HERE_CUT$3/g;
   $jointContents =~ s/\\begin\{figure\}.*?\\label\{(.*?)\}LN_(\d+)_NL(.*?)\\end\{figure\}/CUT_HERE$2 "FIG" \\ref\{$1\}HERE_CUT$3/g;
   $jointContents =~ s/\\begin\{table\}.*?\\label\{(.*?)\}LN_(\d+)_NL(.*?)\\end\{table\}/CUT_HERE$2 "TAB" \\ref\{$1\}HERE_CUT$3/g;
   # Next for more exotic fields like lemma, theorem....
   $jointContents =~ s/\\begin\{(\w*?)\}\\label\{(.*?)}LN_(\d+)_NL/CUT_HERE$3 "$1" \\ref\{$2\}HERE_CUT/g;
   # Remaining labels (for chapters, sections...)
   $jointContents =~ s/\\label\{(.*?)\}LN_(\d+)_NL/CUT_HERE$2 "lab" \\ref\{$1\}HERE_CUT/g;
   # Sections....
   $jointContents =~ s/\\section\{(.*?)\}/CUT_HERE\n %=SECTION= $1 HERE_CUT/g;
   $jointContents =~ s/\\subsection\{(.*?)\}/CUT_HERE%-SubSEC-- $1 HERE_CUT/g;
   $jointContents =~ s/\\subsubsection\{(.*?)\}/CUT_HERE%-SubSubS- $1 HERE_CUT/g;
   $jointContents =~ s/\\chapter\{(.*?)\}/CUT_HERE\n %=============================================\n %=CHAPTER== $1 HERE_CUT/g;


# Extract text between CUT_HERE and HERE_CUT
   @lines = split(/CUT_HERE/,$jointContents);
   for ($i=0; $i <= $#lines; $i++) {
      @linei = split(/HERE_CUT/,$lines[$i]);
      if ($lines[$i] =~ /SECTION|Sub|CHAPTER|PART|FILE/) {
         $lines[$i] = "$linei[0]\n";
         $lines[$i] =~ s/FILE/\n \`\`/;
      } else {
         $lines[$i] = "$linei[0]\n";
      }
   }

################################################################################
#  IMPROVEMENT OF OUTPUT AND PRINT OUTPUT TO FILE
################################################################################

# Add pageref
   for ($i=1; $i <= $#lines; $i++) {
      $lines[$i] =~ s/(\(?\\ref(\{.+?\})\)?)/$1, page \\pageref$2/;
   }

# Replace empty first line by a comment plus list of project files
   $lines[0] = "% This is not a LaTeX file, it has .tex extension for colored syntax\n% Copy references and paste them into your LaTeX document\n% To jump to some label in a file of the project, move the caret on\n% the label where you want to go to and click the \"Go to\" button\n\n$projectFiles\n$biblioFiles\n";

# Final treatment of file references
   $lines[$#lines] = "";
   $jlines = join("CUT_CUT",@lines);
   # Removes one of ajacent references to files
   $jlines =~ s/CUT_CUT *\n *\`\`.*?\'\'.*?\n(CUT_CUT *\n *\`\`.*?\'\'.*?\nCUT_CUT *\n)/$1/g;
   # Add blank line if necessary
   $jlines =~ s/(CUT_CUT *\n *\`\`.*?\'\'.*?\nCUT_CUT)[^\n]/$1\n/g;
   @lines = split(/CUT_CUT/,$jlines);

# Add a line which refers to master document in case the file .labelTeX.tex is parsed
    if($isMain == 0) {
       @lines[$#lines+1] = "\n %%% TeX-single: \"$masterDoc\"";
    } else {
       @lines[$#lines+1] = "\n %%% TeX-master: \"$masterDoc\"";
    }

# Write result in a file
   if (length($dirName) > 0) {
      print "Change directory to -> $dirName\n";
      chdir $dirName;
   } else {
      print "No chdir\n";
   }
   open(FICH_OPEN2,">.labelTeX.tex") or die "Cannot open .labelTeX.tex for write :$!";
   print FICH_OPEN2 "@lines";
   close(FICH_OPEN2);

# Open the file in jedit or reload it
   #@toExecute = ("jedit","reuseview","\"$dirName.labelTeX.tex\"");
   #print "Command: @toExecute\n";
   #system(@toExecute);
   ## doesn't work on Windows because bug / jedit call


