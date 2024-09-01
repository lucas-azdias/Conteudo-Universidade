SELECT p.cpf as "CPF do Cliente", 
	c.data_criacao AS "Data de Criação do Cliente" 
FROM pessoa AS p, cliente AS c
WHERE p.id = c.id;

SELECT *
FROM pessoa AS p, cliente AS c
WHERE p.id = c.id;

SELECT * 
FROM pessoa NATURAL JOIN cliente;

SELECT p.id AS "ID do Cliente", p.nome AS "Nome do Cliente", 
	pr.id AS "ID do Produto", pr.nome AS "Nome do Produto", pr.valor,
    COUNT(*), SUM(r.quantidade)
FROM pessoa AS p
INNER JOIN cliente AS c ON c.id = p.id
INNER JOIN comanda AS co ON co.id_cliente = c.id
INNER JOIN registro AS r ON r.id_comanda = co.id
INNER JOIN produto AS pr ON pr.id = r.id_produto
GROUP BY p.id, pr.id
ORDER BY c.id;


SELECT pessoa.*, cliente.*, comanda.* 
FROM pessoa
INNER JOIN cliente ON cliente.id = pessoa.id
INNER JOIN comanda ON comanda.id_cliente = cliente.id;


SELECT p.id AS "ID do Cliente", p.nome AS "Nome do Cliente",
	pr.nome AS "Nome do Produto", g.id AS "ID Garçom", 
    pf.nome AS "Nome Garçom", f.telefone AS "Telefone Garçom",
    g.valor_hora,
    COUNT(*), SUM(r.quantidade)
FROM pessoa AS p
INNER JOIN cliente AS c ON c.id = p.id
INNER JOIN comanda AS co ON co.id_cliente = c.id
INNER JOIN registro AS r ON r.id_comanda = co.id
INNER JOIN produto AS pr ON pr.id = r.id_produto
INNER JOIN garcom AS g ON g.id = r.id_garcom
INNER JOIN funcionario AS f ON f.id = g.id
INNER JOIN pessoa AS pf ON pf.id = f.id
WHERE g.id = 5 AND co.data_criacao >= "2022-07-01"
GROUP BY p.id, pr.id, g.id
HAVING SUM(r.quantidade) >= 2 
ORDER BY c.id;


SELECT cliente.*, comanda.*, registro.*
FROM cliente
LEFT JOIN comanda ON comanda.id_cliente = cliente.id
LEFT JOIN registro ON registro.id_comanda = comanda.id
ORDER BY cliente.id;


SELECT pagamento_funcionario.*, registro.* 
FROM pagamento_funcionario
RIGHT JOIN registro ON registro.id_comissao = pagamento_funcionario.id;

SELECT pagamento_funcionario.*, registro.* 
FROM pagamento_funcionario
LEFT JOIN registro ON registro.id_comissao = pagamento_funcionario.id;

SELECT pagamento_funcionario.*, registro.* 
FROM pagamento_funcionario
INNER JOIN registro ON registro.id_comissao = pagamento_funcionario.id;

SELECT pagamento_funcionario.*, registro.* 
FROM pagamento_funcionario, registro
WHERE registro.id_comissao = pagamento_funcionario.id;

(SELECT pagamento_funcionario.*, registro.* 
FROM pagamento_funcionario
LEFT JOIN registro ON registro.id_comissao = pagamento_funcionario.id)
UNION
(SELECT pagamento_funcionario.*, registro.* 
FROM pagamento_funcionario
RIGHT JOIN registro ON registro.id_comissao = pagamento_funcionario.id);

SET @id_g := 5;
SET @comissao := 0.10;

SET @valor_comissao := (SELECT SUM(r.valor_produto*r.quantidade)*@comissao FROM registro AS r
WHERE id_garcom = @id_g AND id_comissao IS NULL);

INSERT INTO pagamento_funcionario VALUES (NULL, @valor_comissao, NOW(), @id_g);

#SET @id_pag := (SELECT MAX(id) FROM pagamento_funcionario WHERE id_funcionario = @id_g);
SET @id_pag := (SELECT LAST_INSERT_ID());

SELECT @id_pag;

UPDATE registro SET id_comissao = @id_pag 
WHERE id_garcom = @id_g AND id_comissao IS NULL;



SELECT 195.9*0.07;

SELECT r.id_garcom,
	SUM(r.valor_produto*r.quantidade),
	CASE WHEN SUM(r.valor_produto*r.quantidade) < 150.00
			THEN SUM(r.valor_produto*r.quantidade)*0.05
		WHEN SUM(r.valor_produto*r.quantidade) >= 150.00 
			AND SUM(r.valor_produto*r.quantidade) < 300.00 
			THEN SUM(r.valor_produto*r.quantidade) * 0.07
		ELSE SUM(r.valor_produto*r.quantidade)*0.1
	END AS "Comissão"
FROM registro AS r
GROUP BY r.id_garcom;


SELECT COALESCE(null, null, null, null, "teste", "teste", 123);

