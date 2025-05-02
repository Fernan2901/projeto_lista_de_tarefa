def adicionar_tarefa(lista_de_tarefas, tarefa):
    #adiciona
    lista_de_tarefas.append(tarefa)
    print(f"{'*' * 15}Tarefa adicionada com sucesso.")
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    #exibe
    n = 1
    print("\n")
    print("-" * 50)
    print(f"{' ' * 15}Lista de Tarefas")
    print("-" * 50)
    for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n += 1

def deletar_tarefa(lista_de_tarefas, tarefa):
    #deleta
    lista_de_tarefas.pop(int(tarefa -1))
    return lista_de_tarefas

def exibir_menu():
     #exibe
     print("-" * 50)
     print("Escolha uma opção:\n"\
                "1 - inserir nova tarefa\n" \
                "2 - Listar tarefas\n" \
                "3 - Deletar tarefa\n" \
                "4 - Sair") 
     print("-" * 50)

#inicialização
lista_de_tarefas = list()
continuar = True

#cabeçalho
print("-" * 50)
print("Bem-vindo(a) à sua Lista de Tarefas.")
print("-" * 50)

#loop principal
while continuar :
    exibir_menu()
    opcao = input ("insira o que deseja fazer: ")

    if opcao == "1":
        tarefa = input('insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == "2":
       listar_tarefas(lista_de_tarefas)
    
    elif opcao == "3":
        #validação
        tarefa = input("Insira o número da tarefa que deseja deletar: ")
        if not tarefa.isnumeric():
            print("Inválido. Tente novamente.")
        elif int(tarefa) > len(lista_de_tarefas):
            print("Número inválido. Tente novamente.")
        elif int(tarefa) <= 0:
            print("Número inválido! Tente novamente.")
        else:
            tarefa = int(tarefa)
        deletar_tarefa(lista_de_tarefas, int(tarefa))
    elif opcao =="4":
        continuar = False
    else:
        print("Opção inválida. Tente novamente.")
    print('\n')
    
