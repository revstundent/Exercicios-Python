#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

m = float(input('escreva a distancia em metros: '))
cm = m * 100
mm = m * 1000

print ("{} metros corresponde a {} centimetros e {} milimetros".format(m, cm, mm))
