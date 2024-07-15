palavras = {'vasco', 'vascao', 'vascão', 'vascaino', 'vascaíno'}
def Acerto(msg):
    from emoji import emojize
    from soundplay import playsound
    if msg in palavras:
        print(emojize(':thumbs_up:'))
        playsound('C:/Users/Kelvin/Pictures/pasta do kelvin/Vascao.mp3')
        return 
    else:
        return 'Acesso Negado!'


while True:
    frase = input('Qual é a palavra secreta?: ').strip().lower()
    print(Acerto(frase))
