# 📋 Gerenciador de Tarefas com Python

> Projeto do **Módulo 1** do Bootcamp TOTVS – Fundamentos de Engenharia de Dados e Machine Learning (DIO)

---

## 🎯 Objetivo

Consolidar os fundamentos de Python construindo um gerenciador de tarefas via terminal com **persistência de dados em arquivo JSON**.

---

## 🧠 Conceitos aplicados

| Conceito | Onde aparece no código |
|---|---|
| Variáveis e tipos | Dicionários de tarefa (`id`, `descricao`, `concluida`) |
| Listas | Lista de tarefas carregada do arquivo |
| Funções | Cada operação é uma função separada |
| Condicionais | Verificações de existência, status e entrada do usuário |
| Laços | `while` no menu principal, `for` para listar tarefas |
| List comprehension | Remoção de tarefa por ID |
| Arquivos (I/O) | Leitura e escrita com `json.load` / `json.dump` |
| Módulos built-in | `json` e `os` da biblioteca padrão do Python |

---

## 📁 Estrutura de arquivos

```
modulo1-python-git/
│
├── gerenciador_tarefas.py   # Código principal do projeto
├── tarefas.json             # Criado automaticamente ao rodar o programa
└── README.md                # Este arquivo
```

---

## ▶️ Como executar

**Pré-requisito:** Python 3.8 ou superior instalado.

```bash
# Clone o repositório
git clone https://github.com/kauedota/bootcamp-totvs-dio.git

# Acesse a pasta do projeto
cd bootcamp-totvs-dio/modulo1-python-git

# Execute o programa
python gerenciador_tarefas.py
```

---

## 💡 Funcionalidades

- ✅ **Listar** todas as tarefas com status visual
- ➕ **Adicionar** nova tarefa com ID automático
- ✔️ **Concluir** tarefa pelo ID
- 🗑️ **Remover** tarefa pelo ID
- 💾 **Persistência** — as tarefas são salvas em `tarefas.json` e carregadas ao reiniciar

---

## 🔄 Fluxo do programa

```
Início
  └── Carrega tarefas.json (ou cria lista vazia)
        └── Loop do menu
              ├── 1 → Listar tarefas
              ├── 2 → Adicionar tarefa → salva no arquivo
              ├── 3 → Concluir tarefa → salva no arquivo
              ├── 4 → Remover tarefa  → salva no arquivo
              └── 0 → Encerra o programa
```

---

## 🗂️ Exemplo do arquivo tarefas.json

```json
[
  {
    "id": 1,
    "descricao": "Estudar Python",
    "concluida": true
  },
  {
    "id": 2,
    "descricao": "Fazer projeto do bootcamp",
    "concluida": false
  }
]
```

---

## 🔗 Conexão com Git e GitHub

Este projeto foi versionado seguindo boas práticas:

```bash
git init
git add .
git commit -m "feat: adiciona gerenciador de tarefas com persistência JSON"
git branch -M main
git remote add origin https://github.com/seu-usuario/bootcamp-totvs-dio.git
git push -u origin main
```

**Convenção de commits usada (Conventional Commits):**
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` alteração em documentação
- `refactor:` refatoração sem mudança de comportamento

---

## 👨‍💻 Autor - Kaue Dota

Desenvolvido durante o **Bootcamp TOTVS – DIO**
🔗 [LinkedIn](#) | 🐙 [GitHub](#)
