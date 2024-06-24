galera = list()
dado = list()
totmai = totmen = 0
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade.')
        totmai += 1
    else:
        totmen += 1
        print(f'{pessoa[0]} não é maior de idade.')
print(f'Temos {totmai} maiores de idade.')
print(f'Temos {totmen} menores de idade.')