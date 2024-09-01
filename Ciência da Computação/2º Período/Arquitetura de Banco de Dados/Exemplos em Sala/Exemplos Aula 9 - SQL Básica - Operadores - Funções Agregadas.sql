/*
Atividades SQL BÁSICA

1. Inserir um registro de produto nas comandas 5, 6, 10 e 12.

	a) Selecionar e escolher um produto da tabela produtos  
    (verifique o valor do produto para ser inserido no registro),

	b) Escolha um garçom para vincular ao registro.
*/

INSERT INTO restaurante.registro 
(data_hora, valor_produto, quantidade, id_comanda, id_garcom, id_produto, id_comissao)
VALUES (now(), 18, 2, 5, 7, 4, null), 
		(now(), 45, 1, 6, 5, 12, null), 
        (now(), 7, 1, 10, 7, 1, null), 
        (now(), 7, 3, 12, 6, 2, null);

INSERT INTO restaurante.registro 
	VALUES (now(), 18, 2, 5, 7, 4, null), 
			(now(), 45, 1, 6, 5, 12, null), 
            (now(), 7, 1, 10, 7, 1, null), 
            (now(), 7, 3, 12, 6, 2, null);

/*
2. Atualizar o valor do produto 8 para R$ 12,00.
*/

update restaurante.produto set valor = 12.00 where id = 8;

/*
3. Atualizar a quantidade (mudar para 3) do produto 2, registrado na comanda 2, 
	pelo garçom com 5.
*/

update restaurante.registro set quantidade = 3 
where id_produto = 2 and id_comanda = 2 and id_garcom = 5;

/*
4. Excluir o registro do produto 19 na comanda  2.
*/

DELETE FROM restaurante.registro 
WHERE id_produto = 19 AND id_comanda = 2;

/*
5. Criar a tabela ingredientes, a qual está ligada ao produto por meio de 
uma relação muitos para muitos.
*/

CREATE TABLE restaurante.ingrediente(
	id integer not null auto_increment primary key,
    nome varchar(50) not null,
    quantidade integer not null
);

create table restaurante.ingrediente_produto(
	id_produto integer not null,
    id_ingrediente integer not null,
    primary key (id_produto,id_ingrediente),
    foreign key (id_produto) references produto(id),
    foreign key (id_ingrediente) references ingrediente(id)
);

/*
6. Inserir os ingredientes necessários para preparação do produto 4 
("Caipirinha de Limão") e vincular esses ingredientes.
*/
INSERT INTO ingrediente(nome,quantidade) 
VALUES("Limao", 50), ("Alcool", 10), ("Acucar", 20);

INSERT INTO ingrediente_produto VALUES(4,1),(4,2),(4,3);

/*
Atividades Operadores

1. Selecionar as pessoas que nasceram depois de "1990-01-01",  ordenadas por 
nome em ordem alfabética.
*/

select * from pessoa 
where data_nasc > '1990-01-01' order by nome;

/*
2. Selecionar as comandas cujo valor seja maior do que R$ 100,00, 
ordenadas do maior para o menor valor.
*/

Select * from restaurante.comanda 
where valor_total > 100 order by valor_total desc;

/*
3. Selecionar as comandas registradas entre "2022-02-01" e "2022-09-02", 
ordenadas por data de criação.
*/

select*from pessoa where data_criacao between `2022-02-01`and `2022-09-02`order by data_criacao;

/*
4. Atualizar o valor do produto 10, aumentando 10%.	
*/

	    UPDATE restaurante.produto SET valor = valor * 1.1 WHERE id = 10;

/*
5. Atualizar o valor do produto 7, aumentando R$ 2,30.
*/
	UPDATE restaurante.produto SET valor = valor + 2.3 WHERE id = 7;
/*
6. Atualizar o valor dos produtos com valor maior que 40 reais, 
dando um desconto de 12%.
*/
	UPDATE produto SET valor = valor - (valor * 0.12) where valor > 40;
