"""Pode usar localhost no lugar de servidor"""
from socket import *

servidor="127.0.0.1"
porta=43210
object_socket = socket(AF_INET, SOCK_STREAM)
object_socket.bind((servidor, porta))
object_socket.listen(2)

print("Aguardando cliente...")
while True:
    con, cliente = object_socket.accept()
    print("Conectando com: ", cliente)
    while True:
        mensagemRecebida = str(con.recv(1024))
        print("Recebemos: ", mensagemRecebida)
        mensagemRecebida = b"Olah Cliente!"
        con.send(mensagemRecebida)
        break
    con.close()