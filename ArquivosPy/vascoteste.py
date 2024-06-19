import emoji
from soundplay import playsound
frase = input('Qual é a palavra secreta?: ').strip().lower()
palavra = {'vasco', 'vascao', 'vascão', 'vascaino', 'vascaíno'}
while frase not in palavra:
    print("Você não é um cara legal de verdade")
    frase = input('Tente novamente: ')
print(emoji.emojize(':thumbs_up:'))
print("VOCÊ É MUITO FODA")
playsound('C:/Users/Kelvin/Pictures/pasta do kelvin/Vascao.mp3')



