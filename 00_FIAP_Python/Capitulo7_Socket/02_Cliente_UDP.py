from socket import *

servidor = "127.0.0.1"
porta = 43210

objetoSocket = socket(AF_INET, SOCK_DGRAM)
objetoSocket.connect((servidor, porta))
saida = ''
while saida!="X":
    mensagem = input("Sua mensagem: ")
    objetoSocket.sendto(mensagem.encode(), (servidor, porta))
    dados, origem = objetoSocket.recvfrom(65535)
    print("Resposta do Servidor: ", dados.decode())
    saida = input("Digite <X> para sair: ").upper()
objetoSocket.close()