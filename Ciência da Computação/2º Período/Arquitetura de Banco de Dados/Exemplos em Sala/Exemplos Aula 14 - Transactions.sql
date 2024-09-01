

SET autocommit = FALSE;
START TRANSACTION; #BEGIN ou BEGIN WORK
	INSERT INTO restaurante.pessoa (nome, cpf, sexo, data_nasc)
    VALUES ("Henrique Anderle", "23412345462", "M", "2004-05-12");
    SET @id_pessoa := (SELECT LAST_INSERT_ID());
    INSERT INTO restaurante.cliente VALUES (@id_pessoa, NOW());
    INSERT INTO restaurante.comanda 
    VALUES (NULL, NOW(),0.0,0,@id_pessoa,NULL);
	SELECT * FROM restaurante.comanda ORDER BY id DESC LIMIT 1;
COMMIT;


SET autocommit = FALSE;
START TRANSACTION; #BEGIN ou BEGIN WORK
	SELECT * FROM restaurante.registro;
    DELETE FROM registro;
    SELECT * FROM restaurante.registro;
ROLLBACK;
SELECT * FROM restaurante.registro;


SET autocommit = FALSE;
START TRANSACTION; #BEGIN ou BEGIN WORK
	SELECT * FROM restaurante.registro;
    DELETE FROM registro;
    SELECT * FROM restaurante.registro;
    SELECT * FROM restaurante.comanda;
    DELETE FROM comanda where id >= 1;
    SELECT * FROM restaurante.comanda;
ROLLBACK;
SELECT * FROM restaurante.registro;
SELECT * FROM restaurante.comanda;


SET autocommit = FALSE;
START TRANSACTION; #BEGIN ou BEGIN WORK
	INSERT INTO restaurante.pessoa (nome, cpf, sexo, data_nasc)
    VALUES ("Lucas Gabriel", "23416545462", "M", "2004-01-15");
    SET @id_pessoa := (SELECT LAST_INSERT_ID());
    INSERT INTO restaurante.cliente VALUES (@id_pessoa, NOW());
    INSERT INTO restaurante.comanda 
    VALUES (NULL, NOW(),0.0,0,@id_pessoa,NULL);
	
    SELECT * FROM pessoa 
    inner join cliente on cliente.id = pessoa.id
    inner join comanda on comanda.id_cliente = cliente.id;
ROLLBACK;

SELECT * FROM pessoa 
inner join cliente on cliente.id = pessoa.id
inner join comanda on comanda.id_cliente = cliente.id;

SET autocommit = FALSE;
START TRANSACTION;
	SELECT * FROM garcom g 
    JOIN funcionario f ON g.id = f.id 
    JOIN pessoa p ON p.id = f.id;
	UPDATE garcom SET valor_hora = valor_hora + 10;
	SAVEPOINT insert_garcom;
	INSERT INTO restaurante.pessoa 
    VALUES (NULL, "Mariana Fernandes", "34341234544", "F", "1991-04-05");
	SET @pessoa_id := (SELECT LAST_INSERT_ID());
	INSERT INTO restaurante.funcionario VALUES (@pessoa_id, "mariana@restaurante.com","41999090900", NOW());
	 INSERT INTO restaurante.garcom VALUES (@pessoa_id, 90.00);
	SELECT * FROM garcom g JOIN funcionario f ON g.id = f.id JOIN pessoa p ON p.id = f.id;
ROLLBACK TO SAVEPOINT insert_garcom;
COMMIT;
SELECT * FROM garcom g JOIN funcionario f ON g.id = f.id JOIN pessoa p ON p.id = f.id;


SET autocommit = FALSE;
START TRANSACTION;
	SELECT * FROM garcom g 
    JOIN funcionario f ON g.id = f.id 
    JOIN pessoa p ON p.id = f.id;
	UPDATE garcom SET valor_hora = valor_hora + 20;
	SAVEPOINT insert_garcom;
    UPDATE garcom SET valor_hora = valor_hora - 10;
ROLLBACK TO SAVEPOINT insert_garcom;
COMMIT;
SELECT * FROM garcom g JOIN funcionario f ON g.id = f.id JOIN pessoa p ON p.id = f.id;