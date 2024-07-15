def LeiaDinheiro(msg):
    validado = False
    while not validado:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('\033[0;31mERRO! Digite um preço válido.\033[m')
        else:
            return float(entrada)
