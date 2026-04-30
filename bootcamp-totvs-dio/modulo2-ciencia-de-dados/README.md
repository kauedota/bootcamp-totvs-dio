# 📊 Análise Exploratória de Dados com Python

> Projeto do **Módulo 2** do Bootcamp TOTVS – Fundamentos de Engenharia de Dados e Machine Learning (DIO)

---

## 🎯 Objetivo

Realizar uma **Análise Exploratória de Dados (EDA)** completa sobre um dataset simulado de vendas, aplicando as principais técnicas e bibliotecas de Ciência de Dados com Python.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no código |
|---|---|
| Criação de DataFrames | `pd.DataFrame({...})` com dados simulados |
| Inspeção de dados | `.shape`, `.head()`, `.dtypes`, `.isnull()` |
| Estatísticas descritivas | `.describe()` |
| Agrupamento de dados | `.groupby()` + `.sum()` / `.mean()` |
| Tratamento de NaN | `.fillna(mediana)` |
| Séries temporais | `pd.to_datetime()`, `.dt.to_period()` |
| Visualização | Gráfico de barras, histograma, boxplot, linha |
| Exportação | `.to_csv()` |

---

## 📁 Estrutura de arquivos

```
modulo2-ciencia-de-dados/
│
├── analise_exploratoria.py   # Código principal com EDA completa
├── requirements.txt          # Bibliotecas necessárias
├── vendas_2024_limpo.csv     # Gerado ao rodar o script
├── graficos/                 # Pasta gerada ao rodar o script
│   ├── 01_receita_por_produto.png
│   ├── 02_distribuicao_precos.png
│   ├── 03_boxplot_receita.png
│   └── 04_receita_mensal.png
└── README.md
```

---

## ▶️ Como executar

```bash
# Acesse a pasta do projeto
cd modulo2-ciencia-de-dados

# Instale as dependências
pip install -r requirements.txt

# Execute o script
python analise_exploratoria.py
```

---

## 📈 Gráficos gerados

| # | Gráfico | O que mostra |
|---|---------|-------------|
| 1 | Receita por Produto | Qual produto mais fatura |
| 2 | Distribuição de Preços | Como os preços estão distribuídos |
| 3 | Boxplot por Produto | Variação e outliers de receita |
| 4 | Receita Mensal | Evolução das vendas ao longo do ano |

---

## 🔍 Etapas da análise

```
1. Criação do dataset simulado (200 registros de vendas)
      ↓
2. Inspeção inicial (shape, tipos, valores ausentes)
      ↓
3. Estatísticas descritivas (média, mediana, desvio padrão)
      ↓
4. Análise por categoria (produto e região)
      ↓
5. Tratamento de valores ausentes (fillna com mediana)
      ↓
6. Visualizações (4 gráficos)
      ↓
7. Exportação do dataset limpo (CSV)
```

---

## 🗂️ Bibliotecas utilizadas

- **pandas** — manipulação e análise de dados
- **numpy** — operações numéricas e geração de dados
- **matplotlib** — criação de gráficos
- **seaborn** — gráficos estatísticos elegantes

---

## 👨‍💻 Autor

Desenvolvido durante o **Bootcamp TOTVS – DIO**  
🔗 [LinkedIn](#) | 🐙 [GitHub](#)
