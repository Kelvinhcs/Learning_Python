from random import randint
from time import sleep
print(f'{" Jogue Na Mega Sena ":-^54}')
placeholder = []
TodosOsJogos = []
quantidadejogos = int(input('Quantos jogos você quer que eu sorteie? '))
for TotalJogos in range (0,quantidadejogos):
    placeholder.clear()
    for NumerosDaJogada in range(0, 6):
        gerado = randint(1,60)
        if gerado in placeholder:
            while gerado in placeholder:
                gerado = randint(1,60)
        placeholder.append(gerado)
    TodosOsJogos.append(placeholder[:])
print(f'{f" Gerando {quantidadejogos} novos jogos ":=^54}')
for NumeroDaJogada, Jogada in enumerate(TodosOsJogos):
    sleep(1.5)
    print(f'{NumeroDaJogada+1}ª Jogo: {Jogada}')
print(f'{" Boa Sorte! ":=^54}')
