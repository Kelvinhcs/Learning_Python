frase = str(input('Digite uma frase: ')).strip().upper()  # le a frase, remove espaços antes e depois e já coloca tudo em caixa alta
palavras = frase.split()  # separa cada palavra
junto = ''.join(palavras)  # junta todas as palavras sem espaços
inverso = ''  # variavel vazia

# basicamente um contador que vai ler o tamanho total da variavel "junto" e começar no final (-1 por python começar com 0)
# e termina no primeiro número da string (-1 por python começar com 0 em strings e ignorar o ultimo número neste caso)
# contando de trás pra frente

for letra in range(len(junto) - 1, -1, -1):
    # é o equivalente a pegar o número do contador, "letra"
    # e armazenar na variavél "inverso"
    # o caracter que estiver neste número da variavel "junto"
    # leia-se como:
    # armazene nesta, ela mesma mais, da variavel junto[o caracter que estiver nesta posição]
    #     inverso          +=             junto        [                letra               ]

    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!!')
else:
    print('A frase digitada NÃO é um palíndromo!!')