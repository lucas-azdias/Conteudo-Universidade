
# EXERCÍCIOS JOINS
/*
1. Selecionar o id, nome, data de nascimento, telefone, email, valor_hora dos garçons.
*/
SELECT
	p.id AS "Id do garçom",
	p.nome AS "Nome",
    p.data_nasc AS "Data de nascimento",
    f.telefone AS "Telefone",
    f.email AS "E-mail",
    g.valor_hora AS "Valor-hora"
FROM pessoa p
NATURAL JOIN funcionario f
NATURAL JOIN garcom g;

/*
2. Selecionar o id, nome, valor, quantidade, número de registros, faturamento total e quantidade
   vendida de cada um dos produtos da base de dados.
*/
SELECT
	p.id AS "Id do Produto",
	p.nome AS "Nome",
    p.valor AS "Valor",
    p.quantidade AS "Quantidade",
    IFNULL(COUNT(r.id_produto), 0) AS "Nº de Registros",
    IFNULL(SUM(r.valor_produto * r.quantidade), 0) AS "Faturamento total",
    IFNULL(SUM(r.quantidade), 0) AS "Quantidade vendida"
FROM produto p
LEFT JOIN registro r ON p.id = r.id_produto
GROUP BY p.id, p.nome, p.valor, p.quantidade;

/*
3. Selecionar id, nome, data_criacao e o número de comandas de cada um dos clientes.
*/
SELECT
	p.id AS "Id do cliente",
    p.nome AS "Nome",
    cl.data_criacao AS "Data de criação",
    COUNT(cm.id_cliente) AS "Nº de comandas"
FROM pessoa p
NATURAL JOIN cliente cl
LEFT JOIN comanda cm ON cm.id_cliente = cl.id
GROUP BY p.id, p.nome, cl.data_criacao;

/*
4. Selecionar o id e o nome dos produtos que ainda não foram registrados.
*/
SELECT
	p.id AS "Id do produto",
    p.nome AS "Nome"
FROM produto p
LEFT JOIN registro r ON p.id = r.id_produto
WHERE r.id_produto is null;

/*
5.  Selecionar as informações dos clientes, o valor total das comandas deles e o número de
	produtos já consumidos.
*/
SELECT
	p.id AS "Id do cliente",
    p.nome AS "Nome",
    p.sexo AS "Sexo",
    p.data_nasc AS "Data de nascimento",
    p.cpf AS "CPF",
    cl.data_criacao AS "Data de criação",
    IFNULL(SUM(cm.valor_total), 0) AS "Valor total das comandas",
    IFNULL(SUM(cm.num_items), 0) AS "Nº de produtos consumidos"
FROM pessoa p
NATURAL JOIN cliente cl
LEFT JOIN comanda cm ON cm.id_cliente = cl.id
GROUP BY p.id, p.nome, p.cpf, p.sexo, p.data_nasc, cl.data_criacao;
