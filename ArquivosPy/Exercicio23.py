#Isso foi completamente copiado do guanabara
# SE ELE ESPERA QUE EU SAIBA QUE O MÓDULO/RESTO DA DIVISAO POR 10 É A DEZENA ELE TA LOUCO
n = int(input("Digite um número inteiro de 0 a 9999: "))
m = n // 1000 % 10
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
print("Milhar {}".format(m))
print("Centena {}".format(c))
print("Dezena {}".format(d))
print("Unidade {}".format(u))

"""n = str(input("Digite um número inteiro de 0 a 9999: "))
print("Milhar {}".format(n[0]))
print("Centena {}".format(n[1]))
print("Dezena {}".format(n[2]))
print("Unidade {}".format(n[3]))"""

