<?php
session_start();
	$file_IN = basename("var/www/html/php/ANGWIN_AUTRES/traitement_").$_SESSION['profil'].".py";
	echo shell_exec('python3 '.$file_IN.' 2>&1');
	$file_OUT='sortie_ANGWIN_AUTRES.csv';

	if (($file_OUT !="") && (file_exists($file_OUT)))
	{
		$size = filesize($file_OUT);
		header("content-type: application/force-download; name=$file_OUT");
		header("content-Transfer-Encoding: binary");
		header("content-Length: $size");
		header("content-Disposition: attachment; filename=$file_OUT");
		header("Expires: 0");
		header("Cache-control: no-cache, must-revalidate");
		header("Pragma: no-cache");
		readfile("$file_OUT");
		shell_exec('rm *.csv');
		exit();
	}
	
?>