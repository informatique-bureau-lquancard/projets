<!DOCTYPE html>
<div id="bloc_page">

<html>
<link rel="stylesheet" href="../style.css" />
  <?php
    session_start();
    include('header.html');
    include('menu.html');
   ?>
</html>
		<section>
		<form method="post" action="php/select_tarif.php">
			<p>
				<label for="tarif">Sélectionnez le tarif à normaliser :</label><br />
				<select name="tarif" id="tarif">
					<optgroup class='red' label="MOULINETTE PRECAMPAGNE CHATEAU">
						<option value="PRECHA">BEAUTIFUL PRECAMPAGNE CHATEAU</option>
					<optgroup class='green' label="TARIFS HEBDOMADAIRE" class = "groupehebdo">
						<option value="MILIMA" class="opt_flux">MILLESIMA (flux automatique xml)</option>
						<option value="ANGWIN_HEBDO" class="opt_flux">ANGEL WINES HEBDO (flux automatique xml)</option>
						<!-- <option value="ANGWIN_HEBDO_NON_AUTOMATIQUE" class="opt_flux">ANGEL WINES HEBDO (ANGWIN_HEBDO_NON_AUTOMATIQUE, xlsx)</option> -->
						<option value="CUVFAU" class="opt_flux">CUVELIER FAUVARQUE (flux automatique google)</option>
						<option value="MILLE1" class="opt_old">MILLESIMES HEBDO (MILLES_HEBDO, csv)</option>
						<option value="ENCVIN" class="opt_old">ENCLOS DES VINS (L')</option>
						<option value="ENSEI" class="opt_old">ENSEIGNE DU BORDEAUX</option>
						<option value="CDFINT" class="opt_old">CRUS ET DOMAINES DE FRANCE</option>
						<option value="CHACOM" class="opt_old">CHATEAUX.COM</option>
						<option value="MAISOB" class="opt_flux">MAISON B (flux automatique google)</option>
						<option value="NGVINS" class="opt_flux">NGVINS</option>
						<option value="WINEMA" class="opt_excel">WINE MANIA (Excel)</option>
						<option value="INFO" class="opt_excel">LES GRANDS CRUS (Excel)</option>
						<option value="SOBOFF" class="opt_old">SOBOVI EXPORT</option>
						<option value="ARVI" class="opt_old">ARVI</option>
						<option value="FARR" class="opt_excel">FARR VINTNERS (version Excel)</option>
						<option value="BORDIN" class="opt_old">BORDEAUX INDEX</option>
						<option value="WILKIN" class="opt_old">WILKINSON</option>
						<option value="QUACOU" class="opt_old">QUATRE COULEURS HEBDO (QUACOU, csv)</option>
						<!-- <option value="CRSFW">CRSFW</option> -->
					</optgroup>
					<optgroup label="TARIFS REGULIERS">
						<option value="ADEX">ADEX WINE</option>
						<option value="ANGWIN2">ANGELWINE 2.0</option>
						<option value="BONCHA">BONCHATEAU (BONCHA, xls ou xlsx)</option>
						<option value="BORBLE">BORDEAUX BLENDS (BORBLE, téléchargement Automatique)</option>

						<!-- BORDEAUX BLENDS GENERAL -->
						<option value="GENERAL">GENERAL</option>

						<option value="BOUEY">MAISON BOUEY (Excel)</option>
						<option value="BPCWIN">BORDEAUX PREMIER CRUS (BPCWIN)</option>
						<option value="CDP">CELLIER DES PRODUCTEURS (CDP, xls)</option>
						<!-- <option value="CDP2">CELLIER DES PRODUCTEURS (si CDP ne fonctionne pas)</option>  -->
						<!-- <option value="CDP4">CELLIER DES PRODUCTEURS (PRESQUE PROPRE)</option> -->
						<option value="CEPAGE">CEP'AGE</option>
						<option value="CERSTE">CERCLE DES VIGNERONS DE ST EMILION</option>
						<option value="CHACHA">CHAIS DES CHARTREUX</option>
						<option value="CLOMIL">CLOS DES MILLESIMES</option>
						<option value="CLOMIL2">CLOS DES MILLESIMES (new 16/12/2019)</option>
						<option value="CLOMIL3">CLOS DES MILLESIMES (Jimi/new 11/09/2020)</option>
						<option value="CMVINS">CM VINS (Cédric Manet, xlsx)</option>
						<option value="COMVIG">COMPTOIR DES VIGNOBLES (Excel)</option>
						<option value="CRUCOL">CRUS & COLLECTIONS (CRUCOL, xlsx)</option>
						<option value="DEWITT">DEWITTE (traitement en xlsx vers csv)</option>
						<!-- <option value="DEWITT2">DEWITTE2</option>
						<option value="DEWITT3">DEWITTE3</option> -->
						<option value="DUBOS">DUBOS (MAISON)</option>
						<option value="ENSEI">ENSEIGNE DU BORDEAUX (L')</option>
						<option value="ENSEI2">ENSEIGNE 2 - (SI ENSEI ne fonctionne pas)</option>
						<option value="EUROPA">EUROPA (xlsx)</option>
						<option value="GABIN">MAISON GABIN</option>
						<option value="GVS">GRANDS VINS SELECTION (GVS, xlsx)</option>
						<option value="IN2WIN">IN2WINES</option>
						<option value="JOEMEY">JOEL MEYER Grands Vins & Rareté (Version Excel) </option>
						<option value="LABERG">LA BERGERE</option>
						<option value="MARSOI">MARCHAND DE SOIF (Excel)</option>
						<option value="MILLES_REGULIER">MILLESIMES REGULIER (MILLES_REGULIER, csv)</option>
						<option value="MONTAG">MONTAGNAC (Maison)</option>
						<option value="NISIMA">NISIMA (Excel)</option>
						<!-- <option value="NISIMA2">NISIMA (New 30/07/2020)</option> -->
						<option value="OENALI">OENALI (CASTEL GRANDS CRUS)</option>
						<option value="OENOE">OENOE</option>
						<option value="PASTER">LA PASSION DES TERROIRS (PASTER)</option>
						<!-- <option value="QUACOU">QUATRE COULEURS</option> -->
						<option value="REDCIR">THE RED CIRCLE SAS</option>
						<option value="RDRG">RIVE DROITE RIVE GAUCHE (xls)</option>
						<option value="JSCD">MAISON SERRE (JSCD, xlsx)</option>
						<option value="SODIVI">SODIVIN</option>
						<!-- <option value="TERTRA">BORDEAUX WINE LOCATORS (TERTRA)</option> -->
						<option value="TERTRA">TERROIRS & TRADITIONS (AMELIE GRANT - TERTRA, xlsx)</option>
						<option value="TRANSV">TRANSVIN</option>
						<option value="VINTEX">VINTEX</option>
						<!-- <option value="VGC">VGC</option> -->
						<option value="VGC">VGC (Excel) </option>
						<option value="WINARO">WINE AROUND</option>
						<option value="WINSOU">WINES SOURCING (xlsx)</option>
					</optgroup>
					<optgroup label="TARIFS OFFICIEUX">
						<option value="BOUOFF">MAISON BOUEY OFFICIEUX</option>
						<option value="DESCAF">DESCAS OFFICIEUX</option>
						<option value="GINOFF">GINESTET OFFICIEUX</option>
					</optgroup>
					<optgroup label="TARIFS EXPORT OFFICIEUX">
						<option value="ALIOFF">ALIAS EXPORT OFFICIEUX (ALIOFF, csv)</option>
						<option value="ARIVOF">AUTRES RIVAGES EXPORT OFFICIEUX (Excel)</option>
						<option value="BALOFF">BALLANDE ET MENERET EXPORT OFFICIEUX (BALOFF, csv)</option>
						<option value="BARIOF">BARRIERE FRERES OFFICIEUX (Excel)</option>
						<option value="CDFOFF">C.D.F. OFFICIEUX</option>
						<option value="COMOFF">COMPAGNIE MEDOCAINE OFFICIEUX (Excel)</option>
						<option value="JOHNOF">NATH JOHNSTON OFFICIEUX (Excel)</option>
						<option value="LDVOFF">LD VINS OFFICIEUX (Excel)</option>
						<option value="LVDCOF">LES VINS DE CRUS OFFICIEUX (Excel)</option>
						<option value="MORTIE">MORTIER OFFICIEUX (Excel)</option>
						<option value="MHBOFF">MAHLER BESSE OFFICIEUX</option>
						<option value="SICHE2">SICHEL EXPORT OFFICIEUX</option>
						<option value="SOBOFF">SOBOVI EXPORT OFFICIEUX</option>
						<option value="TWINOF">TWINS EXPORT OFFICIEUX (Excel)</option>
						<!-- <option value="TWMOFF">THE WINE MERCHANT EXPORT OFFICIEUX</option> -->
						<option value="VEYLOF">VEYRET LATOUR EXPORT OFFICIEUX (Excel)</option>
						<!-- <option value="VEYLOF2">VEYRET LATOUR EXPORT OFFICIEUX (new 18/12/2019)</option> -->
						<option value="VIALOF">LOUIS VIALARD EXPORT OFFICIEUX</option>
						<option value="YVMOFF">YVON MAU OFFICIEUX (Excel)</option>
					</optgroup>
					<!-- <optgroup label="FLUX XML">
						<option value="MILLESIMA">MILLESIMA (test)</option>
					</optgroup> -->
					<optgroup label="ETRANGERS ET HORS BORDEAUX">
						<option value="ARTY">ARTY WINE</option>
						<option value="ARTHUR">ARTHUR'S CELLAR (Excel)</option>
						<option value="CAVCAR">CAVE CARRIERE (CAVCAR, csv)</option>
						<!-- <option value="CAVCAR2">CAVE CARRIERE (NEW 21/12/2020)</option> -->
						<option value="CAVEX">CAVE EXCHANGE (CAVEX)</option>
						<option value="CAVMAR">LA CAVE DU MARCHE (CAVMAR, csv)</option>
						<option value="CAVHUG">LA CAVE D'HUGO (CAVHUG, xlsx)</option>
						<option value="CAVTOU">LE CAVEAU DE LA TOUR (CAVTOU, xlsx)</option>
						<option value="FILIPS">FILIPS (csv)</option>
						<option value="PIONSA">PIONSA (version Excel)</option>
						<option value="SENECH">SENECH (xlsx)</option>
						<option value="SWIT">SWIT</option>
						<option value="TERTRA_HORS_BORDEAUX">TERTRA_HORS_BORDEAUX</option>
						<option value="VERSUS">VERSUS</option>
						<option value="VINONE">VINONEGO</option>
					</optgroup>
					<optgroup label="MOULINETTES DIVERSES">
						<option value="STATEV">STATS EXCELLENCE VIN</option>
						<option value="EXTRACT_BORDEREAUX">Traitement extract bordereaux 102</option>
					</optgroup>
				</select>
			</p>
			<p>
				<input type="submit" value="VERIFIER" />
			</p>
		</form>
		</section>
	</body>
	<?php
    include('footer.html');
  ?>
</div>
</html>
