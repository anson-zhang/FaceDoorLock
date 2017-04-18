<?php
    echo shell_exec("python ./train.py");
    echo "<script>alert('Train successful!'); location.href='".$_SERVER["HTTP_REFERER"]."';</script>";
?>