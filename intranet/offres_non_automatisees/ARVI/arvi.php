<?php

	echo shell_exec('python3 traitement_ARVI.py 2>&1');
	$output = shell_exec('ls -l');
	$user = shell_exec('sudo id');
	echo "<pre>$output</pre>";
	echo "<pre>$user</pre>";
	
?>