n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('-=-'*20)
if media < 5.0:
    print(f'Sua media Final foi de {media:.1f}\nEste ano você foi REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua media Final foi de {media:.1f}\nEste ano você permanecerá em RECUPERAÇÃO')
elif media >= 7.0:
    print(f'Sua média final foi de {media:.1f}\nEste ano você foi APROVADO\nParabéns!!!')
print('-=-'*20)
