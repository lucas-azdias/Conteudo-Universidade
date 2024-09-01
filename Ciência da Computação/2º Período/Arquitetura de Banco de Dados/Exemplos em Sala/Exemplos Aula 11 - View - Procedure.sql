-- CREATE VIEW

CREATE OR REPLACE VIEW view_clientes_produtos
 (id_cliente, nome_cliente, data_nasc, 
	data_criacao, nome_produto, quantidade_produto)
AS 
SELECT c.id, p.nome, p.data_nasc, c.data_criacao,
	pr.nome, SUM(r.quantidade)
FROM pessoa AS p
INNER JOIN cliente AS c ON c.id = p.id
INNER JOIN comanda AS co ON co.id_cliente = c.id
INNER JOIN registro AS r ON r.id_comanda = co.id
INNER JOIN produto AS pr ON pr.id = r.id_produto
GROUP BY c.id, pr.id;

SELECT nome_produto, SUM(quantidade_produto) AS soma
FROM view_clientes_produtos
GROUP BY nome_produto
ORDER BY soma DESC;

#procedure para inserir novo cliente

DELIMITER ||
CREATE PROCEDURE inserir_cliente_restaurante(
	IN _nome VARCHAR(50),
    IN _cpf CHAR(11),
    IN _sexo CHAR(1),
    IN _data_nasc DATE
)
BEGIN
	DECLARE id_pessoa INT DEFAULT NULL;
    DECLARE id_comanda INT DEFAULT NULL;
    IF _nome IS NOT NULL AND _cpf IS NOT NULL
		AND _sexo IS NOT NULL AND _data_nasc  IS NOT NULL THEN
		# Criar um novo registro na tabela pessoa.
        INSERT INTO restaurante.pessoa 
			VALUES (NULL, _nome, _cpf, _sexo, _data_nasc);
		
        # Verificar o ID do registro na tabela pessoa.
        SELECT LAST_INSERT_ID() INTO id_pessoa;
        
        # Inserir um novo registro na tabela cliente.
        INSERT INTO restaurante.cliente VALUES (id_pessoa, NOW());
        
        # Inserir um novo registro na tabela comanda.
        INSERT INTO restaurante.comanda VALUES (NULL, NOW(), 0.0, 0, id_pessoa, NULL);
        
        SELECT LAST_INSERT_ID() INTO id_comanda;
    END IF;
	SELECT id_comanda;
END ||
DELIMITER ;

CALL inserir_cliente_restaurante("Josué Aparecido", "12341234125", "M", "2004-09-09");

-- PROCEDURES

-- 1) Criar uma Stored Procedure para selecionar o faturamento do 
-- restaurante por dia da semana em um ano específico 
-- (ano é passado como parâmetro). 


DROP PROCEDURE faturamento_dia_semana;

DELIMITER $$
CREATE PROCEDURE faturamento_dia_semana(IN ano YEAR)
BEGIN
	SELECT WEEKDAY(c.data_criacao), SUM(c.valor_total) 
    FROM restaurante.comanda AS c
    WHERE YEAR(c.data_criacao) = ano
    GROUP BY WEEKDAY(c.data_criacao)
    ORDER BY WEEKDAY(c.data_criacao);
END $$
DELIMITER ;

CALL faturamento_dia_semana("2022");

-- 2) Criar uma Stored Procedure para realizar o pagamento de 
-- um funcionário serviços gerais em um mês específico, caso 
-- ainda não tenha sido pago.

DROP PROCEDURE pagamento_mes_serv_gerais;
DELIMITER $$
CREATE PROCEDURE pagamento_mes_serv_gerais(IN mes INT(2) ZEROFILL, IN ano YEAR, IN id_func INT)
BEGIN
	DECLARE salario_f DOUBLE DEFAULT NULL;
    DECLARE id_pag INT DEFAULT NULL;
    DECLARE dia INT DEFAULT NULL;
    DECLARE data_pagamento VARCHAR(30) DEFAULT NULL;
    SET dia := 15; 
    
    SELECT id INTO id_pag
    FROM restaurante.pagamento_funcionario
    WHERE id_funcionario = id_func 
		AND MONTH(data_hora) = mes
        AND YEAR(data_hora) = ano;
    
    IF id_pag IS NULL THEN
		SELECT salario INTO salario_f
		FROM restaurante.servicos_gerais
		WHERE id = id_func;
        #SET salario_f := (SELECT salario FROM restaurante.servicos_gerais WHERE id = id_func);
        SET data_pagamento := CONCAT(ano,'-',mes,'-',dia,' ',CURTIME());
        
        INSERT INTO restaurante.pagamento_funcionario
        VALUES(NULL, salario_f, data_pagamento, id_func);
        
        SET id_pag := (SELECT LAST_INSERT_ID());
        #SELECT LAST_INSERT_ID() INTO id_pag;
        
    END IF;
    SELECT id_pag;
