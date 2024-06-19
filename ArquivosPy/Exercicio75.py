n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
lista = (n1,n2,n3,n4)
print(f'O número 9 apareceu {lista.count(9)} vez(es).' if lista.count(9) >= 1 else f'O número 9 Não apareceu nenhuma vez.')
print(f'O número 3 foi digitado na posição {lista.index(3)+1}.' if lista.index(3) >= 0 else f'O número 3 não foi digitado em nenhuma posição.')

#UNSOLVED
