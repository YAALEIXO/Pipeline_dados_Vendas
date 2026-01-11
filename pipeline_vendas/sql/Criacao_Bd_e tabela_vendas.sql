USE dw;

GO
CREATE SCHEMA stg;
GO
CREATE TABLE stg.vendas (
    id_venda INT,
    data_venda DATE,
    produto VARCHAR(100),
    categoria VARCHAR(100),
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    canal VARCHAR(50),
    data_carga DATETIME DEFAULT GETDATE()
);
