CREATE DATABASE IF NOT EXISTS transportadora;
USE transportadora;

CREATE TABLE empresa(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
	end_cep char(8) not null,
    end_complemento varchar(20),
    end_numero varchar(10) not null
);

CREATE TABLE funcao(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
	descricao varchar(100) not null
);

CREATE TABLE funcionario(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
    cpf char(11) unique not null,
	rg varchar(10) unique not null,
	data_nasc date not null,
    salario float not null,
    id_empresa integer not null,
    FOREIGN KEY (id_empresa) references empresa(id)
);

CREATE TABLE func_funcao(
	id_funcao integer not null,
    id_funcionario integer not null,
    PRIMARY KEY(id_funcao,id_funcionario),
    FOREIGN KEY (id_funcao) references funcao(id),
    FOREIGN KEY (id_funcionario) references funcionario(id)
);

CREATE TABLE motorista(
	id int not null primary key,
	cnh varchar(10) not null,
    categoria_cnh varchar(2) not null,
    FOREIGN KEY (id) references funcionario(id)
);

CREATE TABLE tipo_veiculo(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
	marca varchar(20) not null,
    modelo varchar(20) not null
);

CREATE TABLE veiculo(
	id int not null auto_increment primary key,
	placa varchar(8) not null,
    chassi varchar(15) not null,
	apolice varchar(30) not null,
	id_empresa integer not null,
    id_tipo integer not null,
    FOREIGN KEY (id_empresa) references empresa(id),
    FOREIGN KEY (id_tipo) references tipo_veiculo(id)
);


CREATE TABLE cliente(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
    cpf char(11) unique not null,
    id_empresa integer not null,
    FOREIGN KEY (id_empresa) references empresa(id)
);

CREATE TABLE contato(
	valor varchar(40) not null,
    tipo enum('telefone','email') not null,
	id_cliente int not null,
    FOREIGN KEY (id_cliente) references cliente(id)
);


CREATE TABLE transporte(
	id int not null auto_increment primary key,
    data_agendamento datetime not null,
	data_saida datetime,
    origem varchar(100) not null,
    data_chegada datetime,
    destino varchar(100) not null,
	id_motorista integer not null,
    id_veiculo integer not null,
    id_cliente integer not null,
    FOREIGN KEY (id_motorista) references motorista(id),
    FOREIGN KEY (id_veiculo) references veiculo(id),
    FOREIGN KEY (id_cliente) references cliente(id)
);

CREATE TABLE tipo_carga(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
    descricao varchar(100) not null
);

CREATE TABLE transporte_tipos(
    id_transporte integer not null,
    id_tipo integer not null,
    FOREIGN KEY (id_transporte) references transporte(id),
    FOREIGN KEY (id_tipo) references tipo_carga(id)
);

CREATE TABLE pagamento(
	id int not null auto_increment primary key,
    valor_total float not null,
    data_p datetime not null,
    id_cliente integer not null,
    id_transporte integer not null,
    FOREIGN KEY (id_transporte) references transporte(id),
    FOREIGN KEY (id_cliente) references cliente(id)
);

CREATE TABLE forma_pagamento(
	id int not null auto_increment primary key,
	nome varchar(40) not null,
    descricao varchar(100) not null
);

CREATE TABLE pagamento_formas(
    id_pagamento integer not null,
    id_forma integer not null,
    valor float not null,
    FOREIGN KEY (id_pagamento) references pagamento(id),
    FOREIGN KEY (id_forma) references forma_pagamento(id)
);

ALTER TABLE transporte add column data_agendamento DATETIME NOT NULL AFTER id;

ALTER TABLE empresa MODIFY end_complemento VARCHAR(50);

INSERT INTO empresa (nome, end_cep,end_complemento,end_numero)
VALUES ('Ovlov', '81580010', 'Ao lado do gato preto', '333');

INSERT INTO empresa (nome, end_cep,end_complemento,end_numero)
VALUES ('Bairro Alto', '81230222', 'Ao lado do gato preto II', '1724');

SELECT * FROM empresa WHERE end_numero = '333';
SELECT * FROM empresa WHERE end_complemento LIKE '%Ao%';

SELECT * FROM transporte WHERE data_agendamento < '2022-09-09 00:00:00';

SELECT * FROM transporte 
WHERE data_agendamento >= '2022-09-01 00:00:00' 
AND data_agendamento <= '2022-09-30 23:59:59';

SELECT * FROM transporte 
WHERE data_agendamento BETWEEN '2022-09-01 00:00:00' AND '2022-09-30 23:59:59';

SELECT * FROM transporte WHERE id BETWEEN 1 AND 100;

DELETE FROM empresa WHERE id = 4;
SELECT * FROM empresa order by nome asc, end_numero desc;

ALTER TABLE empresa auto_increment = 3;

INSERT INTO empresa (nome, end_cep,end_complemento,end_numero)
VALUES ('Largo muita Ordem', '81123456', 'Próximo ao desmaio do Japonês', '00123');

INSERT INTO cliente(id,nome,cpf,id_empresa)
VALUES (1,'Daniel Mendes', '11111111111', 1);

INSERT INTO cliente(nome,cpf,id_empresa)
VALUES ('Daniel Mendes', '44444444444', 3);

INSERT INTO cliente(nome,cpf,id_empresa)
VALUES ('Pagode Santos CiberSecurity', '22222222222', 1);

SELECT * FROM cliente where id_empresa = 3;
SELECT * FROM empresa;
SELECT * FROM cliente;