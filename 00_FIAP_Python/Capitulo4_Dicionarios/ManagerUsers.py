from Capitulo4_Dicionarios.Funcoes import *
usuario={}
opcaoEscolhida = ""

while opcaoEscolhida!="S":
    menu()
    opcaoEscolhida = input(">>").upper()
    if opcaoEscolhida=="I":
        #chave=input("Chave de acesso: ")
        #nome=input("Nome de cadastro: ")
        #dataDeAcesso=input("Data de acesso: ")
        #Localizacao=input("Local de acesso: ")
        #usuario[chave]=[nome,dataDeAcesso,Localizacao]
        insercao(usuario)
    if opcaoEscolhida== "E":
        chave=input("Digite a chave a ser excluída: ")
        del usuario [chave]
        print("✅ Usuário removido com sucesso!!!")
    if opcaoEscolhida=="L":
        for i in usuario:
            print(i)