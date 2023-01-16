from socket import *

servidor="127.0.0.1"
porta=43210
objetoSocket = socket(AF_INET, SOCK_DGRAM)
objetoSocket.bind((servidor, porta))
print("Servidor pronto.......")
while True:
    dados, origem = objetoSocket.recvfrom(65535)
    print("Origem...............: ", origem)
    print("Dados recebidos......: ", dados.decode())
    resposta=input("Digite a resposta: ")
    objetoSocket.sendto(resposta.encode(), origem)
objetoSocket.close()