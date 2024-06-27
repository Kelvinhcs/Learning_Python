ListaGeral = []
contador = 0
print('-=-'*11)

while True:
    #cria/reinicia a variavel resposta, depois le o nome e 2 notas armazenando em listas separadas
    resposta = ''
    NomeDigitado = [str(input('Nome do aluno: ')).strip()]
    Notas = [float(input(f'Digite a 1ª nota: ')), float(input(f'Digite a 2ª nota: '))]
    
    #adiciona a lista NomeDigitado e dentro dela a outra lista Notas
    #ocasionando na ListaGeral: [['Pedro',[9.5, 5.2]], ['Kelvin', [6.2, 5.0]], ['MatGx'[10.0, 5.0]]]
    ListaGeral.append(NomeDigitado[:])
    ListaGeral[contador].append(Notas[:])
    contador += 1
    
    #codigo padrão de validação de resposta 
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
    print('-=-'*11)
    if resposta == 'n':
        break
    
#começa o esquema de printar os dados separados
print('Nº | Nome Do Aluno | Média')
#separa o numero do item, e uma lista maior com nome e dentro dela a outra lista com as notas
for Indice, DadosDoAluno in enumerate(ListaGeral):
    media = soma = 0
    for NotaIndividual in DadosDoAluno[1]: #Separa as notas individuais da lista com as 2 notas               
        soma += NotaIndividual
    media = soma / 2
    print(f'{Indice+1:<2} -> {DadosDoAluno[0]:^13} -> {media}')
print('-=-'*11)

while True:
    escolha = int(input('Digite o número do aluno para mostrar suas notas individuais [999 Interompe]: '))
    if escolha == 999:
        break
    #imprime a lista com as notas do aluno escolhido
    print(f'As notas individuais do aluno {ListaGeral[escolha-1][0]} foram {ListaGeral[escolha-1][1]}.')
    print('-=-'*11)
    
print('Encerando...')
print('-=-'*11)