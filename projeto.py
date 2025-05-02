lista_de_tarefas = list()
continuar = True
while continuar :
    print("Escolha uma opção:\n"\
                "1 - inserir nova tarefa\n" \
                "2 - Listar tarefas\n" \
                "3 -Sair"
    )
    opcao = input ("insira o que deseja fazer: ")
    if opcao == "1":

        tarefa = input('insira uma nova tarefa: ')
        lista_de_tarefas.append(tarefa)

    elif opcao == "2":
        print(lista_de_tarefas)

    elif opcao =="3":
        continuar = False
    else:
        print("Opção inválida. Tente novamente.")
    print('\n')
    