class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def andar(self):
        return f'O {self.nome} andou!'
    
    def emitir_som(self):
        return 

class Papagaio(Animal):
    def emitir_som(self):
        return 'Loro quer biscoito'



a1 = Papagaio('Brad')
print(a1.andar())
print(a1.emitir_som())

#Herança é basicamente criar uma classe com o parametro de outra classe já existente
#polimorfismo é alterar uma função existente na class mae para outra coisa
#encapsulamente é deixar algum atributo (função ele nao falou) para que seja modificado/chamado apenas na função