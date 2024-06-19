qtdprodmaismil = precoprodbarato = qtd = total = 0
nomeprodbarato = ''
while True:
    resposta = ''
    print('-=-'*22)
    nomeprod = str(input('Nome do produto: ')).strip().lower()
    preco = float(input('Preço: R$'))
    qtd += 1
    total += preco
    if preco > 1000:
        qtdprodmaismil += 1
    if qtd == 1 or preco < precoprodbarato:
        nomeprodbarato = nomeprod
        precoprodbarato = preco
    while resposta not in ('s', 'n'):
        resposta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resposta == 'n':
        break
print('-=-'*22)
print(f'O valor total da compra foi de R${total:.2f}.')
print(f'Você digitou {qtdprodmaismil} produtos acima de R$1000.00.')
print(f'O nome do produto mais barato é {nomeprodbarato} por R${precoprodbarato:.2f}.')
print('-=-'*22)
