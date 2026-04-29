# =============================================================================
# PROJETO: Gerenciador de Tarefas com Python
# Módulo 1 - Princípios de Python e Versionamento com Git e GitHub
# Bootcamp TOTVS - Fundamentos de Engenharia de Dados e Machine Learning
# =============================================================================

# -----------------------------------------------------------------------------
# RACIOCÍNIO DO PROJETO:
# Um gerenciador de tarefas é um projeto clássico e poderoso para consolidar
# os fundamentos de Python porque envolve:
#   - Variáveis e tipos de dados
#   - Listas (estrutura de dados essencial)
#   - Funções (organização e reutilização de código)
#   - Condicionais (if/elif/else)
#   - Laços de repetição (while/for)
#   - Entrada e saída de dados
#   - Leitura e escrita de arquivos (persistência de dados)
# -----------------------------------------------------------------------------


import json  # Usamos json para salvar e carregar as tarefas em um arquivo
import os    # Usamos os para verificar se o arquivo de tarefas já existe


# -----------------------------------------------------------------------------
# CONSTANTE: caminho do arquivo onde as tarefas serão salvas
# Usar uma constante evita repetir o nome do arquivo em vários lugares
# -----------------------------------------------------------------------------
ARQUIVO_TAREFAS = "tarefas.json"


# -----------------------------------------------------------------------------
# FUNÇÃO: carregar_tarefas()
# Objetivo: ler o arquivo JSON e retornar a lista de tarefas salvas
# Se o arquivo não existir (primeira execução), retorna uma lista vazia
# -----------------------------------------------------------------------------
def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):          # Verifica se o arquivo existe
        with open(ARQUIVO_TAREFAS, "r") as f:    # Abre o arquivo para leitura
            return json.load(f)                  # Converte JSON → lista Python
    return []                                    # Primeira execução: lista vazia


# -----------------------------------------------------------------------------
# FUNÇÃO: salvar_tarefas(tarefas)
# Objetivo: gravar a lista de tarefas no arquivo JSON
# O parâmetro "tarefas" é a lista que queremos persistir
# indent=2 formata o JSON de forma legível (com indentação de 2 espaços)
# -----------------------------------------------------------------------------
def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:        # Abre (ou cria) o arquivo
        json.dump(tarefas, f, indent=2, ensure_ascii=False)
        # ensure_ascii=False permite salvar acentos corretamente


# -----------------------------------------------------------------------------
# FUNÇÃO: adicionar_tarefa(tarefas, descricao)
# Objetivo: criar uma nova tarefa e adicioná-la à lista
# Cada tarefa é um dicionário com:
#   - "id": número único da tarefa
#   - "descricao": o texto da tarefa
#   - "concluida": booleano que indica se foi feita
# -----------------------------------------------------------------------------
def adicionar_tarefa(tarefas, descricao):
    # Geramos um ID automático: pega o maior ID existente e soma 1
    # Se a lista estiver vazia, o ID começa em 1
    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    tarefa = {
        "id": novo_id,
        "descricao": descricao,
        "concluida": False       # Toda tarefa nova começa como não concluída
    }

    tarefas.append(tarefa)       # Adiciona o dicionário à lista
    salvar_tarefas(tarefas)      # Persiste a lista atualizada no arquivo
    print(f"✅ Tarefa #{novo_id} adicionada: '{descricao}'")


# -----------------------------------------------------------------------------
# FUNÇÃO: listar_tarefas(tarefas)
# Objetivo: exibir todas as tarefas com seu status
# Usamos um loop for para iterar sobre cada tarefa da lista
# -----------------------------------------------------------------------------
def listar_tarefas(tarefas):
    if not tarefas:              # Se a lista estiver vazia
        print("📋 Nenhuma tarefa cadastrada ainda.")
        return

    print("\n📋 SUAS TAREFAS:")
    print("-" * 40)

    for tarefa in tarefas:
        # Operador ternário: define o símbolo de acordo com o status
        status = "✔️ " if tarefa["concluida"] else "⬜"
        print(f"[{status}] #{tarefa['id']} - {tarefa['descricao']}")

    print("-" * 40)


