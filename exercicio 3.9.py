#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = input("Digite uma quantidade de dias: ")
horas = input("Digite uma quantidade de horas: ")
minutos = input("Digite uma quantidade de minutos: ")
segundos = input("Digite uma quantidade de segundos")

total_de_segundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print ("representa {} segundos.".format(total_de_segundos))

