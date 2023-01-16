import getpass
from datetime import datetime

print("Usuário........: ", getpass.getuser())
print("Data completa..: ", datetime.now())
print("Dia............: ", datetime.now().day)
print("Mês............: ", datetime.now().month)
print("Ano............: ", datetime.now().year)
print("Hora...........: ", datetime.now().hour)
print("Minutos........: ", datetime.now().minute)
print("Segundos.......: ", datetime.now().second)

usuario=input("Digite o usuário: ").upper()
senha= input("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado")

