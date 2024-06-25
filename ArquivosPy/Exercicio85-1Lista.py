Listagem = [[], []]
print('-=-'*22)
for Contador in range(0, 7):
    NumeroDigitado = int(input(f'Digite o {Contador+1}º número: '))
    if NumeroDigitado % 2 == 0:
        Listagem[0].append(NumeroDigitado)
    else:
        Listagem[1].append(NumeroDigitado)
print('-=-'*22)
print(f'Os números pares são {sorted(Listagem[0])}.')
print(f'Os números ímpares são {sorted(Listagem[1])}.')

#Existe a possibilidade de utilizar o metodo "sorted()" ao inves de sortear a lista, Assim mantendo a lista original utilizando o sorted() no momento do print. Originalmente Utilizei listagem[0].sort() e listagem[1].sort()
