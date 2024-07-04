def notas(*nota, situacao=False):
    """
    --> Pega as notas que forem colocadas na funcao (Pode Receber várias notas) e separa em um dicionário o total de notas, a maior nota, a menor nota, a media e a situação do aluno.
    :param nota: Todas as notas dadas na chamada da função
    :param situacao(opcional): por padrao ela é false, utilize situacao=True para adicionar no dicionario o modo situacao
    :return: dicionario com as informaçoes separadas
    """
    DictPlacholder = {}
    for qtd, notaunica in enumerate(nota):
        if qtd == 0 or notaunica > maiornota:
            maiornota = notaunica
        if qtd == 0 or notaunica < menornota:
            menornota = notaunica
    #Neste caso acabei utilizando a opção de separar os número em um loop 1 por 1, mas o python suporta os métodos "max()" e "min()" para pegar respectivamente os maiores e menores números do parametro "nota"
    media = sum(nota) / len(nota)
    DictPlacholder['Total'] = len(nota)
    DictPlacholder['Maior Nota'] = maiornota
    DictPlacholder['Menor Nota'] = menornota
    DictPlacholder['Média'] = f'{media:.2f}'
    if situacao == True:
        if media >= 7:
            DictPlacholder['Situação'] = 'Passou'
        if media < 7 and media > 3:
            DictPlacholder['Situação'] = 'Pode Recuperar'
        if media < 3:
            DictPlacholder['Situação'] = 'Reprovado'
    return DictPlacholder
    
    
print(notas(2.2, 1.6, 5.9, situacao=True))
help(notas)
