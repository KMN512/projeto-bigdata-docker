import os
import random
import pandas as pd

QUANTIDADE = 1_000_000

produtos = [
    "Notebook",
    "Mouse",
    "Teclado",
    "Monitor",
    "Headset",
    "Webcam"
]

cidades = [
    "São Paulo",
    "Rio de Janeiro",
    "Curitiba",
    "Florianópolis",
    "Porto Alegre"
]

categorias = [
    "Informática",
    "Acessórios",
    "Eletrônicos"
]

dados = {
    "id": range(1, QUANTIDADE + 1),
    "produto": [random.choice(produtos) for _ in range(QUANTIDADE)],
    "categoria": [random.choice(categorias) for _ in range(QUANTIDADE)],
    "cidade": [random.choice(cidades) for _ in range(QUANTIDADE)],
    "valor": [round(random.uniform(20, 5000), 2) for _ in range(QUANTIDADE)],
    "quantidade": [random.randint(1, 10) for _ in range(QUANTIDADE)]
}

df = pd.DataFrame(dados)

pasta_dados = os.path.join(os.path.dirname(__file__), "..", "dados")
os.makedirs(pasta_dados, exist_ok=True)

arquivo_csv = os.path.join(pasta_dados, "vendas.csv")
arquivo_json = os.path.join(pasta_dados, "vendas.json")
arquivo_parquet = os.path.join(pasta_dados, "vendas.parquet")

print("Gerando CSV...")
df.to_csv(arquivo_csv, index=False)

print("Gerando JSON...")
df.to_json(
    arquivo_json,
    orient="records",
    lines=True,
    force_ascii=False
)

print("Gerando Parquet...")
df.to_parquet(
    arquivo_parquet,
    index=False
)

print("Arquivos criados com sucesso:")
print(arquivo_csv)
print(arquivo_json)
print(arquivo_parquet)