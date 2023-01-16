import socket

resposta = "S"
while (resposta=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("O IP referente à URL informada é: ", ip)
    resposta=input("Digite <S> para continuar: ").upper()