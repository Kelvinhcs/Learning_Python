#inicialização das variaveis utilizadas posteriormente
listagem = [[[],[],[]], [[],[],[]], [[], [], []]]
somatotal = somatc = somapares = 0
#incluindo itens na matriz 3x3
for principal in range(0, 3):
    for contador in range(0,3):
        digitado = int(input(f'Digite um valor para a {principal+1}ª linha na {contador+1}ª posição: '))
        listagem[principal][contador].append(digitado)
        somatotal += digitado
        if digitado % 2 == 0:
            somapares += 1
#imprimindo a matriz         
print('-=-'*19)
for item in listagem:
    for vezes, coisa in enumerate(item):
        print(coisa, end='')
    print()
print('-=-'*19)
#calculo da soma dos valores na terceira coluna
terceiracoluna = listagem[0][2]+listagem[1][2]+listagem[2][2] #separa a terceira coluna em uma lista nova
for item in terceiracoluna: #retira da lista e soma
    somatc += item
#encontrando o maior valor da segunda linha
for segundalinha in listagem[1]:  #separa a segunda linha da listagem
    for posicao, item in enumerate(segundalinha): #separa a posicao e o item nas variáveis de mesmo nome
        if posicao == 0 or item > maioritem: #encontra o maior valor
            maioritem = item
print(f'A soma de todos os valores digitados é de {somatotal}.')
print(f'A soma de todos os valores pares é de {somapares}.')
print(f'A soma dos valores da terceira coluna é {somatc}')
print(f'O maior valor da segunda linha é {maioritem}.')