END $$
DELIMITER ;

CALL pagamento_mes_serv_gerais(2,'2022', 10);


-- Criar uma Stored Procedure para inserir um novo 
-- funcionário garçom no banco de dados.

DROP PROCEDURE IF EXISTS inserir_garcom_restaurante;
DELIMITER ||
CREATE PROCEDURE inserir_garcom_restaurante(
	IN _nome VARCHAR(50),
    IN _cpf CHAR(11),
    IN _sexo CHAR(1),
    IN _data_nasc DATE,
    IN _email VARCHAR(30),
    IN _telefone VARCHAR(30),
    IN _valor_hora DOUBLE
)
BEGIN
	DECLARE id_pessoa INT DEFAULT NULL;
    IF _nome IS NOT NULL AND _cpf IS NOT NULL AND _sexo IS NOT NULL 
		AND _data_nasc  IS NOT NULL AND _email IS NOT NULL 
        AND _telefone IS NOT NULL AND _valor_hora IS NOT NULL THEN
		# Criar um novo registro na tabela pessoa.
        INSERT INTO restaurante.pessoa 
			VALUES (NULL, _nome, _cpf, _sexo, _data_nasc);
		
        # Verificar o ID do registro na tabela pessoa.
        SELECT LAST_INSERT_ID() INTO id_pessoa;
        
        # Inserir um novo registro na tabela funcionario.
        INSERT INTO restaurante.funcionario VALUES (id_pessoa,_email,_telefone, now());
        
        # Inserir um novo registro na tabela garcom.
        INSERT INTO restaurante.garcom VALUES (id_pessoa, _valor_hora);

    END IF;
	SELECT p.*, f.*, g.* FROM garcom g
    INNER JOIN funcionario f ON f.id = g.id
    INNER JOIN pessoa p ON p.id = f.id
    WHERE g.id = id_pessoa;
END ||
DELIMITER ;

CALL inserir_garcom_restaurante("Alice das Maravilhas", "09090909090", 'F',
					"1988-02-03", "alice@restaurante.com", 
                    "41989898989", 100.00);
                    
# procedure pagamento_comanda
DROP PROCEDURE pagamento_comanda;
DELIMITER $$
CREATE PROCEDURE pagamento_comanda(IN id_comanda INT)
BEGIN
	DECLARE valor_comanda DOUBLE;
    DECLARE id_cliente_p DOUBLE;
    SELECT valor_total, id_cliente INTO valor_comanda, id_cliente_p 
    FROM comanda WHERE id = id_comanda AND id_pagamento IS NULL;
	IF valor_comanda IS NOT NULL AND valor_comanda > 0.0 THEN
		INSERT INTO pagamento 
        VALUES (null, valor_comanda, now(),id_cliente_p);
        UPDATE comanda SET id_pagamento = last_insert_id()
        WHERE id = id_comanda;
    END IF;
END $$
DELIMITER ;

CALL pagamento_comanda(2);

# procedure pagamento garcom

DELIMITER $$
CREATE PROCEDURE pagamento_garcom_restaurante(IN _id_garcom INT, IN comissao DOUBLE)
BEGIN
	DECLARE valor_horas_receber, valor_comissao_receber, valor_total_receber DOUBLE DEFAULT 0.0;
    
    SET valor_horas_receber := COALESCE((
									SELECT SUM(g.valor_hora * rh.numero_horas)
									FROM restaurante.garcom g
									INNER JOIN restaurante.registro_horas rh ON rh.id_garcom = g.id
									WHERE g.id = _id_garcom AND rh.id_pagamento_horas IS NULL
								), 0.0);
    SET valor_comissao_receber := COALESCE((
									SELECT SUM(valor_produto * quantidade) * comissao
									FROM restaurante.registro
									WHERE id_garcom = _id_garcom AND id_comissao IS NULL
								), 0.0);
    
    SET valor_total_receber := valor_horas_receber + valor_comissao_receber;
    
    IF valor_total_receber > 0.0 THEN
		INSERT INTO restaurante.pagamento_funcionario 
		VALUES (NULL, valor_total_receber, now(), _id_garcom);
		
        UPDATE restaurante.registro SET id_comissao = (last_insert_id())
		WHERE id_garcom = _id_garcom AND id_comissao IS NULL;
		
        UPDATE restaurante.registro_horas SET id_pagamento_horas = (last_insert_id())
		WHERE id_garcom = _id_garcom AND id_pagamento_horas IS NULL;
    END IF;
    SELECT valor_total_receber;
END $$
DELIMITER ;

CALL pagamento_garcom_restaurante(5, 0.1);
