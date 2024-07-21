###encontrei a opção de gerar uma lista vazia antes e apagala para assim poder utilizar o indice
ListaGeral = []
placeholder = []
contador = 0
print('-=-'*11)
while True:
    resposta = ''
    placeholder.clear()
    NomeDigitado = str(input('Nome do aluno: ')).strip()
    Nota1 = float(input(f'Digite a 1ª nota: '))
    Nota2 = float(input(f'Digite a 2ª nota: '))
    placeholder.append(Nota1)
    placeholder.append(Nota2)
    ListaGeral.append(list('nada'))
    ListaGeral[contador].clear()
    ListaGeral[contador].append(NomeDigitado)
    ListaGeral[contador].append(placeholder[:])
    contador += 1
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
    print('-=-'*11)
    if resposta == 'n':
        break
print('Nº | Nome Do Aluno | Média')
for numero, separacao in enumerate(ListaGeral):
    media = soma = 0
    for nota in separacao[1]:
        soma += nota
    media = soma / 2
    print(f'{numero+1:<2} -> {separacao[0]:^13} -> {media}')
print('-=-'*11)
while True:
    escolha = int(input('Digite o número do aluno para mostrar suas notas individuais [999 Interompe]: '))
    if escolha == 999:
        break
    print(f'As notas individuais do aluno {ListaGeral[escolha-1][0]} foram {ListaGeral[escolha-1][1]}.')
    print('-=-'*11)
print('ACABOU POHAAAAAAAAA')
