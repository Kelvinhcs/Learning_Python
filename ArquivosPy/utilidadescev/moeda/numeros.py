def metade(x, form=False):
    y = x/2
    if form == True:
        return f'R${y:.2f}'
    else:
        return y
def dobro(x, form=False):
    y = x*2
    if form == True:
        return f'R${y:.2f}'
    else:
        return y
def aumentar(Digitado, Valor, form=False):
    porcentagem = (Digitado*Valor)/100
    total = porcentagem + Digitado
    if form == True:
        return f'R${total:.2f}'
    else:
        return total
def diminuir(Digitado, Valor, form=False):
    porcentagem = (Digitado*Valor)/100
    total = Digitado - porcentagem
    if form == True:
        return f'R${total:.2f}'
    else:
        return total
def moeda(x):
    return f'R${x:.2f}'
def resumo(Digitado,Aumento,Reducao):
    print(f"""-----------------------------------------
{'Resumo Do Valor':^40}
-----------------------------------------
Preço analisado:{moeda(Digitado):>15}
Dobro do preço:{dobro(Digitado, form=True):>17}
Metade do preço:{metade(Digitado, form=True):>15}
{Aumento}% de aumento:{aumentar(Digitado, Aumento, form=True):>16}
{Reducao}% de redução:{diminuir(Digitado, Reducao, form=True):>16}
-----------------------------------------
""")
    
    
    
    
    
    
    
