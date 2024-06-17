termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
print(termo, end=' ♦ ')
pa = termo
c = 1
resposta = 1
while resposta != 0:
    while c < 10:
        c += 1
        pa += razao
        print(pa, end=' ♦ ')
    print('Pausa')
    resposta = int(input('\nDeseja mostrar mais quantos números?: '))
    for contador in range(0, resposta):
        c += 1
        pa += razao
        print(pa, end=' ♦ ')
print(f'Progressão finalizada com {c} termos mostrados.')
