<?php
	$response = array();
	if ($_FILES["file"]["error"] > 0) {
		$response["upload_status"] = "Error!";
		echo json_encode($response);
	}
	else {
		if (file_exists("FaceKeys/" . $_POST["key_name"])) {
			$response["upload_status"] = "File exists!";
			echo json_encode($response);
		}
		else {
			move_uploaded_file($_FILES["file"]["tmp_name"], "FaceKeys/" . $_POST["key_name"]);
			$response["upload_status"] = "Successful!";
			echo json_encode($response);
		}
	}
?>