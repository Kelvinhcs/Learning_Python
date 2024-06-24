listagem = [[], []]
print('-=-'*22)
for contador in range(0, 7):
    numero = int(input(f'Digite o {contador+1}º número: '))
    if numero % 2 == 0:
        listagem[0].append(numero)
    else:
        listagem[1].append(numero)
print('-=-'*22)
listagem[0].sort() #Existe a possibilidade de utilizar o metodo "sorted()" ao inves de sortear a lista,
listagem[1].sort() #Assim mantendo a lista original utilizando o sorted() no momento do print.
print(f'Os números pares são {listagem[0]}.')
print(f'Os números ímpares são {listagem[1]}.')