# -----------------------------------------------------------------------------
# FUNÇÃO: concluir_tarefa(tarefas, id_tarefa)
# Objetivo: marcar uma tarefa específica como concluída
# Usamos next() com generator expression para buscar a tarefa pelo ID
# -----------------------------------------------------------------------------
def concluir_tarefa(tarefas, id_tarefa):
    # next() retorna o primeiro item que satisfaz a condição, ou None
    tarefa = next((t for t in tarefas if t["id"] == id_tarefa), None)

    if tarefa is None:           # Se não encontrou nenhuma tarefa com esse ID
        print(f"❌ Tarefa #{id_tarefa} não encontrada.")
        return

    if tarefa["concluida"]:      # Se já estava concluída
        print(f"ℹ️  Tarefa #{id_tarefa} já estava concluída.")
        return

    tarefa["concluida"] = True   # Marca como concluída
    salvar_tarefas(tarefas)      # Salva a alteração
    print(f"🎉 Tarefa #{id_tarefa} marcada como concluída!")


# -----------------------------------------------------------------------------
# FUNÇÃO: remover_tarefa(tarefas, id_tarefa)
# Objetivo: deletar uma tarefa da lista pelo seu ID
# Usamos list comprehension para criar uma nova lista SEM a tarefa removida
# -----------------------------------------------------------------------------
def remover_tarefa(tarefas, id_tarefa):
    tamanho_original = len(tarefas)

    # List comprehension: mantém só as tarefas cujo id é DIFERENTE do buscado
    tarefas[:] = [t for t in tarefas if t["id"] != id_tarefa]

    if len(tarefas) == tamanho_original:   # Se o tamanho não mudou, não achou
        print(f"❌ Tarefa #{id_tarefa} não encontrada.")
    else:
        salvar_tarefas(tarefas)
        print(f"🗑️  Tarefa #{id_tarefa} removida com sucesso.")


# -----------------------------------------------------------------------------
# FUNÇÃO: exibir_menu()
# Objetivo: mostrar as opções disponíveis para o usuário
# Separamos isso em uma função para não repetir código no loop principal
# -----------------------------------------------------------------------------
def exibir_menu():
    print("\n" + "=" * 40)
    print("       GERENCIADOR DE TAREFAS")
    print("=" * 40)
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")
    print("=" * 40)


# -----------------------------------------------------------------------------
# BLOCO PRINCIPAL: if __name__ == "__main__"
# Esse bloco só roda quando executamos este arquivo diretamente
# Se outro arquivo importar este módulo, o bloco NÃO executa automaticamente
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    tarefas = carregar_tarefas()  # Carrega as tarefas salvas (ou lista vazia)

    # Loop principal do programa — roda até o usuário digitar 0
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()  # .strip() remove espaços extras

        if opcao == "1":
            listar_tarefas(tarefas)

        elif opcao == "2":
            descricao = input("Descrição da tarefa: ").strip()
            if descricao:                    # Só adiciona se não estiver vazio
                adicionar_tarefa(tarefas, descricao)
            else:
                print("⚠️  A descrição não pode estar vazia.")

        elif opcao == "3":
            listar_tarefas(tarefas)
            try:
                id_tarefa = int(input("ID da tarefa a concluir: "))
                concluir_tarefa(tarefas, id_tarefa)
            except ValueError:               # Se o usuário digitar algo que não é número
                print("⚠️  Digite um número válido.")

        elif opcao == "4":
            listar_tarefas(tarefas)
            try:
                id_tarefa = int(input("ID da tarefa a remover: "))
                remover_tarefa(tarefas, id_tarefa)
            except ValueError:
                print("⚠️  Digite um número válido.")

        elif opcao == "0":
            print("👋 Até logo!")
            break                            # Encerra o loop e o programa

        else:
            print("⚠️  Opção inválida. Tente novamente.")
