#Escreva um programa que converta uma temperatura digitada em °C em °F.
# A fórmula para conversão é( F = 9 x C / 5 ) + 32.


c = int(input("Digite a temperatura: "))

f = (c*9/5) + 32

print ("Temperatura convertida: {} ".format(f))
