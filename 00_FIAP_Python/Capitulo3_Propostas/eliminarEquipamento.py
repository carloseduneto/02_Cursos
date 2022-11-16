from random import randint as rd

numeroSerial=[]

for indice in range(int(input("Quantos são os equipamentos?"))):
    numeroSerial.append(rd(000000,999999))

for indice in numeroSerial:
    print(indice)

eliminar=int(input("Qual número serial deseja eliminar?"))

for indice in range(len(numeroSerial)):
    if eliminar== numeroSerial[indice]:
        del numeroSerial[indice]
        print("✅Número serial deletado com sucesso ")
        break

for indice in numeroSerial:
    print(indice)

        



