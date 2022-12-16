"""
Sempre usar o open()+with para o arquivo não ficar aberto na memória
"""

#pode definir o caminho aqui tbm, porém assim tá pegando da própia pasta
# with open ("teste.txt", "w") as arquivo:
#     arquivo.write("Sempre foi não tão difícil criar um arquivo (: .")
#
#
# with open("teste.txt", "a") as arquivo:
#     arquivo.write("\nContinua e acaba por aqui, aí vc que decide hehehehehehe")

with open("pagina.html", "w") as pagina:
    pagina.write("<body style='font-family: Arial, sans-serif;' align='center'> <h1>Isso daqui um teste de página "
                 "para WEB</h1>")
    pagina.write("<br><h2> Abaixo segue uns mones importantes para o projeto: ")
    pagina.write("<br><h3>")
    nome=""
    while nome!="Sair":
        nome= input("Digite um nome ou Sair: ").capitalize()
        if nome!="Sair":
            pagina.write("<br>"+nome)
        pagina.write("</h3></body>")
