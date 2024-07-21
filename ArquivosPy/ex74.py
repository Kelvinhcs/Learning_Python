from random import randint
tupla = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os números gerados foram {tupla}.')
print(f'O menor número (sorted) é {sorted(tupla)[0]}.')
print(f'O menor valor ( min() ) é {min(tupla)}.')
print('-=-'*20)
print(f'O maior número (sorted com reverse=True) é {sorted(tupla, reverse=True)[0]}.')
print(f'O maior número (sorted apresentando o último valor) é {sorted(tupla)[-1]}.')
print(f'O maior valor ( max() ) é {max(tupla)}')
