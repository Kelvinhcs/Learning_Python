n = int(input('Digite o n-ésimo termo para ser mostrado: '))
ultimo = 1
penultimo = 0
cont = 1
while cont <= n:
    if cont == 1:
        print(penultimo, end=' ')
        cont += 1
    elif cont == 2:
        print(ultimo, end=' ')
        cont += 1
    else:
        proximo = ultimo + penultimo
        penultimo = ultimo
        ultimo = proximo
        print(proximo, end=' ')
        cont += 1
print('Fim')


# 0 - 1 - 1 - 2 - 3 - 5
#         X
