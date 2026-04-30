# =============================================================================
# PROJETO: Análise Exploratória de Dados com Python
# Módulo 2 - Introdução à Ciência de Dados e Python
# Bootcamp TOTVS - Fundamentos de Engenharia de Dados e Machine Learning
# =============================================================================

# -----------------------------------------------------------------------------
# RACIOCÍNIO DO PROJETO:
# A Análise Exploratória de Dados (EDA - Exploratory Data Analysis) é o
# primeiro passo de qualquer projeto de ciência de dados. Antes de criar
# modelos ou fazer previsões, precisamos ENTENDER os dados:
#   - Quantos registros temos?
#   - Existem valores ausentes (NaN)?
#   - Como os dados estão distribuídos?
#   - Existem outliers (valores extremos)?
#   - Quais variáveis se correlacionam?
#
# Bibliotecas usadas:
#   - pandas: manipulação e análise de dados em tabelas (DataFrames)
#   - numpy: operações matemáticas e geração de dados
#   - matplotlib: criação de gráficos
#   - seaborn: gráficos estatísticos mais elegantes (baseado no matplotlib)
# -----------------------------------------------------------------------------

import pandas as pd        # Manipulação de dados
import numpy as np         # Operações numéricas
import matplotlib.pyplot as plt  # Gráficos
import seaborn as sns      # Gráficos estatísticos
import os                  # Criação de diretórios

# Configurações visuais globais
sns.set_theme(style="whitegrid")   # Estilo dos gráficos
plt.rcParams["figure.figsize"] = (10, 6)  # Tamanho padrão dos gráficos

# Cria pasta para salvar os gráficos gerados
os.makedirs("graficos", exist_ok=True)


# =============================================================================
# PARTE 1: CRIAÇÃO DO DATASET
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Em projetos reais, os dados viriam de um arquivo CSV, banco de dados ou API.
# Aqui simulamos um dataset de vendas de uma empresa fictícia para praticar
# todas as técnicas de EDA sem depender de dados externos.
#
# np.random.seed(42) garante que os números aleatórios sejam sempre os mesmos
# toda vez que o código rodar — isso é chamado de "reprodutibilidade"
# -----------------------------------------------------------------------------

np.random.seed(42)  # Semente para reprodutibilidade

n = 200  # Número de registros no dataset

# Criamos o DataFrame diretamente com um dicionário Python
# Cada chave vira uma coluna, cada lista vira os valores da coluna
df = pd.DataFrame({
    "id_venda": range(1, n + 1),  # IDs de 1 até 200

    # np.random.choice escolhe aleatoriamente entre as opções dadas
    "produto": np.random.choice(
        ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado"],
        size=n
    ),

    "regiao": np.random.choice(
        ["Norte", "Sul", "Leste", "Oeste", "Centro"],
        size=n
    ),

    # np.random.randint gera inteiros aleatórios entre os valores definidos
    "quantidade": np.random.randint(1, 11, size=n),  # Entre 1 e 10 unidades

    # np.random.uniform gera decimais aleatórios no intervalo definido
    "preco_unitario": np.random.uniform(500, 5000, size=n).round(2),

    # pd.date_range cria uma sequência de datas
    # np.random.choice sorteia 200 datas desse intervalo
    "data_venda": np.random.choice(
        pd.date_range("2024-01-01", "2024-12-31"),
        size=n
    ),
})

# Calculamos a receita total de cada venda (quantidade × preço)
df["receita_total"] = (df["quantidade"] * df["preco_unitario"]).round(2)

# Simulamos valores ausentes (NaN) em 5% dos registros de preço
# Isso é comum em dados reais — dados faltantes precisam ser tratados
indices_nan = np.random.choice(df.index, size=int(n * 0.05), replace=False)
df.loc[indices_nan, "preco_unitario"] = np.nan

print("=" * 60)
print("ANÁLISE EXPLORATÓRIA DE DADOS - VENDAS 2024")
print("=" * 60)


# =============================================================================
# PARTE 2: INSPEÇÃO INICIAL DOS DADOS
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Antes de qualquer análise, sempre inspecionamos o dataset para entender
# sua estrutura. Essas são as primeiras funções que qualquer cientista de
# dados roda ao receber um novo conjunto de dados.
# -----------------------------------------------------------------------------

print("\n📌 SHAPE DO DATASET (linhas, colunas):")
print(df.shape)
# shape retorna uma tupla (linhas, colunas)
# Nos diz o "tamanho" do nosso dataset

print("\n📌 PRIMEIROS 5 REGISTROS (df.head()):")
print(df.head())
# head() mostra as primeiras N linhas (padrão = 5)
# Útil para ver como os dados estão estruturados

print("\n📌 TIPOS DE DADOS DE CADA COLUNA:")
print(df.dtypes)
# dtypes mostra o tipo de cada coluna:
# int64 = número inteiro, float64 = decimal, object = texto, datetime64 = data

print("\n📌 VALORES AUSENTES POR COLUNA:")
print(df.isnull().sum())
# isnull() retorna True/False para cada célula
# .sum() soma os True (NaN) de cada coluna


# =============================================================================
# PARTE 3: ESTATÍSTICAS DESCRITIVAS
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# describe() é uma das funções mais poderosas do pandas — ela calcula
# automaticamente as principais estatísticas de todas as colunas numéricas:
# count, mean (média), std (desvio padrão), min, quartis e max
# -----------------------------------------------------------------------------

print("\n📊 ESTATÍSTICAS DESCRITIVAS:")
print(df[["quantidade", "preco_unitario", "receita_total"]].describe().round(2))


