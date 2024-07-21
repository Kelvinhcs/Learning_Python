def MaiorLista(*inteiros):
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
 
def MaiorSeco(*inteiros):
    print('-=-'*17)
    print(f'Tendo como base os valores: ',end='')
    for posicao,valoresunicos in enumerate(inteiros):
        if posicao == 0:
            maior = valoresunicos
        else:
            if valoresunicos > maior:
                maior = valoresunicos
        print(f'{valoresunicos} ', end='')
    print()
    print(f'Possuimos um total de {len(inteiros)} valores.')
    print(f'O maior valor é {maior}.')
    
    
    
MaiorLista([39, 56, 88, 32, 10, 71, 18, 67, 93])
print('-=-'*17)
MaiorSeco(91, 13, 70, 6)
