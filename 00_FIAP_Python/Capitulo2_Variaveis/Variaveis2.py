evento=input('Nome do evento: ')
responsavel=input('Nome do responsável: ')
nome=input('Nome da pessoa que compareceu ao ' + evento +': ')
gastos=float(input(f"Gastos de {nome} em {evento}: R$"))
print(f"Declaro para o senhor {responsavel} que o (a) senhor(a)" + nome + "esteve no evento", evento, ' e gastou o valor de R$'+ str(gastos) + ' com a entrada')