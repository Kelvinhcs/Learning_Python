#Add extrato (histórico de depositos) - DONE
#Taxas de saque - DONE
#Bloqueio de conta de pois de sacar X 
#Transferencias de contas
lista_depositos = []
taxa = 1.50
valor_bloqueio = 350.00
class ContaBancaria:
    def __init__(self, nome, saldo_inicial=0, bloqueio=False) -> None:
        self.nome_titular = nome
        self.saldo = float(saldo_inicial)
        self.bloqueio = False        
        self.contagem_saques = 0
    def exibir_saldo(self):
        print(f"O saldo atual é de: R${float(self.saldo):.2f}")
        
    def depositar(self, valor_deposito):
        if valor_deposito < 0:
            print('O depósito desta maneira não foi aceito')
        else:
            self.saldo += valor_deposito
            print(f"O Valor de R${float(valor_deposito):.2f} foi depositado com sucesso")
            self.exibir_saldo()
            lista_depositos.append(f"{float(valor_deposito):.2f}")
            
    def saque(self, valor_saque):
        global taxa
        global valor_bloqueio
        valor_mais_taxa = float(valor_saque + taxa)
        if self.bloqueio == True:
            print('Saque indisponível por bloqueio de conta')
        else:
            if valor_mais_taxa > self.saldo:
                print('Saldo Insuficiente')
                print(f"Saque com a taxa: R${valor_mais_taxa} (Taxa atual de R${taxa}")
                print(f"Saldo atual: R${self.saldo}")
            else:
                if self.contagem_saques >= 3:
                    self.bloqueio = True
                    print(f"Conta Bloqueada")
                    print(f"Motivação: Quantidade de saques ultrapassada, procure sua agência.")
                elif valor_saque > valor_bloqueio:
                    self.bloqueio = True
                    print(f"Conta bloqueada")
                    print(f"Motivação: Valor de saque acima, procure sua agência.")
                else:     
                    self.saldo -= valor_mais_taxa
                    self.contagem_saques += 1
                    print(f"Saque da quantia de R${float(valor_saque):.2f} foi efetuado com sucesso")
                    print(f"Foi descontado a taxa de R$1.50 de sua conta")
                    self.exibir_saldo() 
        
    def historico_depositos(self, lista):
        for num, item in enumerate(lista, start=1):
            print(f"{num} Depósito - R${float(item):.2f}")
        
        
                    
p1 = ContaBancaria("José")
print()

p1.depositar(valor_deposito=50)
p1.depositar(valor_deposito=100)
p1.depositar(valor_deposito=200)
p1.depositar(valor_deposito=50)
print()

p1.saque(valor_saque=2)
p1.saque(valor_saque=380)
p1.saque(valor_saque=2)
print()

p1.historico_depositos(lista_depositos)