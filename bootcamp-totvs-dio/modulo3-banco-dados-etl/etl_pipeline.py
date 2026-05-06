# =============================================================================
# PROJETO: Pipeline ETL com Python e SQLite
# Módulo 3 - Introdução a Banco de Dados Relacionais e ETL
# Bootcamp TOTVS - Fundamentos de Engenharia de Dados e Machine Learning
# =============================================================================

# -----------------------------------------------------------------------------
# RACIOCÍNIO DO PROJETO:
# ETL significa Extract, Transform, Load (Extrair, Transformar, Carregar).
# É o processo central da Engenharia de Dados:
#
#   EXTRACT  → Buscar dados brutos de uma fonte (CSV, API, banco, etc.)
#   TRANSFORM → Limpar, padronizar e enriquecer os dados
#   LOAD      → Salvar os dados tratados em um banco de dados relacional
#
# Neste projeto simulamos um cenário real:
#   - Uma empresa recebe pedidos em CSV (fonte de dados bruta)
#   - Precisamos tratar esses dados (transformação)
#   - E carregá-los num banco SQLite para consultas SQL (carga)
#
# Bibliotecas usadas:
#   - sqlite3: banco de dados relacional embutido no Python (sem instalação)
#   - pandas: manipulação dos dados na etapa de transformação
#   - csv: leitura de arquivos CSV na etapa de extração
# -----------------------------------------------------------------------------

import sqlite3      # Banco de dados relacional (built-in do Python)
import pandas as pd # Manipulação de dados
import numpy as np  # Geração de dados simulados
import os           # Criação de diretórios
from datetime import datetime  # Manipulação de datas

os.makedirs("dados", exist_ok=True)  # Pasta para arquivos gerados

print("=" * 60)
print("  PIPELINE ETL - PEDIDOS DE VENDAS")
print("=" * 60)


# =============================================================================
# FASE 1: EXTRACT (EXTRAÇÃO)
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Na vida real, os dados chegam de fontes diversas e geralmente "sujos":
# valores faltando, formatos inconsistentes, duplicatas, etc.
# Aqui simulamos um CSV bruto com esses problemas propositalmente
# para praticar o tratamento na fase de transformação.
# -----------------------------------------------------------------------------

print("\n📥 FASE 1: EXTRAÇÃO DOS DADOS")
print("-" * 40)

# Simulamos o CSV bruto que chegaria de um sistema legado
dados_brutos = """id_pedido,cliente,produto,quantidade,preco_unitario,data_pedido,status
1,Maria Silva,Notebook,2,3500.00,2024-01-15,concluido
2,joão santos,Smartphone,1,2200.50,2024-01-16,PENDENTE
3,ANA OLIVEIRA,Tablet,,1800.00,2024-01-17,concluido
4,Carlos Lima,Monitor,3,1200.00,2024/01/18,concluido
5,maria silva,Notebook,1,3500.00,2024-01-19,cancelado
6,Pedro Costa,Teclado,5,350.00,2024-01-20,CONCLUIDO
7,,Smartphone,2,2200.50,2024-01-21,pendente
8,Fernanda Rocha,Tablet,1,1800.00,2024-01-22,concluido
9,Carlos Lima,Monitor,2,1200.00,2024-01-23,Concluido
10,Julia Mendes,Notebook,3,3500.00,2024-01-24,concluido
"""

# Salvamos o CSV bruto na pasta dados/
with open("dados/pedidos_brutos.csv", "w", encoding="utf-8") as f:
    f.write(dados_brutos)

# Lemos com pandas — sep="," define o separador de colunas
df_bruto = pd.read_csv("dados/pedidos_brutos.csv")

print(f"✅ {len(df_bruto)} registros extraídos do arquivo CSV")
print("\nDados brutos (primeiras linhas):")
print(df_bruto.head())

print("\n⚠️  Problemas encontrados nos dados brutos:")
print(f"   - Valores ausentes: {df_bruto.isnull().sum().sum()} células")
print(f"   - Nomes com capitalização inconsistente (ex: 'joão santos', 'ANA OLIVEIRA')")
print(f"   - Datas com formatos diferentes (2024-01-18 vs 2024/01/18)")
print(f"   - Status com capitalização variada (concluido, PENDENTE, Concluido)")


