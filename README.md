# Projeto Big Data com Docker, Hadoop e Spark

## Objetivo

Este projeto tem como objetivo desenvolver um ambiente de Big Data local utilizando Docker, capaz de armazenar e processar dados em diferentes formatos (CSV, JSON e Parquet). Também foram realizados testes de desempenho e resiliência utilizando Apache Spark e Hadoop HDFS.

## Tecnologias Utilizadas

- Docker
- Docker Compose
- Apache Hadoop 3.2.1
- Apache Spark 4.0.3
- Python
- Pandas
- PyArrow
- HDFS

## Arquitetura

O ambiente foi composto por:

- 1 NameNode
- 1 DataNode
- 1 ResourceManager
- 1 NodeManager
- 1 Spark Master
- 2 Spark Workers

## Estrutura do Projeto

```
docker-hadoop/
│
├── dados/
│   ├── vendas.csv
│   ├── vendas.json
│   └── vendas.parquet
│
├── scripts/
│   ├── gerar_dados.py
│   └── processar_spark.py
│
├── docker-compose.yml
├── hadoop.env
└── README.md
```

## Execução

Subir os containers:

```bash
docker compose up -d
```

Executar o processamento:

```bash
docker exec spark-master /opt/spark/bin/spark-submit \
--master spark://spark-master:7077 \
/opt/spark/scripts/processar_spark.py
```

## Resultados

### Armazenamento

| Formato | Tamanho |
|---------|---------|
| CSV | 4,7 MB |
| JSON | 10,8 MB |
| Parquet | 1,4 MB |

### Tempo de processamento (2 Workers)

| Formato | Tempo |
|---------|-------:|
| CSV | 7,79 s |
| JSON | 1,60 s |
| Parquet | 1,30 s |

### Tempo de processamento (1 Worker)

| Formato | Tempo |
|---------|-------:|
| CSV | 5,95 s |
| JSON | 1,40 s |
| Parquet | 0,95 s |

## Teste de Resiliência

Foi desligado um Spark Worker durante os testes.

Mesmo com apenas um Worker ativo, o Spark conseguiu concluir o processamento normalmente, demonstrando a capacidade do cluster de continuar funcionando em caso de falha de um nó.

## Conclusão

O ambiente desenvolvido atendeu aos objetivos propostos. Foi possível armazenar e processar arquivos em diferentes formatos utilizando Hadoop e Spark. Os testes demonstraram o funcionamento do cluster e a capacidade de continuar executando tarefas mesmo após a indisponibilidade de um dos Workers.
