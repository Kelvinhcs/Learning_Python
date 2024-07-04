from datetime import datetime
def voto(ano):
    idade = datetime.now().year - anonasc    
    if ano >= 65:
        return f'Com {idade} anos, a situação de voto é: OPCIONAL.'
    if ano < 65 and ano >= 18:
        return f'Com {idade} anos, a situação de voto é: OBRIGATÓRIO.'
    if ano < 18:
        return f'Com {idade} anos, a situação de voto é: NÃO HABILITADO.'


anonasc = int(input('Ano do nascimento: '))
print(voto(anonasc))