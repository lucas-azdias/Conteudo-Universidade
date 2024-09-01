DROP DATABASE IF EXISTS restaurante;
CREATE DATABASE restaurante;
USE restaurante;

SET sql_mode = 'ONLY_FULL_GROUP_BY';
SET SQL_SAFE_UPDATES = 0;

DROP TABLE IF EXISTS restaurante.ingrediente_produto;
DROP TABLE IF EXISTS restaurante.registro;
DROP TABLE IF EXISTS restaurante.produto;
DROP TABLE IF EXISTS restaurante.ingrediente;
DROP TABLE IF EXISTS restaurante.comanda;
DROP TABLE IF EXISTS restaurante.pagamento_forma;
DROP TABLE IF EXISTS restaurante.pagamento;
DROP TABLE IF EXISTS restaurante.forma_pagamento;
DROP TABLE IF EXISTS restaurante.registro_horas;
DROP TABLE IF EXISTS restaurante.pagamento_funcionario;
DROP TABLE IF EXISTS restaurante.servicos_gerais;
DROP TABLE IF EXISTS restaurante.garcom;
DROP TABLE IF EXISTS restaurante.funcionario;
DROP TABLE IF EXISTS restaurante.cliente;
DROP TABLE IF EXISTS restaurante.pessoa;

CREATE TABLE IF NOT EXISTS restaurante.pessoa(
	id INTEGER AUTO_INCREMENT NOT NULL,    
	nome VARCHAR(50) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    sexo CHAR(1) NOT NULL,
    data_nasc DATE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS restaurante.cliente(
	id INTEGER NOT NULL PRIMARY KEY,    
	data_criacao DATETIME NOT NULL,
    FOREIGN KEY (id) REFERENCES pessoa(id)
);

CREATE TABLE IF NOT EXISTS restaurante.funcionario(
	id INTEGER NOT NULL PRIMARY KEY,
    email VARCHAR(40) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
	data_criacao DATETIME NOT NULL,
    FOREIGN KEY (id) REFERENCES pessoa(id)
);

CREATE TABLE IF NOT EXISTS restaurante.garcom(
	id INTEGER NOT NULL PRIMARY KEY,    
	valor_hora DOUBLE NOT NULL,
    FOREIGN KEY (id) REFERENCES funcionario(id)
);

CREATE TABLE IF NOT EXISTS restaurante.servicos_gerais(
	id INTEGER NOT NULL PRIMARY KEY,    
	salario DOUBLE NOT NULL,
    FOREIGN KEY (id) REFERENCES funcionario(id)
);

CREATE TABLE IF NOT EXISTS restaurante.pagamento_funcionario(
	id INTEGER AUTO_INCREMENT NOT NULL,
    valor double NOT NULL,
    data_hora DATETIME NOT NULL,
    id_funcionario INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id)
);

CREATE TABLE IF NOT EXISTS restaurante.registro_horas(
    numero_horas double NOT NULL,
    data_registro DATETIME NOT NULL,
    id_garcom INTEGER NOT NULL,
    id_pagamento_horas INTEGER,
    FOREIGN KEY (id_garcom) REFERENCES garcom(id),
    FOREIGN KEY (id_pagamento_horas) REFERENCES pagamento_funcionario(id)
);

CREATE TABLE IF NOT EXISTS restaurante.forma_pagamento(
	id INTEGER NOT NULL PRIMARY KEY, 
    nome VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS restaurante.pagamento(
	id INTEGER AUTO_INCREMENT NOT NULL,
    valor double NOT NULL,
    data_hora DATETIME NOT NULL,
    id_cliente INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

CREATE TABLE IF NOT EXISTS restaurante.pagamento_forma(
	id_forma_pagamento INTEGER NOT NULL,
    id_pagamento INTEGER NOT NULL,
    valor double NOT NULL,
    parcelas SMALLINT(2),
    PRIMARY KEY(id_pagamento, id_forma_pagamento),
    FOREIGN KEY (id_forma_pagamento) REFERENCES forma_pagamento(id),
    FOREIGN KEY (id_pagamento) REFERENCES pagamento(id)
);

CREATE TABLE IF NOT EXISTS restaurante.comanda(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,   
	data_criacao DATETIME NOT NULL,
    valor_total DOUBLE,
    num_items INT,
	id_cliente INTEGER NOT NULL,
    id_pagamento INTEGER,
	FOREIGN KEY  (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY  (id_pagamento) REFERENCES pagamento(id)
);

CREATE TABLE IF NOT EXISTS restaurante.produto(
	id INTEGER AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    valor DOUBLE NOT NULL,
    quantidade integer NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS restaurante.registro(
	data_hora DATETIME NOT NULL,
    valor_produto DOUBLE NOT NULL DEFAULT 0.0,
    quantidade integer NOT NULL,
    id_comanda INTEGER NOT NULL,
    id_garcom INTEGER NOT NULL,
    id_produto INT NOT NULL,
    id_comissao INTEGER,
    PRIMARY KEY(id_comanda, id_garcom, id_produto),
    FOREIGN KEY (id_produto) REFERENCES produto(id),
    FOREIGN KEY (id_comanda) REFERENCES comanda(id),
    FOREIGN KEY (id_garcom) REFERENCES garcom(id),
    FOREIGN KEY  (id_comissao) REFERENCES pagamento_funcionario(id)
);

CREATE TABLE IF NOT EXISTS ingrediente (
	id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(40) NOT null,
    quantidade FLOAT NOT null,
    unidade CHAR(1) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS produto_ingredientes (
	id_produto INT NOT NULL,
    id_ingrediente INT NOT NULL,
    quantidade FLOAT,
    PRIMARY KEY(id_produto, id_ingrediente),
    FOREIGN KEY (id_produto) REFERENCES produto(id),
    FOREIGN KEY (id_ingrediente) REFERENCES ingrediente(id)
);