def notas(*nota, situacao=False):
    """
    --> Pega as notas que forem colocadas na funcao e separa em um dicionário o total de notas, a maior nota, a menor nota, a media e a situação do aluno
    :param nota: Todas as notas dadas na chamada da função
    :param situação=: por padrao ela é false, utilize situacao=True para adicionar no dicionario o modo situacao
    :return: dicionario com as informaçoes separadas
    """
    mydict= {}
    for qtd, notaunica in enumerate(nota):
        if qtd == 0 or notaunica > maiornota:
            maiornota = notaunica
        if qtd == 0 or notaunica < menornota:
            menornota = notaunica
    media = sum(nota) / c
    mydict['Total'] = len(nota)
    mydict['Maior Nota'] = maiornota
    mydict['Menor Nota'] = menornota
    mydict['Média'] = f'{media:.2f}'
    if situacao == True:
        if media >= 7:
            mydict['Situação'] = 'Passou'
        if media < 7 and media > 3:
            mydict['Situação'] = 'Pode Recuperar'
        if media < 3:
            mydict['Situação'] = 'Reprovado'
    return mydict
    
    
resp = notas(2.2, 1.6, situacao=True)
print(resp)
