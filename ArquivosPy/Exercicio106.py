while True:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    comando = str(input('Função ou Biblioteca? '))
    if comando.lower().strip() == 'fim':
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('-=-=-=-=-=-=-=-=-= ENCERANDO =-=-=-=-=-=-=-=-=-=-=')
        break
    else:
        print(help(comando))
        