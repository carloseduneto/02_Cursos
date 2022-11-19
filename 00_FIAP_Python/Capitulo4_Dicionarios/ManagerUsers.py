from Capitulo4_Dicionarios.Funcoes import *
usuario={}
opcaoEscolhida = ""

while opcaoEscolhida!="S":
    menu()
    opcaoEscolhida = input(">>").upper()
    if opcaoEscolhida=="I":
        insercao(usuario)
    if opcaoEscolhida== "E":
        excluir(usuario)
    if opcaoEscolhida=="L":
        listar(usuario)
    if opcaoEscolhida=="P":
        pesquisar(usuario)











        #chave=input("Chave de acesso: ")
        #nome=input("Nome de cadastro: ")
        #dataDeAcesso=input("Data de acesso: ")
        #Localizacao=input("Local de acesso: ")
        #usuario[chave]=[nome,dataDeAcesso,Localizacao]