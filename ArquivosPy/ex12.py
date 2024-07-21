print("Bem-Vindo ao calculador de descontos")
p = float(input("Digite o preço do produto: "))
desconto = ((5*p)/100)
pf = p-desconto
print("Originalmente o produto custava R${:.2f}\nMas com o nosso desconto de 5% ele sairá por R${:.2f}".format(p,pf))