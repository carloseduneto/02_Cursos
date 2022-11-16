from random import randint

impressoras=[]
for i in range(int(input("Quantos são os produtos? "))):
    impressoras.append(randint(999,2999))

for indice in impressoras:
    print(f"Valor original: ",indice)    

for indice in range(len(impressoras)):
    impressoras[indice]=impressoras[indice]*0.9

for indice in impressoras:
    print(f"Valor com depreciação: ",indice)