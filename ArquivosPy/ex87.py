#inicialização das variaveis utilizadas posteriormente
Matriz = [[[],[],[]], [[],[],[]], [[], [], []]]
SomaTotal = SomaTerceiraColuna = SomaPares = 0

#incluindo itens na matriz 3x3
for Linha in range(0, 3):
    for Coluna in range(0,3):
        digitado = int(input(f'Digite um valor para a {Linha+1}ª linha na {Coluna+1}ª posição: '))
        Matriz[Linha][Coluna].append(digitado)
        SomaTotal += digitado
        if digitado % 2 == 0:
            SomaPares += digitado
            
#imprimindo a matriz         
print('-=-'*19)
for Linha in Matriz:
    for NumeroUnico in Linha:
        print(NumeroUnico, end='')
    print()
print('-=-'*19)

#calculo da soma dos valores na terceira coluna
TerceiraColuna = Matriz[0][2]+Matriz[1][2]+Matriz[2][2] #separa a terceira coluna em uma lista nova
for NumerosSeparados in TerceiraColuna: #retira da lista e soma
    SomaTerceiraColuna += NumerosSeparados
    
#encontrando o maior valor da segunda linha
for SegundaLinha in Matriz[1]:  #separa a segunda linha da Matriz
    for Posicao, Numero in enumerate(SegundaLinha): #separa a posicao e o numero nas variáveis de mesmo nome
        if Posicao == 0 or Numero > maioritem:
            maioritem = Numero
            
#impresao dos dados solicitados 
print(f'A soma de todos os valores digitados é de {SomaTotal}.')
print(f'A soma de todos os valores pares é de {SomaPares}.')
print(f'A soma dos valores da terceira coluna é {SomaTerceiraColuna}')
print(f'O maior valor da segunda linha é {maioritem}.')
