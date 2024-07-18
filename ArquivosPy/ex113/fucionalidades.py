def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(f'\033[0;31mO Usuário decidiu não informar este dado, considerando 0...\033[m')
            return 0
        except:
            print('\033[0;31mERRO! Tente digitar o número novamente...\033[m')
        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = input(msg)
            if n.find('.') > -1:
                n = float(n)
            else:
                print('\033[0;31mERRO! Tente digitar o número novamente...\033[m')
                continue
        except KeyboardInterrupt:
            print(f'\033[0;31mO Usuário decidiu não informar este dado, considerando 0...\033[m')
            return 0
        except:
            print('\033[0;31mERRO! Tente digitar o número novamente...\033[m')
        else:
            return n