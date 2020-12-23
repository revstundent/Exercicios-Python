# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# pelo usuario, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço apagar, sabendo que o custa R$ 60 por dia e R$ 0,15 por km rodado.


cada_km = 0.15
aluguel_carro = 60.0

km = int(input("digite uma quantidade de km: "))
dias_alugado = int(input("quantos dias de carro alugado: "))

preco_km = km * cada_km
preco_car = dias_alugado * aluguel_carro

print ("R${:5.2} - Preço por KM".format(preco_km))
print ("R$ {} - Preço do alguel do carro".format(preco_car))
