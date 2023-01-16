"""Pode usar localhost no lugar de servidor"""
from socket import *
from Capitulo99_Funcoes.Remover import *

servidor="127.0.0.1"
porta=53210
object_socket = socket(AF_INET, SOCK_STREAM)
object_socket.bind((servidor, porta))
object_socket.listen(2)

print("Aguardando cliente...")
while True:
    con, cliente = object_socket.accept()
    print("Conectando com: ", cliente)
    while True:
        mensagemRecebida = str(con.recv(1024))
        mensagemRecebida=removerAspas(mensagemRecebida)
        print("Cliente: ", mensagemRecebida)
        if mensagemRecebida == 'Oi':
            mensagemRecebida = b"Oiii!"
            con.send(mensagemRecebida)
        if mensagemRecebida == 'Tudo bom?':
            mensagemRecebida = b"Tudo e com voceh?"
            con.send(mensagemRecebida)
        if mensagemRecebida == 'Tudo bem?':
            mensagemRecebida = b"Ah, que ohtimo!"
            con.send(mensagemRecebida)
        if mensagemRecebida == 'Tchau':
            mensagemRecebida = b"Ateh mais!"
            con.send(mensagemRecebida)
        break
    con.close()