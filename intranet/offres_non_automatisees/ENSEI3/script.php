<?php
session_start();
// Execution du script python adéquate au profil du tarif.
	$script_tarif = basename("traitement_").$_SESSION['profil'].".py";
	echo shell_exec('python3 '.$script_tarif.' 2>&1');
	$file_OUT=basename("sortie_").$_SESSION['profil'].".xlsx";
// Téléchargement du fichier de sortie .csv
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
// Après le téléchargement on supprime les fichiers .csv. On aime la propreté ici :-)
		shell_exec('rm *.xlsx');
		shell_exec('rm *.xls');
		shell_exec('rm *.csv');
		exit();
	}
	
?>