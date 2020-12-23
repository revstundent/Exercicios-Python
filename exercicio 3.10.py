# Faça um prorama que calcule o aumento de um salário. Ele deve solicitar o alor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = int(input('digite seu salario: '))
perc = int(input('digit a porcentagem: '))

newsalario = salario + ((salario * perc)/100)
aumento = newsalario - salario

print ("Aumento de R$", aumento)
print ("Atual Salario R$", newsalario)
