from datetime import datetime
print('...CALCULADOR DE ALISTAMENTO...')
genero = int(input('[0] Masculino\n[1] Feminino\nSelecione a opção do seu gênero biológico: '))
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = datetime.now().year - nascimento
print('-=-'*27)
if genero == 1:
    print('Por lei, as mulheres No Brasil\nNÃO participam do Alistamento militar obrigatório\nObrigado.')
elif genero != 1 and genero != 0:
    print('Você digitou uma opção incorreta\nPor gentileza, reinicie o programa\nObrigado.')
elif idade < 18 and genero == 0:
    print(f'Ainda faltam {18-idade} anos para você se alistar.')
    print(f'Você deverá se alistar em {(18-idade) + datetime.now().year}')
elif idade == 18 and genero == 0:
    print(f'Você precisa se alistar esse ano.')
    print(f'Compareça a uma junta militar IMEDIATAMENTE')
elif idade > 18 and genero == 0:
    print(f'Você deveria ter se alistado a {idade-18} anos atrás.')
    print(f'Seu comparecimento precisaria ter sido em {datetime.now().year-(idade-18)}')