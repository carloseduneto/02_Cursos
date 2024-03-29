import json
import os
def exibirMenu():
    opcao = int(input("Digite: "
                      "\n<1> para registrar ativo"
                      "\n<2> para exibir ativos armazenados"
                      "\n>>"))
    return opcao

def lerArquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arquivoJason:
            dicionario = json.load(arquivoJason)
    else:
        dicionario = {}
    return dicionario

def gravarArquivo(dicionario, arquivo):
    # with open(arquivo, "w") as arquivoJason:
    #     json.dump(dicionario, arquivoJason)
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)


def registrar (dicionario, arquivo):
    # resp = "S"
    # while resp == "S":
    #     dicionario=[input("Digite o número patrimonial: ")] = [
    #         input("Digite a data da última atualização: "),
    #         input("Digite a descrição: "),
    #         input("Digite o departamento: ")]
    #
    #     resp = input("Digite <S> para continuar: ").upper()
    #     gravarArquivo(dicionario, arquivo)
    # return "JASON gerado!!!"
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravarArquivo(dicionario, arquivo)
    return "JSON gerado!!!!"

def exibir(arquivo):
    dicionario=lerArquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........:", dado[0])
        print("Descrição....:", dado[1])
        print("Departamento.:", dado[2])