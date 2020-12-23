#Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.


m1 = float(input("qual sua primeira nota: "))
m2 = float(input("qual sua segunda nota: "))
m3 = float(input("qual sua terceira nota: "))

media = (m1 + m2 + m3) / 3

if media < 7:
    print ("reprovado")

elif media< 10:
    print ("aprovado")
else:
    print ("aprovado com distinção!")
