from random import randint
lista = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os números gerados foram {lista}')
print(f'O menor número é {sorted(lista)[0]}')
print(f'O maior número é {sorted(lista, reverse=True)[0]}')
