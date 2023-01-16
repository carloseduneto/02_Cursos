def menu():
    print("O que você deseja fazer?")
    print("<I> Inserir \n<E> Excluir \n<L> Listar \n<P> Pesquisar \n<S> Sair")


def insercao(dicionario):
    dicionario[input("Chave de acesso: ").upper()] = [input("Nome de cadastro: "),
                                               input("Data de acesso: "),
                                               input("Local de acesso: ")]
    print(f"Adicionado com sucesso ✅\n")

def pesquisar(dicionario):
    chave=input("Digite a chave a ser pesquisada: ").upper()
    if dicionario[chave]!=None:
        lista=dicionario.get(chave)
        print(f"✅Usuário encontrado: {dicionario[chave]} \n Último acesso: {lista[1]} \nÚltima localização: {lista[2]}")
    else:
        print(f"❌Usuário inválido")
def excluir(dicionario):
    chave = input("Digite a chave a ser excluída: ").upper()
    del dicionario[chave]
    print("✅ Usuário removido com sucesso!!!")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto: ")
        print("Login: ", chave)
        print("Dados: ", valor)