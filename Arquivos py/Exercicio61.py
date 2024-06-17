termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
print(termo, end=' ♦ ')
pa = termo
c = 1
while c < 10:
    c += 1
    pa += razao
    print(pa, end=' ♦ ')
print('Fim')
