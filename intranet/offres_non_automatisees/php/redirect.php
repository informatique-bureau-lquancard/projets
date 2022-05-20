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
"BOUOFF", "CDFINT", "CHACHA", "CHACOM", "CERSTE", "COMVIG", "DESCAF", "DUBOS", "ENCVIN", "ENSEI", "GABIN", "INFO", "LABERG","MONTAG", "NISIMA", "PASTER", "PIONSA", "RGRD", "SOBOVI", "SODIVI", 
"TERTRA", "VGC", "WILKIN", "WINARO", "WINEMA", "PRECHA");

function scriptLancement($nomProfil)
{

	$variable = 
	'<html>
		<head>
			<meta charset="utf-8" />
			<title>' . $nomProfil . '</title>
		</head>
		<body>
			<form method="post" action="' . $nomProfil . '/script.php">
			<input type="submit" value="Lancer traitement ' . $nomProfil . '" />
			</form>
		</body>
	</html>';

	return $variable;
}

foreach ($tab_profil as $value){
	
    if ($_SESSION['profil'] == $value) {
		echo '' . scriptLancement($_SESSION['profil']);
	}
}

?>



