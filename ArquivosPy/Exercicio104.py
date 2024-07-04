def leiaint(msg):
    while True:
        n = input(msg)
        if n.isdigit() or n[0] == ' ' and n[1:].isdigit():
            return int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        
    
numero = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {numero}')