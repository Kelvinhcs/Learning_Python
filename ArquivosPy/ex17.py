print("Bem Vindo ao simulador do inferno")
co = float(input("Digite o Valor do Cateto Oposto: "))
ca = float(input("Digite o Valor do Cateto Adjacente: "))
hi = (co**2 + ca**2) ** (1/2)
print("Valor da Hipotenusa é {:.2f}".format(hi))