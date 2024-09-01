<?php

      include "conn.php";

      $usuario = $_POST["usuario"];
      $senha = $_POST["senha"];

      $query = "SELECT EXISTS(SELECT * FROM users WHERE usuario = '$usuario' AND senha = '$senha') AS 'is_user_valid'";
      $registros = mysqli_query($conn, $query);

      $registro = mysqli_fetch_assoc($registros)['is_user_valid'];

      if ($registro == "0") {
            $response = FALSE;
      } else {
            $response = TRUE;
      }
      
      $objetoJSON = json_encode($response);
      echo $objetoJSON;

?>
