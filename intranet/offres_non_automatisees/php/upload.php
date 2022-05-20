<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="../style.css" />
		<title>INTRANET BLQ</title>
	</head>
<div id="bloc_page">
<?php
	session_start();
	include('../header.html');
	include('../menu.html');
?>

<?php

$tab_profil = array("GENERAL", "TRANSV", 
"ADEX", "ARTY", "ARVI","ALIOFF", "ANGWIN2", "ANGWIN_HEBDO_NON_AUTOMATIQUE", "ANGWIN_AUTRES", "ANGWIN_BDXNOTOWC", "ANGWIN_BGO", "ANGWIN_BXOWC", "ARIVOF", "ARTHUR", 
"BALOFF", "BOUEY","BORDIN", "BORBLE", "BPCWIN0", 
"CAVCAR", "CAVHUG", "CAVMAR", "CAVTOU", "CDP", "CEPAGE", "CMVINS", "COMOFF", "CRUCOL", 
"DEWITT", 
"EUROPA", 
"FARR", 
"GVS", 
"JOHNOF", "JSCD", 
"MILLE1", 
"MILLES_REGULIER", 
"NGVINS", 
"RDRG", 
"REDCIR", 
"TWINOF", 
"VEYLOF", 
"WINSOU",
"BARIOF", "BONCHA",
"CAVEX", "CDFOFF", "CLOMIL", "CRSFW",
"EXTRACT_BORDEREAUX",
"FILIPS",
"GINOFF",
"IN2WIN",
"JOEMEY",
"LDVOFF", "LVDCOF",
"MARSOI", "MHBOFF", "MORTIE",
"OENALI", "OENOE",
"QUACOU",
"SENECH", "SICHE2", "SOBOFF", "STATEV", "SWIT",
"TERTRA_HORS_BORDEAUX", "TWMOFF",
"VERSUS", "VIALOF", "VINONE", "VINTEX",
"YVMOFF",
"BOUOFF", "CDFINT", "CHACHA", "CHACOM", "CERSTE", "COMVIG", "DESCAF", "DUBOS", "ENCVIN", "ENSEI", "GABIN", "INFO", "LABERG", "MONTAG", "NISIMA", "PASTER", "PIONSA", "RGRD", "SOBOVI", "SODIVI", 
"TERTRA", "VGC", "WILKIN", "WINARO", "WINEMA", "PRECHA");

	function scriptTelechargement($nomProfil)
	{
		/*
		$general_str = "GENERAL";
		//On les différencie car ils ne seront pas similaire à la fin : general_str sera un des profils choisie / general_str_bis restera GENERAl concernant le dossier du même nom
		$general_str_bis = "GENERAL";
		*/

		if(file_exists($nomProfil . "/" . $_FILES["tarifupload"]["name"]))
		{
				echo $_FILES["tarifupload"]["name"] . " existe déjà.";
		}
		else
		{
				move_uploaded_file($_FILES["tarifupload"]["tmp_name"], $nomProfil . "/" . $_FILES["tarifupload"]["name"]);
				echo "votre fichier a été téléchargé avec succès.";
		}
	}

	session_start();

	// Vérifier que le formulaire a été soumis
	if ($_SERVER["REQUEST_METHOD"] == "POST")
	{
		//Vérifie si le fichier a été uploadé sans erreur.
		if(isset($_FILES["tarifupload"]) && $_FILES["tarifupload"]["error"] == 0)
		{
			//$allowed = array("csv" => "/tmp/php/");
			$allowedExt = array("csv", "xls", "xlsx");
			$allowedMime = array("text/csv", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-excel");
			$filename = $_FILES["tarifupload"]["name"];
			$filetype = $_FILES["tarifupload"]["type"];
			$filesize = $_FILES["tarifupload"]["size"];
			$_SESSION['charged'] = '1';

			// Vérifie l'extension du fichier
			$ext = pathinfo($filename, PATHINFO_EXTENSION);
			//if (!array_key_exists($ext, $allowed)) die("Erreur : Votre fichier n'est pas au format csv (utf-8). Merci de l'enregistrer au bon format avant de le charger.");
			if (!in_array($ext, $allowedExt)) die("Erreur : Votre fichier n'est pas au format au bon format. (csv utf-8, xls ou xlsx uniquement).");
			// Verifie la taille du fichier - 10Mo Maximum
			//$maxsize = 10 * 1024 * 1024;
			//if($filesize > $maxsize) die("Error: La taille du fichier est supérieure à la limite autorisée.");

			// Verifie le type MIME du fichier
			if (in_array($filetype, $allowedMime))
			{
				// Verifie si le fichier existe avant de le télécharger.
				foreach ($tab_profil as $value){
	
					if ($_SESSION['profil'] == $value) {
						echo '' . scriptTelechargement($_SESSION['profil']);
					}
				}

				if ($_SESSION['profil']=='ARTHUR')
				{
					if(file_exists("ARTHUR/" . $_FILES["tarifupload"]["name"]))
					{
							echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
							move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ARTHUR/" . $_FILES["tarifupload"]["name"]);
							echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ADEX')
				{
					if(file_exists("ADEX/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ADEX/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ANGWIN_BXOWC')
				{
					if(file_exists("ANGWIN_BXOWC/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ANGWIN_BXOWC/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ANGWIN_BDXNOTOWC')
				{
					if(file_exists("ANGWIN_BDXNOTOWC/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ANGWIN_BDXNOTOWC/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ANGWIN_BGO')
				{
					if(file_exists("ANGWIN_BGO/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ANGWIN_BGO/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ANGWIN_AUTRES')
				{
					if(file_exists("ANGWIN_AUTRES/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ANGWIN_AUTRES/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ARTY')
				{
					if(file_exists("ARTY/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ARTY/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ARVI')
				{
					if(file_exists("ARVI/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ARVI/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='BORDIN')
				{
					if(file_exists("BORDIN/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "BORDIN/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='BPCWIN')
				{
					if(file_exists("BPCWIN/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "BPCWIN/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CEPAGE')
				{
					if(file_exists("CEPAGE/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CEPAGE/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CDFINT')
				{
					if(file_exists("CDFINT/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CDFINT/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CDP2')
				{
					if(file_exists("CDP2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CDP2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CDP4')
				{
					if(file_exists("CDP4/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CDP4/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CERSTE')
				{
					if(file_exists("CERSTE/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CERSTE/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CHACHA')
				{
					if(file_exists("CHACHA/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CHACHA/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CHACOM')
				{
					if(file_exists("CHACOM/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CHACOM/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='COMVIG')
				{
					if(file_exists("COMVIG/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "COMVIG/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='DUBOS')
				{
					if(file_exists("DUBOS/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "DUBOS/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ENCVIN')
				{
					if(file_exists("ENCVIN/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ENCVIN/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ENSEI')
				{
					if(file_exists("ENSEI/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ENSEI/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ENSEI2')
				{
					if(file_exists("ENSEI2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ENSEI2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='FILIPS')
				{
					if(file_exists("FILIPS/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "FILIPS/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='INFO')
				{
					if(file_exists("INFO/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "INFO/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='LABERG')
				{
					if(file_exists("LABERG/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "LABERG/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='LABERG2')
				{
					if(file_exists("LABERG2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "LABERG2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='MONTAG')
				{
					if(file_exists("MONTAG/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "MONTAG/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='NISIMA')
				{
					if(file_exists("NISIMA/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "NISIMA/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				// if ($_SESSION['profil']=='NISIMA2')
				// {
				// 	if(file_exists("NISIMA2/" . $_FILES["tarifupload"]["name"]))
				// 	{
				// 		echo $_FILES["tarifupload"]["name"] . " existe déjà.";
				// 	}
				// 	else
				// 	{
				// 		move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "NISIMA2/" . $_FILES["tarifupload"]["name"]);
				// 		echo "votre fichier a été téléchargé avec succès.";
				// 	}
				// }
				if ($_SESSION['profil']=='PIONSA')
				{
					if(file_exists("PIONSA/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "PIONSA/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='SOBOVI')
				{
					if(file_exists("SOBOVI/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "SOBOVI/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='SODIVI')
				{
					if(file_exists("SODIVI/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "SODIVI/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='TERTRA')
				{
					if(file_exists("TERTRA/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "TERTRA/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='TRANSV')
				{
					if(file_exists("TRANSV/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "TRANSV/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='VGC')
				{
					if(file_exists("VGC/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "VGC/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='WILKIN')
				{
					if(file_exists("WILKIN/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "WILKIN/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='WINARO')
				{
					if(file_exists("WINARO/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "WINARO/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='WINEMA')
				{
					if(file_exists("WINEMA/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "WINEMA/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='BOUOFF')
				{
					if(file_exists("BOUOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "BOUOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='DESCAF')
				{
					if(file_exists("DESCAF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "DESCAF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='PASTER')
				{
					if(file_exists("PASTER/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "PASTER/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='GABIN')
				{
					if(file_exists("GABIN/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "GABIN/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='IN2WIN')
				{
					if(file_exists("IN2WIN/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "IN2WIN/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='GINOFF')
				{
					if(file_exists("GINOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "GINOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CLOMIL')
				{
					if(file_exists("CLOMIL/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CLOMIL/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='SOBOFF')
				{
					if(file_exists("SOBOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "SOBOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}

				if ($_SESSION['profil']=='BARIOF')
				{
					if(file_exists("BARIOF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "BARIOF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CDFOFF')
				{
					if(file_exists("CDFOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CDFOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='TWMOFF')
				{
					if(file_exists("TWMOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "TWMOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ARIVOF')
				{
					if(file_exists("ARIVOF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ARIVOF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='LDVOFF')
				{
					if(file_exists("LDVOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "LDVOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='LVDCOF')
				{
					if(file_exists("LVDCOF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "LVDCOF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='VIALOF')
				{
					if(file_exists("VIALOF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "VIALOF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='VINONE')
				{
					if(file_exists("VINONE/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "VINONE/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='BONCHA')
				{
					if(file_exists("BONCHA/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "BONCHA/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='VERSUS')
				{
					if(file_exists("VERSUS/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "VERSUS/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='SWIT')
				{
					if(file_exists("SWIT/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "SWIT/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='DEWITT2')
				{
					if(file_exists("DEWITT2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "DEWITT2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='DEWITT3')
				{
					if(file_exists("DEWITT3/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "DEWITT3/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ENSEI3')
				{
					if(file_exists("ENSEI3/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ENSEI3/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='OENOE')
				{
					if(file_exists("OENOE/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "OENOE/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='STATEV')
				{
					if(file_exists("STATEV/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "STATEV/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CLOMIL2')
				{
					if(file_exists("CLOMIL2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CLOMIL2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CLOMIL3')
				{
					if(file_exists("CLOMIL3/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CLOMIL3/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='VGC2')
				{
					if(file_exists("VGC2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "VGC2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='SICHE2')
				{
					if(file_exists("SICHE2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "SICHE2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='OENALI')
				{
					if(file_exists("OENALI/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "OENALI/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CDP3')
				{
					if(file_exists("CDP3/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CDP3/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='BOUEY')
				{
					if(file_exists("BOUEY/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "BOUEY/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='ANGWIN2')
				{
					if(file_exists("ANGWIN2/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "ANGWIN2/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CUVFAU')
				{
					if(file_exists("CUVFAU/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CUVFAU/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				// if ($_SESSION['profil']=='CAVCAR2')
				// {
				// 	if(file_exists("CAVCAR2/" . $_FILES["tarifupload"]["name"]))
				// 	{
				// 		echo $_FILES["tarifupload"]["name"] . " existe déjà.";
				// 	}
				// 	else
				// 	{
				// 		move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CAVCAR2/" . $_FILES["tarifupload"]["name"]);
				// 		echo "votre fichier a été téléchargé avec succès.";
				// 	}
				// }
				if ($_SESSION['profil']=='CAVEX')
				{
					if(file_exists("CAVEX/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CAVEX/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='VINTEX')
				{
					if(file_exists("VINTEX/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "VINTEX/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='CRSFW')
				{
					if(file_exists("CRSFW/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "CRSFW/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='EXTRACT_BORDEREAUX')
				{
					if(file_exists("EXTRACT_BORDEREAUX/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "EXTRACT_BORDEREAUX/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='MARSOI')
				{
					if(file_exists("MARSOI/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "MARSOI/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='JOEMEY')
				{
					if(file_exists("JOEMEY/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "JOEMEY/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='YVMOFF')
				{
					if(file_exists("YVMOFF/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "YVMOFF/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
				if ($_SESSION['profil']=='MORTIE')
				{
					if(file_exists("MORTIE/" . $_FILES["tarifupload"]["name"]))
					{
						echo $_FILES["tarifupload"]["name"] . " existe déjà.";
					}
					else
					{
						move_uploaded_file($_FILES["tarifupload"]["tmp_name"], "MORTIE/" . $_FILES["tarifupload"]["name"]);
						echo "votre fichier a été téléchargé avec succès.";
					}
				}
			}
			else
			{
				echo "Error: Il y a eu un probème de téléchargement de votre fichier. Veuillez réessayer.";
			}
		}
		else
		{
			echo "Error: " . $_FILES["tarifupload"]["error"];
			$_SESSION['charged'] = '0';
		}
	}
	include("redirect.php");
	include("progressbar.php");
	?>
	<br>
		<input type="button" onclick="window.location.href='/traitement_tarifs.php'"; value="TRAITER UN NOUVEAU TARIF" />
	</section>
</body>
</html>
