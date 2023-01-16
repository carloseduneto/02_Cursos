def removerAspas(texto):
    texto= texto.replace("'", "")
    if texto[0]=="b":
        texto= texto[1:]
    return texto