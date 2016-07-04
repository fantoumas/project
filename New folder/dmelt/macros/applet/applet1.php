<?php

require("list_files.php");

$list=list_files("lib/system/") . ", " . 
      list_files("lib/freehep/");
$html_body  = "";
$html_body .= <<<EOT
<html>
<body>
<h1>Histogram example</h1>
<APPLET
  CODE="Example1.class"
  WIDTH=0 HEIGHT=0 ARCHIVE="$list"> 
  Please use a Java-enabled browser.
</APPLET>
</body>
</html>
EOT;

print $html_body 
?>



