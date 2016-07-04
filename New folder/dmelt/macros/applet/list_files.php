<?php

function list_files($dir)
{
$list="";
if ($handle = opendir($dir)) {
   while (false !== ($file = readdir($handle))) {
      if ($file != "." && $file != "..") {
           $ff= $dir . $file;
           $list .= $ff . ", ";
        }
    }
    closedir($handle);
}

return $list;
}
 
?>



