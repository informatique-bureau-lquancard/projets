<!DOCTYPE html>
<html>
<body>
<section>
<link rel="stylesheet" href="../style.css" />
<div id="bloc_page">
		<?php
		session_start();
		include('../header.html');
		include('../menu.html');
		// On recupere le choix du profil tarif à traiter
		$_SESSION['profil'] = $_POST['tarif'];
		$_SESSION['erreur'] = 'Erreur de session';
		echo $_SESSION['profil'];

		// formulaire d'upload du tarif vers le bon repertoire
		if ($_SESSION['profil'] == 'MILIMA')
		{
			echo '
				<form method="post" action="MILLESIMA/script-flux.php">
				<input type="submit" value="Récupérer le Tarif MILLESIMA" />';

		}
		else if ($_SESSION['profil'] == 'ANGWIN_HEBDO')
		{
			echo '
				<form method="post" action="ANGWIN_HEBDO/script-flux.php">
				<input type="submit" value="Récupérer le Tarif ANGWIN HEBDO" />';

		}
		else if ($_SESSION['profil'] == 'MAISOB')
		{
			echo '
				<form method="post" action="MAISOB/script-flux.php">
				<input type="submit" value="Récupérer le Tarif MAISON B" />';

		}
		else if ($_SESSION['profil'] == 'CUVFAU')
		{
			echo '
				<form method="post" action="CUVFAU/script-flux.php">
				<input type="submit" value="Récupérer le Tarif CUVELIER FAUVARQUE" />';

		}
		else if ($_SESSION['profil'] == 'NGVINS')
		{
			echo '
				<form method="post" action="NGVINS/script-flux.php">
				<input type="submit" value="Récupérer le Tarif NGVINS (automatique)" />';

		}
		else if ($_SESSION['profil'] == 'ENSEI')
		{
			echo '
				<form method="post" action="ENSEI/script.php">
				<input type="submit" value="Récupérer le Tarif ENSEI (automatique)" />';

		}
		else if ($_SESSION['profil'] == 'BORBLE')
		{
			echo '
				<form method="post" action="BORBLE/script.php">
				<input type="submit" value="Récupérer le Tarif BORBLE (automatique)" />';

		}
		else
		{
			echo '
					<form method="post" action="upload.php" enctype="multipart/form-data">
						<p>
							<label for="tarifupload">Fichier à traiter :</label>
							<input type="file" name="tarifupload" id="tarifupload">
							<input type="submit" name="envoie" value="Charger le tarif">
							<p><strong>Note :</strong> Attention : Refonte des moulinettes en cours, le controle des extensions de fichiers authorise maintenant : .csv, .xls et .xlsx<br />
							Tarifs revues, dernière mise à jour :17/02/2022 :<br />
								- JOEMEY, COMVIG, BONCHA, FARR, TERTRA2, ARTHUR, BOUEY, INFO, CRUCOL, NGVINS, ENSEI HEBDO et ENSEI, CMVINS, CPD, CUVFAU, MAISOB, PIONSA, RGRD, WINEMA, CAVHUG, ANGELWINE_HEBDO<br />
								- Les Officieux : MORTIE, YVMOFF, JOHNOF, VEYLOF, BARIOF, TWINOF, COMOFF, LDVOFF, LVDCOF</p>
							<br />
							<p><strong>Les fichiers ci-dessus n\'on pas besoin d\'être enregistrés en csv. le fichier téléchargé peut être traité tel quel.</strong><br />
							<br />
							Pour les autres fichiers, continuer de faire "Enregistrer sous" --> format CSV UTF-8, merci<br >
							<i>Un répertoire sur le serveur a été créé spécifiquement pour cet usage, il est vidé par CRON tous les jours à 22h <br />
							Chemin d acces : //partage/Tarifs pour traitement</i><br /> </p>
						</p>
					</form>';
		}
		include("particularites.php");
		include('../footer.html');
		?>
		</section>
	</body>
</div>
</html>
