combustível = 100
tripulantes = []

#Definição das Funções
def viajar():
    global combustível
    if(combustível >= 30):
        combustível = combustível - 30 ## ----> Gastar combustível
        print("\nA Nave Viajou!!🚀🚀")
    else:
       print("\nVocê está sem Combustível Suficiente⛽❌. Abasteça!!🚨") 
    

def abastecer():
    global combustível
    combustível = 100 
    print("\nTanque Abastecido!⛽")

def status_nave():
    print("\n-------- STATUS DE NAVE --------")
    print(f"Temos {combustível} de Combustível")
    print(f"Os Tripulantes são {tripulantes}")
    print("-" * 32 + "\n")

def registrar_tripulante():
    novo_tripulante = input("Qual o nome do Tripulante?: ")
    tripulantes.append(novo_tripulante)
    print("Tripulante Inserido com Sucesso!!🧑‍🚀🪪")

def suprimir_tripulante():
    if len(tripulantes) == 0:
        print("Não há Tripulantes para remover!!")
        print("Adicione um Tripulante para prosseguir...")
    else:
        ## tripulante_removido = input("Qual o nome do Tripulante que quer retirar?: ") 
        ## tripulantes.remove(tripulante_removido)
        tripulantes.pop()
        print("Tripulante Removido com Sucesso!!🧑‍🚀🪪")
        print(f"Os Tripulantes presentes na Nave são: {tripulantes}")

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
    elif(opção == "¨6"):
        print("Viagem Encerrada!")
        break 
