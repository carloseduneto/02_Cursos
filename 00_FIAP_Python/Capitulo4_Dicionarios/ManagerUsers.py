def menu():
    print("O que você deseja fazer?")
    print("<I> Inserir \n<E> Excluir \n<L> Listar \n<S> Sair")

usuario={}
menu()
opcaoEscolhida = input(">>").upper()

while opcaoEscolhida!="S":
    if opcaoEscolhida=="I":
        chave=input("Chave de acesso: ")
        nome=input("Nome de cadastro: ")
        dataDeAcesso=input("Data de acesso: ")
        Localizacao=input("Local de acesso: ")
        usuario[chave]=[nome,dataDeAcesso,Localizacao]
        print(f"{nome} adionado com sucesso ✅ {usuario.get(chave)}\n")
        menu()
        opcaoEscolhida=input(">>")