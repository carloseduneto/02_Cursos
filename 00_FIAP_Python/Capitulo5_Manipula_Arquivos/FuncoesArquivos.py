def escolha ():
    opcao = int(input("Digite: "
                      "\n<1> para registrar ativo "
                      "\n<2> para persistir em arquivo"
                      "\n<3> para exibir ativos armazenados: "
                      ))
    return opcao

def registrar (dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp=input("Digite <S> para continuar.").upper()

def persistir (dicionario):
    with open("04.1_Inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2])

            print("Persisitido com sucesso!")

def mostrar():
    with open("04.1_Inventario.csv", "r") as inv:
        linhas=inv.readlines()
    return linhas