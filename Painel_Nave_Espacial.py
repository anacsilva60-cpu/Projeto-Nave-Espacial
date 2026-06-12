combustível = 100
tripulantes = []

#Definição das Funções
def viajar():
    global combustível
    if len(tripulantes) == 0:
        print("\n   Não é possível Viajar! Não há Tripulantes na Nave!")
        print("    Adicione Tripulantes para prosseguir com a Viagem...")

    else:
        if(combustível >= 30):
            combustível = combustível - 30 ## ----> Gastar combustível
            print("\n   A Nave Viajou!!🚀🚀")
        else:
            print("\nVocê está sem Combustível Suficiente⛽❌. Abasteça!!🚨") 
    travar_menu()

def abastecer():
    global combustível
    combustível = 100 
    print("\n   Tanque Abastecido!⛽")
    travar_menu()

def status_nave():
    print("\n-------- STATUS DE NAVE --------")
    print(f"Temos {combustível} de Combustível")
    print(f"Os Tripulantes são {tripulantes}")
    print("-" * 32 + "\n")
    travar_menu()

def registrar_tripulante():
    novo_tripulante = input("Qual o nome do Tripulante?: ")
    tripulantes.append(novo_tripulante)
    print("\n   Tripulante Inserido com Sucesso!!🧑‍🚀🪪")
    print(f"   Os Tripulantes presentes na Nave são: {tripulantes}")
    travar_menu()

def suprimir_tripulante():
    if len(tripulantes) == 0:
        print("\n   Não há Tripulantes para remover!!⚠️")
        print("     Adicione um Tripulante para prosseguir...")
    else:
        tripulante_removido = input("Qual o nome do Tripulante que quer retirar?: ") 
        tripulantes.remove(tripulante_removido)
        ## tripulantes.pop()
        print("\n   Tripulante Removido com Sucesso!!🧑‍🚀🪪")
        print(f"   Os Tripulantes presentes na Nave são: {tripulantes}")
    travar_menu()

def travar_menu():
    input("\nPrecione <ENTER> para continuar... ")

print("\n----> Bem Vindo ao Menu Interativo da Nave!🎛️ 🎚️  Por Favor, selecione uma opção: ")
while True: ## ----> Loop roda de sempre!!
    print("\n1- Mostrar Status da Nave | 2- Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Remover Tripulante | 6- Sair ")
    opção = input("Escolha: ")
    if(opção == "1"):
        status_nave()
    elif(opção == "2"):
        viajar()
    elif(opção == "3"):
        abastecer()
    elif(opção == "4"):
        registrar_tripulante()
    elif(opção == "5"):
        suprimir_tripulante()
    elif(opção == "6"):
        print("\n   Viagem Encerrada!")
        break 