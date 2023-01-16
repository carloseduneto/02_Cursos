from socket import *
from Capitulo99_Funcoes.Remover import *

servidor = "127.0.0.1"
porta = 53210
mensagem=""
while mensagem!= "SAIR":
    mensagem= bytes(input("Digite algo: "), "utf-8")
    objetoSocket=socket(AF_INET, SOCK_STREAM)
    objetoSocket.connect((servidor, porta))
    objetoSocket.send(mensagem)
    resposta=objetoSocket.recv(1024)
    resposta=str(resposta)
    resposta = removerAspas(resposta)
    print("Servidor: ", resposta)
    objetoSocket.close()