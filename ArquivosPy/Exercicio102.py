def fatorial(num, show=False):
    """
    Função que calcula o fatorial de um número, td bem que vc poderia utilizar a biblioteca, mas vale a pena aprender sempre as bases né.
    :parametro num: número para o calculo do fatorial
    :parametro show= (opcional): faz um print do cálculo que foi feito 
    :return: Retorna o fatorial do número informado
    """
    resultado = 1 
    for um in range(num, 0, -1):
        if show == True:
            print(um, end='')
            if um > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= um
    return resultado








numero = int(input('Digite um número: '))
print(fatorial(numero, show=True))