# =============================================================================
# FASE 2: TRANSFORM (TRANSFORMAÇÃO)
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# A transformação é onde a maior parte do trabalho acontece.
# Vamos resolver cada problema identificado na extração:
# 1. Padronizar nomes (title case)
# 2. Padronizar status (lowercase)
# 3. Corrigir formato de datas
# 4. Tratar valores ausentes
# 5. Calcular coluna derivada (receita_total)
# 6. Remover/sinalizar duplicatas
# -----------------------------------------------------------------------------

print("\n\n🔄 FASE 2: TRANSFORMAÇÃO DOS DADOS")
print("-" * 40)

# Trabalhamos em uma cópia para preservar os dados originais
df = df_bruto.copy()

# --- TRANSFORMAÇÃO 1: Padronizar nomes de clientes ---
# .str.title() transforma "maria silva" → "Maria Silva"
# .str.strip() remove espaços extras no início e fim
df["cliente"] = df["cliente"].str.title().str.strip()
print("✅ Nomes de clientes padronizados (title case)")

# --- TRANSFORMAÇÃO 2: Padronizar status ---
# .str.lower() transforma "PENDENTE", "Concluido" → "pendente", "concluido"
df["status"] = df["status"].str.lower().str.strip()
print("✅ Status padronizados (lowercase)")

# --- TRANSFORMAÇÃO 3: Corrigir formato de datas ---
# pd.to_datetime com infer_datetime_format detecta automaticamente
# o formato da data, seja "2024-01-18" ou "2024/01/18"
df["data_pedido"] = pd.to_datetime(df["data_pedido"], format="mixed")
print("✅ Datas normalizadas para formato padrão")

# --- TRANSFORMAÇÃO 4: Tratar valores ausentes ---
# Cliente ausente: preenchemos com "Desconhecido"
qtd_clientes_nulos = df["cliente"].isnull().sum()
df["cliente"] = df["cliente"].fillna("Desconhecido")

# Quantidade ausente: preenchemos com 1 (pedido mínimo)
qtd_quantidade_nulos = df["quantidade"].isnull().sum()
df["quantidade"] = df["quantidade"].fillna(1).astype(int)

print(f"✅ {qtd_clientes_nulos} cliente(s) ausente(s) → 'Desconhecido'")
print(f"✅ {qtd_quantidade_nulos} quantidade(s) ausente(s) → 1")

# --- TRANSFORMAÇÃO 5: Criar coluna derivada ---
# Calculamos a receita total de cada pedido
df["receita_total"] = (df["quantidade"] * df["preco_unitario"]).round(2)
print("✅ Coluna 'receita_total' calculada (quantidade × preço)")

# --- TRANSFORMAÇÃO 6: Adicionar timestamp de processamento ---
# Registra quando o ETL foi executado — essencial para auditoria
df["processado_em"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("✅ Timestamp de processamento adicionado")

# --- TRANSFORMAÇÃO 7: Extrair informações da data ---
# Colunas derivadas da data facilitam análises posteriores
df["ano"] = df["data_pedido"].dt.year
df["mes"] = df["data_pedido"].dt.month
df["dia_semana"] = df["data_pedido"].dt.day_name()
print("✅ Colunas de ano, mês e dia da semana extraídas")

print("\nDados transformados:")
print(df[["id_pedido", "cliente", "status", "quantidade", "receita_total"]].to_string(index=False))

# Salvamos o CSV transformado
df.to_csv("dados/pedidos_transformados.csv", index=False, encoding="utf-8-sig")
print("\n✅ Dados transformados salvos em: dados/pedidos_transformados.csv")


# =============================================================================
# FASE 3: LOAD (CARGA NO BANCO DE DADOS)
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# SQLite é um banco de dados relacional que fica em um único arquivo .db
# É ideal para aprender SQL e para projetos de médio porte.
# Em produção, usaríamos PostgreSQL, MySQL ou o próprio banco da TOTVS.
#
# sqlite3.connect() cria a conexão com o banco (cria o arquivo se não existir)
# cursor é o objeto que executa os comandos SQL
# -----------------------------------------------------------------------------

print("\n\n📤 FASE 3: CARGA NO BANCO DE DADOS")
print("-" * 40)

# Conecta ao banco SQLite (cria o arquivo se não existir)
conn = sqlite3.connect("dados/vendas.db")
cursor = conn.cursor()

# --- CRIAÇÃO DA TABELA ---
# CREATE TABLE IF NOT EXISTS: cria a tabela só se ainda não existir
# Isso evita erro se rodarmos o script mais de uma vez
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id_pedido       INTEGER PRIMARY KEY,
        cliente         TEXT NOT NULL,
        produto         TEXT NOT NULL,
        quantidade      INTEGER NOT NULL,
        preco_unitario  REAL NOT NULL,
        receita_total   REAL NOT NULL,
        data_pedido     TEXT NOT NULL,
        status          TEXT NOT NULL,
        ano             INTEGER,
        mes             INTEGER,
        dia_semana      TEXT,
        processado_em   TEXT
    )