# =============================================================================
# PARTE 4: ANÁLISE POR CATEGORIA
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# groupby() agrupa os dados por uma coluna categórica (ex: produto)
# e permite calcular estatísticas para cada grupo separadamente.
# É equivalente ao GROUP BY do SQL.
# -----------------------------------------------------------------------------

print("\n📊 RECEITA TOTAL POR PRODUTO:")
receita_por_produto = (
    df.groupby("produto")["receita_total"]
    .sum()                    # Soma a receita de cada produto
    .sort_values(ascending=False)  # Ordena do maior para o menor
    .round(2)
)
print(receita_por_produto)

print("\n📊 QUANTIDADE MÉDIA VENDIDA POR REGIÃO:")
media_por_regiao = (
    df.groupby("regiao")["quantidade"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)
print(media_por_regiao)


# =============================================================================
# PARTE 5: TRATAMENTO DE VALORES AUSENTES
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Existem várias estratégias para lidar com NaN:
# 1. Remover as linhas com NaN (dropna) — perde dados
# 2. Preencher com a média/mediana (fillna) — mantém os dados
# 3. Preencher com um valor específico
#
# Aqui usamos a mediana por ser mais robusta a outliers do que a média
# -----------------------------------------------------------------------------

mediana_preco = df["preco_unitario"].median()
df["preco_unitario"] = df["preco_unitario"].fillna(mediana_preco)

print(f"\n✅ Valores ausentes preenchidos com a mediana: R$ {mediana_preco:.2f}")
print(f"   Valores ausentes restantes: {df['preco_unitario'].isnull().sum()}")


# =============================================================================
# PARTE 6: VISUALIZAÇÕES
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Gráficos são fundamentais para comunicar insights. Vamos criar 4 gráficos:
# 1. Barras — receita por produto
# 2. Histograma — distribuição dos preços
# 3. Boxplot — identificação de outliers
# 4. Linha — evolução da receita ao longo do tempo
# -----------------------------------------------------------------------------

# --- GRÁFICO 1: Receita por Produto ---
fig, ax = plt.subplots()
receita_por_produto.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")
ax.set_title("Receita Total por Produto (2024)", fontsize=14, fontweight="bold")
ax.set_xlabel("Produto")
ax.set_ylabel("Receita Total (R$)")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig("graficos/01_receita_por_produto.png", dpi=150)
plt.close()
print("\n📈 Gráfico salvo: graficos/01_receita_por_produto.png")


# --- GRÁFICO 2: Distribuição dos Preços (Histograma) ---
# Um histograma mostra como os dados estão distribuídos
# bins=20 divide o eixo X em 20 faixas de valores
fig, ax = plt.subplots()
sns.histplot(df["preco_unitario"], bins=20, kde=True, color="steelblue", ax=ax)
# kde=True adiciona a curva de densidade (estimativa suavizada da distribuição)
ax.set_title("Distribuição dos Preços Unitários", fontsize=14, fontweight="bold")
ax.set_xlabel("Preço Unitário (R$)")
ax.set_ylabel("Frequência")
plt.tight_layout()
plt.savefig("graficos/02_distribuicao_precos.png", dpi=150)
plt.close()
print("📈 Gráfico salvo: graficos/02_distribuicao_precos.png")


# --- GRÁFICO 3: Boxplot de Receita por Produto ---
# O boxplot mostra a mediana, quartis e outliers de cada grupo
# É excelente para comparar distribuições e identificar valores extremos
fig, ax = plt.subplots()
sns.boxplot(data=df, x="produto", y="receita_total", palette="Blues", ax=ax)
ax.set_title("Distribuição da Receita por Produto", fontsize=14, fontweight="bold")
ax.set_xlabel("Produto")
ax.set_ylabel("Receita Total (R$)")
plt.tight_layout()
plt.savefig("graficos/03_boxplot_receita.png", dpi=150)
plt.close()
print("📈 Gráfico salvo: graficos/03_boxplot_receita.png")


# --- GRÁFICO 4: Receita Mensal (Série Temporal) ---
# Extraímos o mês de cada venda e agrupamos para ver a evolução no tempo
df["mes"] = pd.to_datetime(df["data_venda"]).dt.to_period("M")
# dt.to_period("M") converte a data para o período mensal (ex: 2024-01)

receita_mensal = df.groupby("mes")["receita_total"].sum()

fig, ax = plt.subplots()
receita_mensal.plot(kind="line", marker="o", color="steelblue", ax=ax)
ax.set_title("Evolução da Receita Mensal (2024)", fontsize=14, fontweight="bold")
ax.set_xlabel("Mês")
ax.set_ylabel("Receita Total (R$)")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.savefig("graficos/04_receita_mensal.png", dpi=150)
plt.close()
print("📈 Gráfico salvo: graficos/04_receita_mensal.png")


# =============================================================================
# PARTE 7: EXPORTANDO O DATASET LIMPO
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Após a limpeza e análise, é boa prática salvar o dataset tratado
# em um arquivo CSV para uso futuro (ex: alimentar um modelo de ML)
# index=False evita salvar o índice do pandas como uma coluna extra
# -----------------------------------------------------------------------------

df.to_csv("vendas_2024_limpo.csv", index=False, encoding="utf-8-sig")
# encoding="utf-8-sig" garante que acentos apareçam corretamente no Excel

print("\n✅ Dataset limpo exportado: vendas_2024_limpo.csv")
print("\n🎉 Análise exploratória concluída!")
