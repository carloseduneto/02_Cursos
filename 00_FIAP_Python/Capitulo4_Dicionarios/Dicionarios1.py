usuarios={}

usuarios={
    "Chaves":["Chaves Silva", "17/06/2017", "Recepcao_01"],
    "Quico":["Enrico Flores", "03/06/2017", "Raiox_02"]
}#Dois objetos com a mesma chave será sobrescrito pelo primeiro

usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recepcao_01"]
print(usuarios)
print("#"*15, "="*10, "#"*15)
print("Dados: ", usuarios.get("Florinda"))