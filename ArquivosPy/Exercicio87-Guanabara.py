#inicialização das variaveis utilizadas posteriormente
Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
SomaTotal = SomaTerceiraColuna = SomaPares = 0

#incluindo itens na matriz 3x3
for Linha in range(0, 3):
    for Coluna in range(0,3):
        Matriz[Linha][Coluna] = int(input(f'Digite um valor para a {Linha+1}ª linha na {Coluna+1}ª posição: '))
        if Matriz[Linha][Coluna] % 2 == 0:
            SomaPares += Matriz[Linha][Coluna]
        SomaTotal += Matriz[Linha][Coluna]
            
#imprimindo a matriz         
print('-=-'*19)
for Linha in Matriz:
    for NumeroUnico in Linha:
        print(f'[{NumeroUnico:^5}]', end='')
    print()
print('-=-'*19)

#calculo da soma dos valores na terceira coluna
for contador in range(0, 3):
   SomaTerceiraColuna += Matriz[contador][2] 
    
#encontrando o maior valor da segunda linha
for Posicao, Numero in enumerate(Matriz[1]): #separa a posicao e o numero nas variáveis de mesmo nome
    if Posicao == 0 or Numero > MaiorValorSegundaLinha:
        MaiorValorSegundaLinha = Numero

#impresao dos dados solicitados          
print(f'A soma de todos os valores digitados é de {SomaTotal}.')
print(f'A soma de todos os valores pares é de {SomaPares}.')
print(f'A soma dos valores da terceira coluna é {SomaTerceiraColuna}')
print(f'O maior valor da segunda linha é {MaiorValorSegundaLinha}.')
 