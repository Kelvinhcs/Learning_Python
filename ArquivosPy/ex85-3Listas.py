listagem = list()
phpar = list()
phimpar = list()
for contador in range(0, 7):
    numero = int(input(f'Digite o {contador}º valor: '))
    if numero % 2 == 0:
        phpar.append(numero)
    else:
        phimpar.append(numero)
phpar.sort()
phimpar.sort()
listagem.append(phpar)
listagem.append(phimpar)
print(listagem)
