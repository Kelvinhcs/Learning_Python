def contador(start, end, step):
    if step == 0:
        step = 1
    if step < 0:
        step = abs(step)
    print('-'*40)
    print(f'Contagem de {start} até {end} de {step} em {step}.')
    if start < end:
        print(f'{start} ', end='')
        while start < end:
            start += step
            if start > end:
                break
            else:
                print(f'{start} ', end='')
        print('Fim!')
    elif start > end:
        print(f'{start} ', end='')
        while start > end:
            start -= step
            if start < end:
                break
            else:
                print(f'{start} ', end='')
        print('Fim!')
    print('-'*40)
 
 
inicio = int(input('Começo: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
