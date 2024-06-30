from time import sleep
def contador(start, end, step):
    if step == 0:
        step = 1
    if step < 0:
        step = abs(step)
    print('-'*40)
    print(f'Contagem de {start} até {end} de {step} em {step}.', flush=True)
    sleep(2)
    if start < end:
        while start <= end:
            print(f'{start} ', end='', flush=True)
            sleep(0.5)
            start += step
        print('Fim!')
    elif start > end:
        while start >= end:
            print(f'{start} ', end='', flush=True)
            start -= step
            sleep(0.5)
        print('Fim!')
    print('-'*40)
 
contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Começo: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
