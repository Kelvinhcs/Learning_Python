import moeda
digitado = float(input('Digite um o preço: R$'))
print(f'A metade de {moeda.moeda(digitado)} é {moeda.metade(digitado, form=True)}')
print(f'O dobro de {moeda.moeda(digitado)} é {moeda.dobro(digitado, form=True)}')
print(f'Aumentado 10% de {moeda.moeda(digitado)}, temos {moeda.aumentar(digitado, 10,form=True)}')
print(f'Diminuindo 13% de {moeda.moeda(digitado)}, temos {moeda.diminuir(digitado, 13, form=True)}')