CREATE SCHEMA IF NOT EXISTS projeto_inovacao;

USE projeto_inovacao;

CREATE TABLE projeto_inovacao.users (
  id_users INT AUTO_INCREMENT UNIQUE NOT NULL,
  nome VARCHAR(50) NULL,
  sobrenome VARCHAR(75) NULL,
  email VARCHAR(100) NULL,
  matricula VARCHAR(8) NULL,
  usuario VARCHAR(32) NULL,
  senha VARCHAR(32) NULL,
  PRIMARY KEY (id_users)
);