/*
7. Inserir o pagamento referente ao valor da comanda 1;
*/

insert into pagamento(valor, data_hora, id_cliente) 
values ((select valor_total from comanda where id = 1), now(), 1);

update comanda set id_pagamento = 1 where id = 1;

update comanda set 
id_pagamento = (select max(id) from pagamento) 
where id = 1;

/*
8. Selecionar os registros que não estão ligados a nenhum 
pagamento de comissão.
*/

SELECT * FROM registro WHERE id_comissao IS NULL;

/*
9. Selecionar todas as pessoas cuja antepenúltima letra 
	do nome é igual a "T".
*/

SELECT*FROM restaurante.pessoa WHERE nome LIKE "%t__";

/*
10. Selecionar as pessoas que possuem as vogais "a", "e" e "o" 
	no nome ou que tenham as vogais "i" e "u".
*/

select * from restaurante.pessoa 
where (nome like '%A%' and nome like '%E%' and nome like '%O%')
or (nome like '%I%' and nome like '%U%');

/*
Atividades Funções de Agregação

1. Consultar valor máximo, mínimo e médio dos produtos cadastrados 
(Nomear os campos como Máximo, Mínimo e Média).
*/

select 
	max(valor) as "Máximo", 
    min(valor) as "Mínimo", 
    round(avg(valor),2) as "Média" 
from produto;


/*
2. Consultar número de registros de cada um dos garçons.
*/

select id_garcom, count(id_garcom) 
from registro 
group by id_garcom;

select id_garcom, count(*) 
from registro 
group by id_garcom;


/*
3. Os valor total dos registros de cada garçom que efetuou 
	mais do que 3 registros.
*/
select id_garcom, sum(quantidade * valor_produto)
FROM registro
GROUP BY id_garcom
HAVING COUNT(*) > 3;


/*
4. Consultar o valor total e o número de comandas já registradas.
*/

select sum(valor_total), count(id) 
from restaurante.comanda;

select sum(valor_total), count(*) 
from restaurante.comanda;

/*
5. Consultar as comandas que não possuem registro de produtos.
*/

SELECT * FROM comanda where num_items = 0 OR num_items IS NULL;
SELECT * FROM comanda where valor_total = 0.0 OR valor_total IS NULL;

SELECT * FROM comanda 
WHERE id NOT IN (SELECT id_comanda FROM registro);

/*
6. Consultar o id dos garçons que registraram mais do que R$ 120,00.
*/

select id_garcom, SUM(valor_produto * quantidade) as soma 
from registro 
group by id_garcom 
having soma > 20.00;

/*
7. Consultar o valor total gasto e o número de comandas de cada 
um dos clientes.
*/

/*
8. Consultar os valores distintos de produtos no banco de dados.
*/

SELECT valor, count(*) from produto group by valor;
SELECT distinct(valor)from produto order by valor;

/*
9. Atualizar a quantidade disponível de cada um dos produtos 
	diminuindo a quantidade dos produtos registrados.
*/

UPDATE produto 
SET quantidade = quantidade - CASE WHEN (
									SELECT SUM(quantidade) FROM registro
									WHERE id_produto = produto.id
								) IS NULL THEN 0.0
								ELSE (
									SELECT SUM(quantidade) FROM registro
									WHERE id_produto = produto.id
								) END;
/*
10. Selecionar o valor médio das comandas e 
	o valor médio dos produtos consumidos.
*/
SELECT AVG(valor_total), 
		SUM(valor_total)/SUM(num_items) 
FROM comanda;

SELECT SUM(valor_total)/COUNT(*), 
		SUM(valor_total)/SUM(num_items) 
FROM comanda;

SELECT id_comanda, 
	SUM(valor_produto * quantidade), 
    SUM(valor_produto * quantidade)/SUM(quantidade)
from registro
group by id_comanda;

