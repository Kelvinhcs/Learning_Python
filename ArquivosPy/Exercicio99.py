def maior(*inteiros):
    print('-=-'*17)
    print(f'Tendo como base os valores: ',end='')
    for tiradapohadatupla in inteiros:
        for posicao,valoresunicos in enumerate(tiradapohadatupla):
            if posicao == 0:
                maior = valoresunicos
            else:
                if valoresunicos > maior:
                    maior = valoresunicos
            print(f'{valoresunicos} ', end='')
        print()
        print(f'Possuimos um total de {len(tiradapohadatupla)} valores.')
    print(f'O maior valor é {maior}.')
 
lista1 = [23, 47, 72, 19, 5, 93, 14, 65]
lista2 = [86, 33, 57, 99, 20, 68, 42]
lista3 = [91, 13, 70, 6]
lista4 = [0]
lista5 = [39, 56, 88, 32, 10, 71, 18, 67, 93]

maior(lista1)
maior(lista2)
maior(lista3)
maior(lista4)
maior(lista5)
print('-=-'*17)