UPDATE comanda SET 	valor_total = COALESCE( (SELECT SUM(quantidade * valor_produto) 
										FROM restaurante.registro WHERE id_comanda = comanda.id) , 0.0),
					num_items = COALESCE( (SELECT SUM(quantidade) 
											FROM restaurante.registro WHERE id_comanda = comanda.id), 0);

SELECT dayofweek(c.data_criacao), 
	CASE WHEN dayofweek(c.data_criacao) = 1 THEN "Domingo"
		WHEN dayofweek(c.data_criacao) = 2 THEN "Segunda"
        WHEN dayofweek(c.data_criacao) = 3 THEN "Terça"
        WHEN dayofweek(c.data_criacao) = 4 THEN "Quarta"
        WHEN dayofweek(c.data_criacao) = 5 THEN "Quinta"
        WHEN dayofweek(c.data_criacao) = 6 THEN "Sexta"
        ELSE "Sábado" END AS dia_semana,
		sum(c.valor_total)
from comanda AS c
GROUP BY dayofweek(c.data_criacao)
ORDER BY dayofweek(c.data_criacao); 

SELECT dayofweek(c.data_criacao), 
	CASE weekday(c.data_criacao) 
		WHEN 6 THEN "Domingo"
		WHEN 0 THEN "Segunda"
        WHEN 1 THEN "Terça"
        WHEN 2 THEN "Quarta"
        WHEN 3 THEN "Quinta"
        WHEN 4 THEN "Sexta"
		ELSE "Sábado" 
	END AS dia_semana,
	SUM(c.valor_total)
from comanda AS c
GROUP BY dayofweek(c.data_criacao)
ORDER BY dayofweek(c.data_criacao); 



SELECT month(c.data_criacao),
	CASE month(c.data_criacao) 
		WHEN 1 THEN "Janeiro"
		WHEN 2 THEN "Fevereiro"
        WHEN 3 THEN "Março"
        WHEN 4 THEN "Abril"
        WHEN 5 THEN "Maio"
        WHEN 6 THEN "Junho"
        WHEN 7 THEN "Julho"
		WHEN 8 THEN "Agosto"
        WHEN 9 THEN "Setembro"
        WHEN 10 THEN "Outubro"
        WHEN 11 THEN "Novembro"
		ELSE "Dezembro" 
	END AS dia_semana,
	sum(c.valor_total)
from comanda AS c
GROUP BY month(c.data_criacao)
ORDER BY month(c.data_criacao); 



SELECT DAYOFYEAR('2022-10-19');
SELECT MONTH('2022-10-19');

SELECT NOW();
SELECT CURDATE();
SELECT CURTIME();


SELECT DAYNAME('2022-10-05');
SELECT MONTHNAME('2022-10-05');


SELECT DATE_ADD(CURDATE(), INTERVAL 3 YEAR);
SELECT DATE_ADD(CURDATE(), INTERVAL 3 MONTH);
SELECT DATE_ADD(CURDATE(), INTERVAL 3 DAY);
SELECT DATE_ADD(NOW(), INTERVAL 3 HOUR);
SELECT DATE_ADD(NOW(), INTERVAL 3 MINUTE);
SELECT DATE_ADD(NOW(), INTERVAL 3 SECOND);

SELECT DATE_SUB(CURDATE(), INTERVAL 3 YEAR);
SELECT DATE_SUB(CURDATE(), INTERVAL 3 MONTH);
SELECT DATE_SUB(CURDATE(), INTERVAL 3 DAY);
SELECT DATE_SUB(NOW(), INTERVAL 3 HOUR);
SELECT DATE_SUB(NOW(), INTERVAL 3 MINUTE);
SELECT DATE_SUB(NOW(), INTERVAL 3 SECOND);

SELECT 
	p.nome,
	YEAR(FROM_DAYS(TO_DAYS(CURDATE()) - TO_DAYS(p.data_nasc)))
FROM pessoa p;

SELECT 
	TIMESTAMPDIFF(YEAR, p.data_nasc, NOW()) AS idade
FROM pessoa AS p
ORDER BY idade;




CREATE OR REPLACE VIEW view_produtos_clientes (id_cliente, nome_cliente, data_nasc, cpf, sexo, data_criacao,
									nome_produto, sum_quantidade)
AS
SELECT c.id, p.nome, p.data_nasc, p.cpf, p.sexo, c.data_criacao, pr.nome, SUM(r.quantidade)
FROM pessoa AS p
INNER JOIN cliente c ON c.id = p.id
INNER JOIN comanda co ON co.id = c.id
INNER JOIN registro r ON r.id_comanda = co.id
INNER JOIN produto pr ON pr.id = r.id_produto
GROUP BY c.id, p.nome, p.data_nasc, p.cpf, p.sexo, pr.nome;

SELECT * FROM view_produtos_clientes;

SELECT nome_produto, SUM(sum_quantidade) 
FROM view_produtos_clientes
GROUP BY nome_produto;

SELECT nome_cliente, SUM(sum_quantidade) 
FROM view_produtos_clientes
GROUP BY nome_cliente;

















