import math
print("Bem vindo a terra da solidão")
a = float(input("Digite o valor do ângulo: "))
print("Com Base no Ângulo {:.2f}\nO valor do seno é {:.2f}\nDo Cosseno é {:.2f}\nE da tangente é {:.2f}".format(a,math.sin(math.radians(a)),math.cos(math.radians(a)),math.tan(math.radians(a))))