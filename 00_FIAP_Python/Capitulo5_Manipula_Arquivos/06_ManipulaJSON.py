import json
import os
if os.path.exists("07_Invetario_Jason.json"):
    with open("0")
inventario={}
opcao=int(input("Digite: "
                "\n<1> para registrar ativo"
                "\n<2> para exibir ativos armazenados"
                "\n>>"))

while opcao>0 and opcao<3:
    if opcao==1:
        resp="S"
        while resp=="S":
            inventario[input("Digite o número patrimonial: ")]=[
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp=input("Digite <S> para continuar: ").upper()
        with open("07_Invetario_Jason.json", "w") as aquivoJason:
            json.dump(inventario, aquivoJason)
        print("JASON gerado!!!")
    elif opcao==2:
        for chave, dado in inventario.items():
            print("Data.........:", dado[0])
            print("Descrição....:", dado[1])
            print("Departamento.:", dado[2])
    opcao = int(input("Digite: "
                      "\n<1> para registrar ativo"
                      "\n<2> para exibir ativos armazenados"
                      "\n>>"))
