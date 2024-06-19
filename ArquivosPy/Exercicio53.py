frase = str(input('Digite uma frase: ')).strip()
nospace = ''.join(frase.split()).lower()
if nospace == nospace[::-1]:
    print('Esta frase É SIM um palíndromo!!')
else:
    print('Esta frase NÃO É um palíndromo!!')
