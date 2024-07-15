def metade(x=0, form=False):
    y = x/2
    if form == True:
        return f'R${y:.2f}'
    else:
        return y
    
def dobro(x=0, form=False):
    y = x*2
    if form == True:
        return f'R${y:.2f}'
    else:
        return y
    
def aumentar(Digitado=0, Valor=0, form=False):
    porcentagem = (Digitado*Valor)/100
    total = porcentagem + Digitado
    if form == True:
        return f'R${total:.2f}'
    else:
        return total
    
def diminuir(Digitado=0, Valor=0, form=False):
    porcentagem = (Digitado*Valor)/100
    total = Digitado - porcentagem
    if form == True:
        return f'R${total:.2f}'
    else:
        return total
    
def moeda(x):
    return f'R${x:.2f}'

def resumo(Digitado=0,Aumento=0,Reducao=0):
    print('-'*40)
    print(f'{'Resumo dos valores':^40}')
    print('-'*40)
    print(f'Valor Analisado: \t{moeda(Digitado)}')
    print(f'Dobro do valor: \t{dobro(Digitado, form=True)}')
    print(f'Metade do valor: \t{metade(Digitado, form=True)}')
    if Aumento > 9:
        print(f'{Aumento}% de aumento: \t{aumentar(Digitado, Aumento, form=True)}')
    else: 
        print(f'{Aumento}% de aumento: \t\t{aumentar(Digitado, Aumento, form=True)}')
    if Reducao > 9:
        print(f'{Reducao}% de redução: \t{diminuir(Digitado, Reducao, form=True)}')
    else:    
        print(f'{Reducao}% de redução: \t\t{diminuir(Digitado, Reducao, form=True)}')
    print('-'*40)