def validacao(DadosLocais, NomeDoArquivomsg, msg):
    saida2 = 2
    while True:
        try:
            digitado = input(msg)
        except KeyboardInterrupt:
            print('trigger saida')
        except:
            print('erro')
        else:
            return digitado, saida2
    
print(validacao([],'dados,json', 'Digita algo ai: '))