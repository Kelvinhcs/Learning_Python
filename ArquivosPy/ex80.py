listagem = list()
for contador in range(0,5):
    digitado = int(input('Digite um valor: '))
    if contador == 0 or digitado > listagem[-1]:
        listagem.append(digitado)
        print(listagem)
        print('Valor adicionado na ultima posição')
    else:
        for c in range(len(listagem)):
            if digitado < listagem[c]:
                listagem.insert(c, digitado)
                print(listagem)
                break
print(f'A lista digitada organizada é {listagem}')
