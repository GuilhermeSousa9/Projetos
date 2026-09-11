tarefas = []

while True:
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            print("\nSuas tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

            numero = int(input("Digite o número da tarefa que deseja remover: "))

            if 1 <= numero <= len(tarefas):
                removida = tarefas.pop(numero - 1)
                print(f"Tarefa '{removida}' removida!")
            else:
                print("Número inválido.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")