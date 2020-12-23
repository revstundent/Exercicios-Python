#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00 .

salario = int(input("qual seu salario?: "))
minimo = 1200
if salario >= minimo:
    print ("voce precisa pagar o imposto!")
else:
    print ("nao precisa pagar imposto!")
