import random
print("Porque toda vez é sempre assim?")
a = str(input("Digite o nome do primeiro aluno: "))
b = str(input("Digite o nome do segundo aluno: "))
c = str(input("Digite o nome do terceiro aluno: "))
d = str(input("Digite o nome do quarto aluno: "))
l = [a,b,c,d]
print("O escolhido foi {}".format(random.choice(l)))
