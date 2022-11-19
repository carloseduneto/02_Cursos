def menu():
    print("O que você deseja fazer?")
    print("<I> Inserir \n<E> Excluir \n<L> Listar \n<S> Sair")


def insercao(dicionario):
    dicionario[input("Chave de acesso: ").upper()] = [input("Nome de cadastro: "),
                                               input("Data de acesso: "),
                                               input("Local de acesso: ")]
    print(f"Adicionado com sucesso ✅\n")