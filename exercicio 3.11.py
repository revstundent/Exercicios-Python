#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria = int(input('digite o valor: '))
porc = int(input('digite o numero de desconto: '))

novopreco = mercadoria - ((mercadoria * porc)/100)
desconto = mercadoria - novopreco

print ("Preço R$", novopreco)

print ("Desconto de R$", desconto)
