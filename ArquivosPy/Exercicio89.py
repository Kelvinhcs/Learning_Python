ListaGeral = []
contador = 0
print('-=-'*11)
while True:
    resposta = ''
    NomeDigitado = str(input('Nome do aluno: ')).strip()
    Notas = [float(input(f'Digite a 1ª nota: ')), float(input(f'Digite a 2ª nota: '))]
    ListaGeral.append(list('nada'))
    ListaGeral[contador].clear()
    ListaGeral[contador].append(NomeDigitado[:])
    ListaGeral[contador].append(Notas[:])
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
print('Encerando...')
print('-=-'*11)
