maisdezoite = homens = mulheresmenosvinte = 0
while True:
    genero = resposta = ''
    print('-=-'*24)
    idade = int(input('Digite a idade desta pessoa: '))
    while genero not in ('m', 'f'):
        genero = str(input('Selecione o gênero: [M/F] ')).strip().lower()[0]
    if idade >= 18:
        maisdezoite += 1
    if genero == 'm':
        homens += 1
    if genero == 'f' and idade < 20:
        mulheresmenosvinte += 1
    while resposta not in ('s', 'n'):
        resposta = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
    if resposta == 'n':
        break
print('-=-'*24)
print(f'Foi cadastrado {maisdezoite} maiores de idade.')
print(f'Foi cadastrado {homens} pessoas que se identificam com o gênero masculino.')
print(f'Foi cadastrado {mulheresmenosvinte} mulheres com menos de 20 anos.')
print('-=-'*24)
