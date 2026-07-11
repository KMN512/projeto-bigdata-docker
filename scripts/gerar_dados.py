from pathlib import Path
import random
import pandas as pd

QUANTIDADE_REGISTROS = 100_000

produtos = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor",
    "Headset",
    "Webcam",
]

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Curitiba",
    "Florianópolis",
    "Porto Alegre",
]

categorias = [
    "Informática",
    "Acessórios",
    "Eletrônicos",
]

dados = {
    "id": range(1, QUANTIDADE_REGISTROS + 1),
    "produto": [
        random.choice(produtos)
        for _ in range(QUANTIDADE_REGISTROS)
    ],
    "categoria": [
        random.choice(categorias)
        for _ in range(QUANTIDADE_REGISTROS)
    ],
    "cidade": [
        random.choice(cidades)
        for _ in range(QUANTIDADE_REGISTROS)
    ],
    "valor": [
        round(random.uniform(20, 5000), 2)
        for _ in range(QUANTIDADE_REGISTROS)
    ],
    "quantidade": [
        random.randint(1, 10)
        for _ in range(QUANTIDADE_REGISTROS)
    ],
}

dataframe = pd.DataFrame(dados)

pasta_projeto = Path(__file__).resolve().parent.parent
pasta_dados = pasta_projeto / "dados"
pasta_dados.mkdir(exist_ok=True)

arquivo_csv = pasta_dados / "vendas.csv"
arquivo_json = pasta_dados / "vendas.json"
arquivo_parquet = pasta_dados / "vendas.parquet"

print("Gerando CSV...")
dataframe.to_csv(arquivo_csv, index=False)

print("Gerando JSON...")
dataframe.to_json(
    arquivo_json,
    orient="records",
    lines=True,
    force_ascii=False,
)

print("Gerando Parquet...")
dataframe.to_parquet(
    arquivo_parquet,
    index=False,
)

print("\nArquivos gerados com sucesso:")
print(arquivo_csv)
print(arquivo_json)
print(arquivo_parquet)
print(f"\nTotal de registros: {len(dataframe):,}")