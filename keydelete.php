<?php
	unlink("./FaceKeys/".$_SERVER["QUERY_STRING"]);
	unlink("./Faces/".$_SERVER["QUERY_STRING"]);
	echo "<script>alert('Delete successful!'); location.href='".$_SERVER["HTTP_REFERER"]."';</script>";
?>