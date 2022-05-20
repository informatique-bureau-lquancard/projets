<?php
	session_start();
?>
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="../style.css" />
<div id="bloc_page">
		<?php
		session_start();
		include('../header.html');
		include('../menu.html');
		?>
<?php
	// Script de création d'un fichier xls à partir du formulaire flash_offer.php
	// pour traiter ensuite avec le bon script python selon le profil de l'offre flash (nisima, chacha, adex...)
	// description du processus :
	//  - 1/ on recupere le formulaire et on crée le fichier xls
	//	- 2/ On appelle le script python selon le $_POST['origin']
	//  - 3/ On ouvre le fichier csv


	// Envoie du formulaire
	$message = $_POST['message'];
	$origin = $_POST['origin'];


	$nb_lignes = substr_count($message,"\n"); // On récupère le nombre de lignes dans $message car cela peut toujours servir...

	// on remplace tous les retours chariots 'n/' par le séparateur ';'
	$patterns = array();
	$patterns[4] = '/\n/';

	$replacements = array();
	$replacements[4] = ';';


	$imessage = preg_replace($patterns, $replacements, $message);

	$imessage = explode(';',$imessage); // $imessage est un :array
	$colMessage = array_chunk($imessage, 1); // on met en colonne

	set_time_limit(300);

	// **** Emploie de fputcsv pour créer le csv.... spreadsheet ne fonctionne plus :( **** //
	$fp = fopen('flash_offer.csv', 'w');
	fputs($fp, $bom =(chr(0xEF) . chr(0xBB) . chr(0xBF) ));
	foreach ($colMessage as $ligne)
	{
		fputcsv($fp, $ligne, ';');
	}
	fclose($fp);

	echo '<pre>';
	print_r($imessage);
	echo '</pre>';

	// Execution du script python (traitement du fichier offre_flash.csv)
	echo shell_exec('python3 '.basename('flash_').$origin.'.py 2>&1');
	$File_OUT = basename('flash_').$origin.'.csv';

	echo '<a href="'.$File_OUT.'" download="'.$File_OUT.'">Télécharger Offre</a>';

		include('../footer.html');
?>
</html>
