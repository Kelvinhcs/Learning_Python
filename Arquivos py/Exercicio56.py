somatotal = 0
idadehomemvelho = 0
nomehomemvelho = ''
femmenosvinte = 0
for c in range(1, 5):
    print(f'-=-=-=-=-=-=-=-=-=- {c}ª  Pessoa -=-=-=--=-=-=-=-=-=-')
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite o seu genero(m/f): ')).strip().lower()
    if sexo not in ('m', 'f'):
        print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print('Opção inválida...')
        print('Resposta Desconsiderada...')
        if c == 4:
            print('Calculando respostas...')
        else:
            print(f'Passando para a {c+1}º resposta...')
    else:
        somatotal += idade
        if sexo == 'm':
            if idade > idadehomemvelho or c == 1:
                idadehomemvelho = idade
                nomehomemvelho = nome
        if sexo == 'f' and idade < 20:
            femmenosvinte += 1
media = somatotal / 4
print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'A média das idades informadas foi de {media:.1f}.')
print(f'O nome do homem mais velho é {nomehomemvelho} com {idadehomemvelho}.')
print(f'A quantidade de mulheres abaixo dos 20 é de {femmenosvinte}.')
print(f'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


