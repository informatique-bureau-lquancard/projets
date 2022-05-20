<?php

	echo shell_exec('python3 traitement_TRANSV.py 2>&1');
	$file='sortie_TRANSV.csv';

	if (($file !="") && (file_exists($file)))
	{
		$size = filesize($file);
		header("content-type: application/force-download; name=$file");
		header("content-Transfer-Encoding: binary");
		header("content-Length: $size");
		header("content-Disposition: attachment; filename=$file");
		header("Expires: 0");
		header("Cache-control: no-cache, must-revalidate");
		header("Pragma: no-cache");
		readfile("$file");
		shell_exec('rm *.csv');
		exit();
	}
	
?>