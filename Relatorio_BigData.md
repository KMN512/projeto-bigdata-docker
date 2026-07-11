RELATÓRIO
Desenvolvimento de um Ambiente Big Data utilizando Docker, Hadoop e Apache Spark
1. Introdução

O crescimento do volume de dados gerados diariamente exige tecnologias capazes de armazenar e processar grandes quantidades de informações de forma eficiente. Nesse contexto, ferramentas como Hadoop e Apache Spark são amplamente utilizadas em ambientes de Big Data por permitirem processamento distribuído e escalabilidade.

Neste projeto foi desenvolvido um ambiente local utilizando Docker, simulando um cluster de Big Data composto por Hadoop HDFS e Apache Spark.

2. Objetivo

Desenvolver um ambiente de Big Data capaz de:

armazenar arquivos CSV, JSON e Parquet;
processar os dados utilizando Apache Spark;
avaliar o desempenho dos diferentes formatos;
verificar o comportamento do sistema diante da falha de um nó.
3. Tecnologias utilizadas
Tecnologia	Finalidade
Docker	Virtualização dos serviços
Hadoop HDFS	Armazenamento distribuído
Apache Spark	Processamento distribuído
Python	Geração e processamento dos dados
Pandas	Manipulação dos dados
PyArrow	Criação do arquivo Parquet
4. Arquitetura

Insira aqui o diagrama que acabamos de criar.

Legenda:

Docker Host
Spark Master
Spark Worker 1
Spark Worker 2
Hadoop NameNode
Hadoop DataNode
Arquivos CSV, JSON e Parquet
5. Fluxo dos dados

O fluxo de execução ocorreu conforme as etapas abaixo:

Geração dos arquivos CSV, JSON e Parquet através de um script em Python.
Envio dos arquivos para o Hadoop HDFS.
Leitura dos dados utilizando Apache Spark.
Processamento distribuído entre os Workers.
Apresentação dos resultados.
6. Resultados
Espaço ocupado
Formato	Tamanho
CSV	4,7 MB
JSON	10,8 MB
Parquet	1,4 MB
Processamento com 2 Workers
Formato	Tempo
CSV	7,79 s
JSON	1,60 s
Parquet	1,30 s
Processamento com apenas 1 Worker
Formato	Tempo
CSV	5,95 s
JSON	1,40 s
Parquet	0,95 s
7. Teste de Resiliência

Durante os testes foi desligado um dos Spark Workers.

Mesmo com apenas um Worker ativo, o processamento foi concluído com sucesso, demonstrando que o cluster permaneceu operacional mesmo diante da falha de um dos nós.

8. Análise dos resultados

Os testes mostraram que:

o formato Parquet ocupou menos espaço em disco;
CSV apresentou maior tempo de leitura;
JSON apresentou desempenho intermediário;
o ambiente continuou funcionando mesmo após a falha de um Worker.

Embora os testes com um Worker tenham apresentado tempos ligeiramente menores, esse comportamento pode ser explicado pelo pequeno volume de dados processados (100 mil registros). Em conjuntos de dados maiores, espera-se que o uso de múltiplos Workers apresente ganhos mais evidentes devido ao paralelismo do processamento.

9. Conclusão

O ambiente desenvolvido atingiu os objetivos propostos. Foi possível criar um cluster local utilizando Docker, Hadoop e Apache Spark, armazenar dados em diferentes formatos e realizar processamento distribuído.

Os testes também demonstraram a capacidade do ambiente em continuar processando informações mesmo após a indisponibilidade de um dos Workers, evidenciando a resiliência da arquitetura adotada.
