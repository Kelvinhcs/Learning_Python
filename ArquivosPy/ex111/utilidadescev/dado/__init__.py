def LeiaDinheiro(msg):
    while True:
        n = input(msg)
        if n.isdigit():
            return float(n)
        else:
            print('\033[0;31mERRO! Digite um preço válido.\033[m')