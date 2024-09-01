INSERT INTO pessoa (nome, cpf, sexo, data_nasc)  
VALUES ("Antônio dos Santos", "00000000000", "M", "2000-01-02"), ("Maria de Jesus", "10000000000", "F", "2001-04-12"), 
		("José da Silva", "20000000000", "M", "1993-04-12"),("Marcia Rocha", "30000000000", "F", "1998-05-10"),
        ("Marcos Antonio de Lima", "40000000000", "M", "1990-03-11"),("Vinicius Prado", "50000000000", "M", "1987-12-19"),
        ("Sabrina Antunes", "60000000000", "F", "1995-07-8"),("Luiz Antonio Junior", "70000000000", "M", "1992-01-12"),
        ("Valter Paes", "80000000000", "M", "1979-10-06"), ("João Arthur de Souza", "90000000000", "M", "1989-09-16"), 
        ("Janice Aparecida", "11000000000", "F", "1986-01-20");
  
INSERT INTO cliente (id, data_criacao)
VALUES (1, "2022-01-01"),(2, "2022-01-01"),(3, "2022-03-01"),(4, "2022-02-01"),(11, "2022-09-27");

INSERT INTO funcionario (id, email, telefone, data_criacao)
VALUES (5,"marcos@restaurante.com", "41999999999","2022-01-07"),
		(6,"vinicius@restaurante.com", "41988888888", "2022-01-03"),
        (7,"sabrina@restaurante.com", "41987777777", "2022-01-05"),
        (8,"luizantonio@restaurante.com", "41999999999","2022-01-07"),
		(9,"valterpaes@restaurante.com", "41988888888", "2022-01-03"),
        (10,"joaoarthur@restaurante.com", "41987777777", "2022-01-05");
        
INSERT INTO garcom (id, valor_hora)
VALUES (5,70.00),(6,73.00),(7,55.00);

INSERT INTO servicos_gerais (id, salario)
VALUES (8,1500.00),(9,1300.00),(10,2200.00);

INSERT INTO comanda (id_cliente, data_criacao,valor_total, num_items)
VALUES (1, "2022-09-01", 0.0, 0),(2, "2022-03-01", 0.0, 0), (3, "2022-06-01", 0.0, 0),(4, "2022-02-01", 0.0, 0),
        (4, "2022-02-18", 0.0, 0),(1, "2022-05-12", 0.0, 0), (1, "2022-07-11", 0.0, 0),(3, "2022-12-01", 0.0, 0),
        (3, "2022-08-21", 0.0, 0),(4, "2022-08-28", 0.0, 0),(11, "2022-09-27", 0.0, 0),(11, "2022-09-28", 0.0, 0);

INSERT INTO produto (nome, valor,quantidade)  
VALUES ("Refrigerante Laranja 1l", 7.00, 134),("Refrigerante Coca 1l", 7.00, 120),("Refrigerante Guaraná 1l", 7.00, 120),
		("Caipirinha de Limão", 18.00, 40),("Batata Frita 300g", 22.00, 70),("Alcatra acebolada 450g", 38.00, 90),
		("Cerveja 600ml", 12.00, 134),("Suco Polpa Abacaxi", 14.00, 70),("Batata Frita 500g", 39.00, 70),
        ("Executivo Frango", 28.00, 30),("Executivo Bife", 32.00, 30),("Executivo Picanha", 45.00, 30),
        ("Salada Mista", 25.00, 30),("Strogonoff de Frango", 35.00, 30),("Strogonoff de Carne", 37.00, 30),
        ("Esfirra de Frango", 4.90, 10), ("Esfirra de Carne", 4.90, 15), ("Esfirra de Queijo Provolone", 5.90, 5),
        ("Coxinha de Costela", 7.90, 20);

INSERT INTO registro (data_hora, valor_produto, quantidade, id_comanda, id_garcom,id_produto)
VALUES ("2022-09-01 23:42:00", 14.00, 3, 1, 5, 8),("2022-09-01 21:30:00", 38.00, 1, 1, 5, 6),("2022-09-01 21:30:00", 12.00, 2, 1, 5, 7),
		("2022-09-01 21:30:00", 12.00, 2, 1, 5, 13),("2022-09-01 22:00:00", 22.00, 1, 1, 6, 5),("2022-09-01 22:10:00", 22.00, 1, 1, 7, 19),
		("2022-09-01 22:10:00", 22.00, 1, 1, 7, 10),("2022-03-01 23:42:00", 7.00, 5, 2, 5, 2),("2022-03-01 21:30:00", 18.00, 2, 2, 5, 4),
        ("2022-03-01 21:30:00", 12.00, 6, 2, 5, 7),("2022-03-01 21:30:00", 25.00, 2, 2, 5, 13),("2022-03-01 22:00:00", 22.00, 1, 2, 6, 5),
        ("2022-03-01 22:10:00", 7.90, 1, 2, 7, 19),("2022-03-01 22:10:00", 28.00, 1, 2, 7, 10),("2022-06-01 23:42:00", 7.00, 1, 3, 5, 3),
		("2022-06-01 21:30:00", 7.00, 1, 3, 6, 1),("2022-06-01 21:30:00", 12.00, 2, 3, 6, 7),("2022-02-01 21:30:00", 22.00, 2, 4, 5, 4),
        ("2022-02-01 22:00:00", 14.00, 1, 4, 6, 8),("2022-02-01 22:10:00", 45.00, 1, 4, 7, 12),("2022-02-01 22:10:00", 28.00, 1, 4, 7, 10);

INSERT INTO restaurante.registro_horas (numero_horas,data_registro,id_garcom)
VALUES (4, '2022-09-01 23:59:00', 5), (2, '2022-09-01 23:59:00', 6), (3, '2022-03-01 23:59:00', 7);