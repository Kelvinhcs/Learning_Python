from random import randint
lista = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os números gerados foram {lista}.')
print(f'O menor número (sorted) é {sorted(lista)[0]}.')
print(f'O menor valor (min() ) é {min(lista)}.')
print('-=-'*20)
print(f'O maior número (sorted com reverse=True) é {sorted(lista, reverse=True)[0]}.')
print(f'O maior número (sorted apresentando o último valor) é {sorted(lista)[-1]}.')
print(f'O maior valor (max() ) é {max(lista)}.')
