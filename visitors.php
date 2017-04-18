<?php
	echo '
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<title>Face Door Lock</title>
				<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
				<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
			</head>
			<body>
				<nav class="navbar navbar-default">
					<div class="container-fluid">
						<div class="navbar-header">
							<a class="navbar-brand" href="#">Face <kbd>Door</kbd> Lock</a>
						</div>
							<ul class="nav navbar-nav">
				      		<li><a href="index.html">Upload Keys</a></li>
				      		<li><a href="keys.php">Manage Keys</a></li>
				      		<li class="active"><a href="visitors.php">Manage Visitors</a></li>
				    	</ul>
					</div>
				</nav>
				<div class = "container">
		 ';

	$path = "./visitors";
	$handle = opendir($path);
	while (false !== ($file = readdir($handle))) {
		list($filesname, $kzm) = explode(".", $file);
		if($kzm=="gif" or $kzm=="jpg" or $kzm=="JPG" or $kzm=="png") {
			if (!is_dir('./'.$file)) {
				$array[]=$file;
				$i++;
			}
		}
	}

	for ($j = 0; $j < $i; ++$j){
	echo
		'<a href="visitordelete.php?'.$array[$j].'"><img class = "img-rounded" vspace=30 hspace=30 align=left width=320 height=240 src='.$path.'/'.$array[$j].'></a>';
	}
	echo '
		</div>
		</body></html>';
?>