""")

# Limpa registros anteriores para evitar duplicatas ao re-executar
cursor.execute("DELETE FROM pedidos")

# --- INSERÇÃO DOS DADOS ---
# Usamos pandas to_sql para inserir o DataFrame inteiro de uma vez
# if_exists="append": adiciona os dados sem recriar a tabela
# index=False: não salva o índice do pandas como coluna
colunas_para_carregar = [
    "id_pedido", "cliente", "produto", "quantidade",
    "preco_unitario", "receita_total", "data_pedido",
    "status", "ano", "mes", "dia_semana", "processado_em"
]

df[colunas_para_carregar].to_sql(
    "pedidos",           # Nome da tabela
    conn,                # Conexão com o banco
    if_exists="append",  # Adiciona sem recriar a tabela
    index=False          # Não salva o índice do pandas
)

conn.commit()  # Confirma (salva) as alterações no banco
print(f"✅ {len(df)} registros carregados na tabela 'pedidos' do banco SQLite")


# =============================================================================
# FASE 4: CONSULTAS SQL (VALIDAÇÃO E ANÁLISE)
# =============================================================================
# -----------------------------------------------------------------------------
# RACIOCÍNIO:
# Após carregar os dados, fazemos consultas SQL para:
# 1. Validar que a carga funcionou corretamente
# 2. Gerar insights sobre os dados
#
# pd.read_sql_query() executa SQL e retorna um DataFrame diretamente
# Isso combina o poder do SQL com a facilidade do pandas
# -----------------------------------------------------------------------------

print("\n\n🔍 FASE 4: CONSULTAS SQL DE VALIDAÇÃO E ANÁLISE")
print("-" * 40)

# --- CONSULTA 1: Total de registros ---
resultado = pd.read_sql_query("SELECT COUNT(*) as total FROM pedidos", conn)
print(f"\n📌 Total de pedidos no banco: {resultado['total'][0]}")

# --- CONSULTA 2: Receita por status ---
print("\n📌 RECEITA TOTAL POR STATUS:")
query_status = """
    SELECT 
        status,
        COUNT(*) as quantidade_pedidos,
        SUM(receita_total) as receita_total,
        AVG(receita_total) as ticket_medio
    FROM pedidos
    GROUP BY status
    ORDER BY receita_total DESC
"""
df_status = pd.read_sql_query(query_status, conn)
df_status["receita_total"] = df_status["receita_total"].round(2)
df_status["ticket_medio"] = df_status["ticket_medio"].round(2)
print(df_status.to_string(index=False))

# --- CONSULTA 3: Top clientes ---
print("\n📌 TOP CLIENTES POR RECEITA:")
query_clientes = """
    SELECT 
        cliente,
        COUNT(*) as total_pedidos,
        SUM(receita_total) as receita_total
    FROM pedidos
    WHERE status = 'concluido'
    GROUP BY cliente
    ORDER BY receita_total DESC
    LIMIT 5
"""
df_clientes = pd.read_sql_query(query_clientes, conn)
df_clientes["receita_total"] = df_clientes["receita_total"].round(2)
print(df_clientes.to_string(index=False))

# --- CONSULTA 4: Produto mais vendido ---
print("\n📌 PRODUTOS MAIS VENDIDOS (QUANTIDADE):")
query_produtos = """
    SELECT 
        produto,
        SUM(quantidade) as total_unidades,
        SUM(receita_total) as receita_total
    FROM pedidos
    GROUP BY produto
    ORDER BY total_unidades DESC
"""
df_produtos = pd.read_sql_query(query_produtos, conn)
df_produtos["receita_total"] = df_produtos["receita_total"].round(2)
print(df_produtos.to_string(index=False))

# Fecha a conexão com o banco
conn.close()

print("\n" + "=" * 60)
print("  ✅ PIPELINE ETL CONCLUÍDO COM SUCESSO!")
print("=" * 60)
print(f"\n  Arquivos gerados:")
print(f"  📄 dados/pedidos_brutos.csv       → Dados originais")
print(f"  📄 dados/pedidos_transformados.csv → Dados após ETL")
print(f"  🗄️  dados/vendas.db               → Banco SQLite")
