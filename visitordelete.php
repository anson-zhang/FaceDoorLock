<?php
	unlink("./visitors/".$_SERVER["QUERY_STRING"]);
	echo "<script>alert('Delete successful!'); location.href='".$_SERVER["HTTP_REFERER"]."';</script>";
?>