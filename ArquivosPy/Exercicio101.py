def voto(anodonascimento):
    from datetime import datetime
    idade = datetime.now().year - anodonascimento    
    if idade < 16:
        return f'Com {idade} anos, a situação de voto é: NÃO HABILITADO.'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos, a situação de voto é: OPCIONAL'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos, a situação de voto é: OBRIGATÓRIO.'


AnoDigitado = int(input('Ano do nascimento: '))
print(voto(AnoDigitado))