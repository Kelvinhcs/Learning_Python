from random import randint
from time import sleep
TodosOsJogos = []

print(f'{" Jogue Na Mega Sena ":-^54}') #embelezamento
QuantidadeDeJogos = int(input('Quantos jogos você quer que eu sorteie? '))

#Começa um loop que ira funcionar com base no valor escolhido pelo usuário
for VariavelSemUtilidade in range(0,QuantidadeDeJogos):
    placeholder = []
    for NumerosDaJogada in range(0, 6): #Rodará 6 vezes 
        Gerado = randint(1,60) #Gerará numeros válidos de 1 até 60, abaixo garante que nao serão repetidos
        if Gerado in placeholder:
            while Gerado in placeholder:
                Gerado = randint(1,60) 
        placeholder.append(Gerado)
    TodosOsJogos.append(placeholder[:])

#Printando os Jogos na tela  
print(f'{f" Gerando {QuantidadeDeJogos} novos jogos ":=^54}')
for NumeroDaJogada, Jogada in enumerate(TodosOsJogos):
    sleep(1.5)
    print(f'{NumeroDaJogada+1}º Jogo: {sorted(Jogada)}')
print(f'{" Boa Sorte! ":=^54}')
