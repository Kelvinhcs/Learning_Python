print("Bem-Vindo ao nosso conversor de moedas")
r = float(input("Digite a quantidade que deseja converter: "))
d = r/4.93
print("Com o valor de {} reais você seria capaz de possuir\n{:.2f} Dólares\n{:.2f} Euros\n{:.2f} Libras\nDe acordo com a cotação do dia 20/02/2024\nRespectivamente de 4.93, 5.33, 6.22.".format(r,r/4.93,r/5.33,r/6.22))
