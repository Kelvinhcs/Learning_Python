from random import randint
pc = randint(0, 10)
print('Caixa de texto 1 explicando que o jogo vai de 0 a 10')
print('Caixa de texto 2 fazendo provocação engraçada')
resposta = False
qtd = 0
while not resposta:
    jogador = int(input('Qual o seu palpite? '))
    qtd += 1
    if jogador == pc:
        resposta = True
    else:
        if jogador < pc:
            print('Mais... Tente outra vez.')
        if jogador > pc:
            print('Menos... Tente outra vez.')
print(f'Acertou com {qtd} tentativas. Parabéns!')
