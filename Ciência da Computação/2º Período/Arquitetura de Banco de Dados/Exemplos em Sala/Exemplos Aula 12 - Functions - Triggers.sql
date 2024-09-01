# FUNCTIONS

DROP FUNCTION IF EXISTS dia_da_semana;

DELIMITER //
CREATE FUNCTION dia_da_semana(_data DATE)
RETURNS VARCHAR(30) DETERMINISTIC
BEGIN
	DECLARE dia_semana VARCHAR(30) DEFAULT NULL;
    
    CASE  DAYOFWEEK(_data)
		WHEN 1 THEN 
			SET dia_semana := "Domingo";
		WHEN 2 THEN
			SET dia_semana := "Segunda";
		WHEN 3 THEN
			SET dia_semana := "Terça";
		WHEN 4 THEN
			SET dia_semana := "Quarta";
		WHEN 5 THEN
			SET dia_semana := "Quinta";
		WHEN 6 THEN
			SET dia_semana := "Sexta";
		ELSE
			SET dia_semana := "Sábado";
	END CASE;
    RETURN dia_semana;
END //
DELIMITER ;
SELECT dia_da_semana_texto("2001-12-18");

DROP FUNCTION horas_garcons_restaurante;

DELIMITER $$
CREATE FUNCTION horas_garcons_restaurante(id_garcom INT)
RETURNS DOUBLE DETERMINISTIC
BEGIN
	DECLARE valor_horas DOUBLE DEFAULT 0.0;
    SELECT SUM(rh.numero_horas * g.valor_hora) INTO @valor_horas
			FROM garcom g
            INNER JOIN registro_horas rh ON rh.id_garcom = g.id
            WHERE g.id = id_garcom AND rh.id_pagamento_horas IS NULL;
	RETURN @valor_horas;
END $$
DELIMITER ;

DROP FUNCTION comissao_garcons_restaurante;

DELIMITER $$
CREATE FUNCTION comissao_garcons_restaurante(id_garcom INT, _comissao DOUBLE)
RETURNS DOUBLE DETERMINISTIC
BEGIN
	DECLARE valor_comissao DOUBLE DEFAULT 0.0;
    SELECT SUM(r.valor_produto * r.quantidade)*_comissao INTO @valor_comissao
			FROM garcom g
            INNER JOIN registro r ON r.id_garcom = g.id
            WHERE g.id = id_garcom AND r.id_comissao IS NULL;
	RETURN @valor_comissao;
END $$
DELIMITER ;

# Atualizar procedure pagamento_garcom_restaurante com as funções criadas

DROP PROCEDURE IF EXISTS pagamento_garcom_restaurante;

DELIMITER $$
CREATE PROCEDURE pagamento_garcom_restaurante(IN _id_garcom INT, IN _comissao DOUBLE)
BEGIN
	DECLARE valor_horas DOUBLE DEFAULT 0.0;
    DECLARE valor_comissao DOUBLE DEFAULT 0.0;
    DECLARE id_pagamento INT DEFAULT NULL;
    DECLARE valor_pagamento DOUBLE DEFAULT 0.0;
    
    IF _id_garcom IS NOT NULL THEN
		SELECT horas_garcons_restaurante(_id_garcom) INTO @valor_horas;
        SELECT comissao_garcons_restaurante(_id_garcom, _comissao) INTO valor_comissao;
        SET @valor_pagamento := (COALESCE(@valor_horas, 0.0) + COALESCE(@valor_comissao, 0.0));
        IF @valor_pagamento > 0.0 THEN
			INSERT INTO pagamento_funcionario VALUES (NULL, @valor_pagamento, NOW(), _id_garcom);
        
			SELECT LAST_INSERT_ID() INTO @id_pagamento;
			
			UPDATE registro_horas SET id_pagamento_horas = @id_pagamento
				WHERE id_garcom = _id_garcom AND id_pagamento_horas IS NULL;
			
			UPDATE registro SET id_comissao = @id_pagamento
				WHERE id_garcom = _id_garcom AND id_comissao IS NULL;
        END IF;
    END IF;
    SELECT CONCAT("O valor pago foi: ", @valor_pagamento) AS "RETORNO";
END $$
DELIMITER ;

CALL pagamento_garcom_restaurante(5, 0.10);



# TRIGGERS

DELIMITER $$
CREATE TRIGGER after_insert_registro
AFTER INSERT ON restaurante.registro 
FOR EACH ROW 
BEGIN
	UPDATE restaurante.comanda 
		SET valor_total = valor_total + (NEW.valor_produto * NEW.quantidade),
			num_items = num_items + NEW.quantidade
	WHERE id = NEW.id_comanda;
    
    UPDATE restaurante.produto
		SET quantidade = quantidade - NEW.quantidade
	WHERE id = NEW.id_produto;
END $$
DELIMITER ;

INSERT INTO registro(data_hora, valor_produto, quantidade, id_comanda, id_garcom, id_produto)
VALUES ("2022-09-01 23:42:00", 7.00, 10, 1, 7, 1);


DELIMITER $$
CREATE TRIGGER before_insert_registro
BEFORE INSERT ON restaurante.registro 
FOR EACH ROW 
BEGIN
	DECLARE estoque INT DEFAULT 0;
    SELECT quantidade INTO estoque FROM restaurante.produto 
	WHERE id = NEW.id_produto;
    IF estoque < NEW.quantidade THEN
		SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Não Existe estoque do produto selecionado!!'; 
    END IF;
END $$
DELIMITER ;


INSERT INTO registro(data_hora, valor_produto, quantidade, id_comanda, id_garcom, id_produto)
VALUES ("2022-09-01 23:42:00", 5.90, 6, 1, 7, 18);

DELIMITER $$
CREATE TRIGGER after_delete_registro
AFTER DELETE ON restaurante.registro 
FOR EACH ROW 
BEGIN
	UPDATE restaurante.comanda 
		SET valor_total = valor_total - (OLD.valor_produto * OLD.quantidade),
			num_items = num_items - OLD.quantidade
	WHERE id = OLD.id_comanda;
    
    UPDATE restaurante.produto
		SET quantidade = quantidade + OLD.quantidade
	WHERE id = OLD.id_produto;
END $$
DELIMITER ;

DELETE FROM restaurante.registro WHERE id_comanda = 1 AND id_garcom = 7 AND id_produto = 1;

DELIMITER $$
CREATE TRIGGER after_update_registro
AFTER UPDATE ON restaurante.registro 
FOR EACH ROW 
BEGIN
	DECLARE quant_diff DOUBLE DEFAULT 0.0;
    SET quant_diff := (NEW.quantidade - OLD.quantidade);
	IF quant_diff <> 0 THEN
		UPDATE restaurante.comanda 
			SET valor_total = valor_total + (OLD.valor_produto * quant_diff),
				num_items = num_items + quant_diff
		WHERE id = OLD.id_comanda;
		
		UPDATE restaurante.produto
			SET quantidade = quantidade - quant_diff
		WHERE id = OLD.id_produto;
	END IF;
END $$
DELIMITER ;

UPDATE registro SET quantidade = 10 
WHERE id_comanda = 1 AND id_garcom = 7 AND id_produto = 19;


