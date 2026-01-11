# Pipeline de Vendas com SQL Server

Este projeto é um pipeline de dados completo, desenvolvido em Python, que realiza a ingestão, validação e persistência de dados de vendas em um banco SQL Server. 

O pipeline segue boas práticas de Engenharia de Dados, incluindo:
- Separação de responsabilidades (ingestão, processamento, carregamento)
- Pipeline reproducível e modular
- Persistência em camada de **staging**, simulando um ambiente de dados real

## Arquitetura do Pipeline

CSV (raw)
→ Python (Pandas)
→ SQL Server (Schema: staging)

## Tecnologias utilizadas
- Python (pandas)
- SQL Server
- SQLAlchemy / pyodbc
- Git / GitHub

## Objetivo
Este projeto serve como exemplo de pipeline de dados júnior, ideal para portfólio e para demonstrar competências em Engenharia de Dados, incluindo ingestão, validação e persistência em banco relacional.
