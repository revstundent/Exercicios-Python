#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

dist = float(input("distancia em km: "))
velo = float(input("digite a velocidade media: "))

tempo = dist / velo

print ("Tempo em horas {:.1f}".format(tempo))


