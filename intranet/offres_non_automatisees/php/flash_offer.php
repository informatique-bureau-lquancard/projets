<!DOCTYPE html>
<html>
<div id="bloc_page">

<?php
	session_start();
	include('header.html');
	include('menu.html');
?>

<section>
	<form method="POST" action="flash/flash.php">
		<p>
		<label for="flash_offer">Offres flash :</label>
		<select name="origin" id="origin">
			<optgroup label = "Scripts fonctionnels">
				<option value="nisima">NISIMA</option>
				<option value="adex">ADEX WINE</option>
				<option value="boncha">BONCHATEAU</option>
			</optgroup>
			<optgroup label = "Scripts à venir">
				<option value="MAISOB">MAISON B</option>
				<option value="CHACHA">CHAIS DES CHARTREUX</option>
				<option value="TERTRA">BORDEAUX WINE LOCATORS (ANDY LENCH)</option>
				<option value="DEWITT">DEWITTE</option>
				<option value="WINSOU">WINE SOURCING</option>
			</optgroup>
		</select>
	</br>

	</br>
		<label for="message">Message :</label>
	</br>
		<textarea name="message" id="message" style="width: 100%" rows=50 required></textarea>
		</p>
	<input type="submit" value="VERIFIER" />
	</form>
	<p>
		<h2>Gestion des erreurs de scripts</h2><br />
		**********************************************<br />
		Les caisses collections ne sont pas prises en comptes par les scripts.
		Merci de les rentrer manuellement dans l'application.
	</p>
</section>

<?php
	include('footer.html');
?>

</div>
</html>
