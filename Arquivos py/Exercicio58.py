from random import randint
pc = randint(0, 10)
qtd = 1
print('Acabei de pensar em um número... Será que você consegue adivinhar?')
print('Vou te dar uma dica, pode ser qualquer um de 0 a 10.')
resposta = int(input('Faça uma tentativa: '))
while resposta != pc:
    qtd += 1
    if pc > resposta:
        resposta = int(input('Um pouco mais... Tente outra vez:  '))
    elif pc < resposta:
        resposta = int(input('Um pouco menos... Tente outra vez:  '))
print(f'Parabéns Você acertou com {qtd} tentativas!!!')
print(f'O Computador pensou em {pc}.')
print(f'Você digitou {resposta}.')
