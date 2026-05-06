# 🗄️ Pipeline ETL com Python e SQLite

> Projeto do **Módulo 3** do Bootcamp TOTVS – Fundamentos de Engenharia de Dados e Machine Learning (DIO)

---

## 🎯 Objetivo

Construir um **pipeline ETL completo** (Extract → Transform → Load) que processa dados brutos de pedidos de vendas, trata inconsistências e carrega os dados num banco de dados relacional SQLite para consultas SQL.

---

## 🧠 O que é ETL?

```
EXTRACT  → Extrair dados brutos da fonte (CSV, API, banco legado...)
    ↓
TRANSFORM → Limpar, padronizar e enriquecer os dados
    ↓
LOAD      → Carregar os dados tratados no destino (banco de dados)
```

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| Leitura de CSV | `pd.read_csv()` na fase de extração |
| Tratamento de NaN | `.fillna()` na transformação |
| Padronização de strings | `.str.lower()`, `.str.title()` |
| Parsing de datas | `pd.to_datetime()` |
| Colunas derivadas | `quantidade × preco_unitario` |
| Banco de dados SQLite | `sqlite3.connect()` |
| Criação de tabela | `CREATE TABLE IF NOT EXISTS` |
| Carga de dados | `df.to_sql()` |
| Consultas SQL | `SELECT`, `GROUP BY`, `ORDER BY`, `HAVING` |
| SQL via pandas | `pd.read_sql_query()` |

---

## 📁 Estrutura de arquivos

```
modulo3-banco-dados-etl/
│
├── etl_pipeline.py              # Pipeline ETL completo (Extract→Transform→Load)
├── queries.sql                  # Arquivo com consultas SQL comentadas
├── dados/                       # Gerado ao rodar o script
│   ├── pedidos_brutos.csv       # Dados originais com problemas
│   ├── pedidos_transformados.csv# Dados após transformação
│   └── vendas.db                # Banco SQLite com os dados carregados
└── README.md
```

---

## ▶️ Como executar

**Pré-requisito:** Python 3.8+ e pandas instalados.

```bash
# Acesse a pasta do projeto
cd modulo3-banco-dados-etl

# Instale as dependências (só pandas, o sqlite3 já vem com Python)
pip install pandas

# Execute o pipeline
python etl_pipeline.py
```

---

## 🔍 Problemas tratados na transformação

| Problema | Solução |
|---|---|
| Nomes com capitalização errada (`joão`, `ANA`) | `.str.title()` |
| Status inconsistente (`PENDENTE`, `Concluido`) | `.str.lower()` |
| Datas com formato diferente (`2024/01/18`) | `pd.to_datetime()` |
| Valores ausentes em cliente | `.fillna("Desconhecido")` |
| Valores ausentes em quantidade | `.fillna(1)` |

---

## 🗃️ Visualizando o banco de dados

Para abrir o banco `vendas.db` visualmente, instale o **DB Browser for SQLite**:
👉 [https://sqlitebrowser.org/dl/](https://sqlitebrowser.org/dl/)

É gratuito e permite ver as tabelas e rodar as queries do arquivo `queries.sql`.

---

## 📊 Consultas SQL incluídas

- `SELECT` básico com `WHERE` e `ORDER BY`
- Funções de agregação: `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`
- Agrupamento com `GROUP BY` e filtro com `HAVING`
- Subconsultas (subqueries)
- Manipulação de dados: `INSERT`, `UPDATE`, `DELETE`

---

## 👨‍💻 Autor

Desenvolvido durante o **Bootcamp TOTVS – DIO**  
🔗 [LinkedIn](#) | 🐙 [GitHub](#)
