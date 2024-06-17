r = str(input('Digite seu gênero(m/f): ')).strip().lower()
while r not in ('m', 'f'):
    print('Opção inválida, digite novamente por favor: ')
    r = str(input('Digite seu gênero(m/f): ')).strip().lower()
if r == 'm':
    print(f'Gênero masculino registrado com sucesso.')
else:
    print(f'Gênero feminino registrado com sucesso. ')
print('Fim')
