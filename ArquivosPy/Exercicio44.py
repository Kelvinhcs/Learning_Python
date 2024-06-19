from time import sleep
precooriginal = float(input('Digite o preço atual do produto: '))
print('-=-'*20)
print('[1] à vista dinheiro/cheque\n[2] à vista no cartão')
print('[3] em até 2x no cartão\n[4] 3x ou mais no cartão')
pagamento = int(input('Digite a opção desejada: '))
print('-=-'*20)
if pagamento != 1 and pagamento != 2 and pagamento != 3 and pagamento != 4:
    print('Método de pagamento INVÁLIDO.')
else:
    if pagamento == 1:
        desconto = (precooriginal*10)/100
        print(f'O preço de seu produto é de R${precooriginal-desconto:.2f}.')
        print(f'Foi aplicado um desconto de {desconto:.2f}, 10% do valor original.')
    elif pagamento == 2:
        desconto = (precooriginal*5)/100
        print(f'O preço de seu produto é de R${precooriginal-desconto:.2f}.')
        print(f'Foi aplicado um desconto de R${desconto:.2f}, 5% do valor original.')
    elif pagamento == 3:
        parcela = precooriginal / 2
        print(f'O preço total do seu produto é de R${precooriginal}\nNão foram aplicados descontos ou juros.')
        print(f'Você terá que pagar R${parcela:.2f} em 2 parcelas.')
    elif pagamento == 4:
        quantidade = int(input('Em quantas parcelas você gostaria de pagar.(Máximo de 12):'))
        if quantidade not in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
            print('Quantidade de parcelas inválidas.')
        else:
            parcela = precooriginal / quantidade
            juros = (precooriginal*20)/100
            print(f'O preço total de seu produto é de R${precooriginal+juros:.2f}.')
            print(f'Foi aplicado um juros de R${juros:.2f}, 20% do valor original.')
            print(f'Você terá que pagar R${parcela:.2f} em {quantidade} parcelas.')
print('-=-'*20)
sleep(1)
print('Desligando sistema...')
sleep(2)
