<?php

      include "conn.php";

      $nome = $_POST["nome"];
      $sobrenome = $_POST["sobrenome"];
      $email = $_POST["email"];
      $matricula = $_POST["matricula"];
      $usuario = $_POST["usuario"];
      $senha = $_POST["senha"];

      $query = "SELECT EXISTS (SELECT * FROM users WHERE usuario = '$usuario' AND senha = '$senha') AS 'is_user_valid'";
      $registros = mysqli_query($conn, $query);

      $registro = mysqli_fetch_assoc($registros)['is_user_valid'];

      if ($registro == "0") {
            $response = TRUE;
            $query = "INSERT INTO users (id_users, nome, sobrenome, email, matricula, usuario, senha)
            VALUES (NULL, '$nome', '$sobrenome', '$email', '$matricula', '$usuario', '$senha')";
            mysqli_query($conn, $query);
      } else {
            $response = FALSE;
      }

      $objetoJSON = json_encode($response);
      echo $objetoJSON;

?>
