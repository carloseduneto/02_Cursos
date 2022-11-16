from Capitulo3_Funcoes.IdentificacaoDeFuncoes import *
# o from recebe o local físico
# o import decide quais funções serão importadas (* asterísco importa tudo)

equipamentos=[]
valores=[]
numeroSeriais=[]
departamentos=[]
resposta="S"

while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numeroSeriais.append(int(input("Numero serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input("Digite 'S' para continuar: ").upper()

for indice in range (0, len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.........:", equipamentos[indice])
    print("Valor...........:", valores[indice])
    print("Serial..........:", numeroSeriais[indice])
    print("Departamneto.:", departamentos[indice])

busca=input("DIgite o nome do equipamento que deseja buscar: ")

for indice in range(0, len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor..:", valores[indice])
        print("Serial.:", numeroSeriais[indice])

        