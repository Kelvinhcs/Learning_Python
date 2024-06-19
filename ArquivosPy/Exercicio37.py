numero = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma das opções abaixo:\n[1] Converter para BINÁRIO\n[2] Converter para OCTAL\n[3] Converter para HEXADECIMAL\nSua opção: '))
print('-=-'*20)
if opcao == 1:
    print(f'Convertendo {numero} para BINÁRIO\nO Resultado é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'Convertendo {numero} para OCTAL\nO resultado é {oct(numero)[2:]} ')
elif opcao == 3:
    print(f'Convertendo {numero} para HEXADECIMAL\nO resultado é {hex(numero)[2:]}')
else:
    print('Você digitou uma opção INVALIDA.\nDesligando sistema...')