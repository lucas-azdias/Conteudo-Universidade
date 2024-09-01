SET SQL_SAFE_UPDATES = 0;


# Atividades Operadores
/*
1. Selecionar as pessoas que nasceram depois de "1990-01-01",  ordenadas por nome em ordem alfabética.
*/
SELECT * FROM pessoa WHERE data_nasc > "1990-01-01" ORDER BY nome ASC;

/*
2. Selecionar as comandas cujo valor seja maior do que R$ 100,00, ordenadas do maior para o menor valor.
*/
SELECT * FROM comanda WHERE valor_total > 100 ORDER BY valor_total DESC;

/*
3. Selecionar as comandas registradas entre "2022-02-01" e "2022-09-02", ordenadas por data de criação.
*/
SELECT * FROM comanda WHERE data_criacao BETWEEN "2022-02-01" AND "2022-09-02" ORDER BY data_criacao;

/*
4. Atualizar o valor do produto 10, aumentando 10%.
*/
UPDATE produto SET
	valor = valor * 1.1
    WHERE id = 10;

/*
5. Atualizar o valor do produto 7, aumentando R$ 2,30.
*/
UPDATE produto SET
	valor = valor + 2.3
    WHERE id = 7;

/*
6. Atualizar o valor dos produtos com valor maior que 40 reais, dando um desconto de 12%.
*/
UPDATE produto SET
	valor = valor * (1 - 0.12)
    WHERE valor > 40;

/*
7. Inserir o pagamento referente ao valor da comanda 1;
*/
INSERT INTO pagamento(valor, data_hora, id_cliente) VALUES (
	(SELECT SUM(valor_produto * quantidade) FROM registro WHERE id_comanda = 1),
    CURRENT_TIMESTAMP(),
    (SELECT id_cliente FROM comanda WHERE id = 1));

/*
8. Selecionar os registros que não estão ligados a nenhum pagamento de comissão.
*/
SELECT * FROM registro WHERE id_comissao IS NULL;

/*
9. Selecionar todas as pessoas cuja antepenúltima letra do nome é igual a "T".
*/
SELECT * FROM pessoa WHERE nome LIKE "%T__";

/*
10. Selecionar as pessoas que possuem as vogais "a", "e" e "o" no nome ou que tenham as vogais "i" e "u".
*/
SELECT * FROM pessoa WHERE (nome LIKE "%A%" AND nome LIKE "%E%" AND nome LIKE "%O%") OR (nome LIKE "%I%" AND nome LIKE "%U%");


# Atividades Funções de Agregação
/*
1. Consultar valor máximo, mínimo e médio dos produtos cadastrados (Nomear os campos como Máximo, Mínimo e Média).
*/
SELECT MAX(valor) AS "Máximo", MIN(valor) AS "Mínimo", AVG(valor) AS "Média" FROM produto;

/*
2. Consultar número de registros de cada um dos garçons.
*/
SELECT id_garcom AS "Garçom", COUNT(*) AS "Nº de registros" FROM registro GROUP BY id_garcom;

/*
3. Os valor total dos registros de cada garçom que efetuou mais do que 3 registros.
*/
SELECT id_garcom AS "Garçom", SUM(valor_produto * quantidade) AS "Total registrado" FROM registro GROUP BY id_garcom HAVING COUNT(id_garcom) >= 3;

/*
4. Consultar o valor total e o número de comandas já registradas.
*/
SELECT COUNT(*) AS "Nº de comandas", SUM(valor_total) AS "Valor total" FROM comanda;

/*
5. Consultar as comandas que não possuem registro de produtos.
*/
SELECT COUNT(*) AS "Nº de comandas sem registros" FROM comanda WHERE NOT id IN (
	SELECT id_comanda FROM registro
);

/*
6. Consultar o id dos garçons que registraram mais do que R$ 120,00.
*/
SELECT id_garcom AS "Garçom com mais de R$120 registrados" FROM registro GROUP BY id_garcom HAVING SUM(valor_produto * quantidade) > 120;

/*
7. Consultar o valor total gasto e o número de comandas de cada um dos clientes.
*/
SELECT id_cliente AS "ID do Cliente", COUNT(id) AS "Nº de comandas", SUM(valor_total) AS "Valor total gasto" FROM comanda GROUP BY id_cliente;

/*
8. Consultar os valores distintos de produtos no banco de dados.
*/
SELECT DISTINCT valor FROM produto;

/*
9. Atualizar a quantidade disponível de cada um dos produtos diminuindo a quantidade dos produtos registrados.
*/
UPDATE produto SET
	quantidade = quantidade - (SELECT SUM(quantidade) FROM registro WHERE produto.id = id_produto GROUP BY id_produto)
    WHERE id IN (SELECT id_produto FROM registro);

/*
10. Selecionar o valor médio das comandas e o valor médio dos produtos consumidos.
*/
SELECT AVG(valor_total) AS "Média do valor das comandas" FROM comanda;
SELECT AVG(valor_produto) AS "Média do valor dos produtos nas comandas" FROM registro GROUP BY id_comanda;
