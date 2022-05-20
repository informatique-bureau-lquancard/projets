<?php
session_start();
$filename = basename("sortie_").$_SESSION['profil'].".csv";
echo $filename;
?>