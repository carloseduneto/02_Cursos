from socket import *

servidor = "127.0.0.1"
porta = 43210

mensagem= bytes(input("Digite algo: "), "utf-8")
objetoSocket=socket(AF_INET, SOCK_STREAM)
objetoSocket.connect((servidor, porta))
objetoSocket.send(mensagem)
resposta=objetoSocket.recv(1024)
print("Recebemos: ", resposta)
objetoSocket.close()