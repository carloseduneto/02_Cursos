"""
Sempre usar o open()+with para o arquivo não ficar aberto na memória
"""

#pode definir o caminho aqui tbm, porém assim tá pegando da própia pasta
with open ("teste.txt", "w") as arquivo:
    arquivo.write("Sempre foi não tão difícil criar um arquivo (: .")


with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinua e acaba por aqui, aí vc que decide hehehehehehe")
