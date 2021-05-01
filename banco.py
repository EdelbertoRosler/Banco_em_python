class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=1000):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        try:
            if (self.saldo + self.limite) < valor:
                print('Saldo insuficiente!')
                return False
            else:
                self.saldo -= valor
                if self.saldo < 0:
                    self.limite = (self.limite + self.saldo)
                print('Você sacou R$ {}\nSeu saldo atual é de R$ {}'.format(valor, self.saldo))
                return True
        except ValueError:
            print('Digite um valor válido!')
            return False


    def extrato(self):
        return 'Titular: {}\nConta : {}\nSaldo: R$ {}\nLimite disponível: R$ {}'.format(self.titular, self.numero,
                                                                                        self.saldo, self.limite)


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, titular, saldo, limite=0):
        super().__init__(numero, titular, saldo, limite)

    def saca_poupanca(self, valor):
        try:
            if self.saldo < valor:
                print('Saldo insuficiente!')
                return False
            else:
                self.saldo -= valor
                print('Você sacou R$ {}\nSeu saldo atual é de R$ {}'.format(valor, self.saldo))
                return True
        except ValueError:
            print('Digite um valor válido!')
            return False

# ******************************* M E N U S ***************************************

def menu():
    print('*' * 66)
    print(' Ola! Seja bem vindo ao DigiCASH Bank, o seu banco 100 % digital!')
    print('*' * 66)
    print('-' * 44)
    print('''O que você dedeja fazer?
  | [1] - Abrir uma nova Conta Corrente  |
  | [2] - Abrir uma nova Conta Poupança  |
  | [0] - Sair                           |''')
    print('-' * 44)
    escolha = str(input('Escolha o código da opção:'))

###### Conta Corrente e suas operações ######
    if escolha == '1':
        print('OK. Vamos lá...\nPara abrir uma nova conta, você deverá digitar o número, seu nome, e seu saldo...')
        CC1 = ContaCorrente(numero=int(input('N° Conta: ')),
                            titular=str(input('Nome: ')),
                            saldo=int(input('Saldo: ')))
        print('Conta Corrente criada com sucesso!')
        print('-' * 44)
        print('''O que você deseja fazer agora? 
  | [3] - Depósito                      |
  | [4] - Saque                         |
  | [5] - Extrato                       |
  | [0] - Voltar ao menu anterior       |''')
        print('-' * 44)

        submenu = str(input('Escolha o código da opção:'))
        while submenu == '3' or submenu == '4' or submenu == '5':
            if submenu == '3':
                while True:
                    try:
                        CC1.deposita(valor=float(input('Depositar R$ ')))
                        break
                    except ValueError:
                        print('Digite um valor válido!')
                submenu = str(input('Escolha o código da opção:'))

            if submenu == '4':
                while True:
                    try:
                        CC1.saca(valor=float(input('Sacar R$ ')))
                        break
                    except ValueError:
                        print('Digite um valor válido!')
                submenu = str(input('Escolha o código da opção:'))

            if submenu == '5':
                print(CC1.extrato())
                submenu = str(input('Escolha o código da opção:'))
            else:
                return False
            return True

###### conta poupança com suas operações ######
    elif escolha == '2':
        print('OK. vamos lá...\nVocê deve digitar o número, depois seu nome, e seu saldo...')
        CP1 = ContaPoupanca(numero=int(input('N° Conta: ')),
                            titular=str(input('Nome: ')),
                            saldo=int(input('Saldo: ')))
        print('Conta Poupança criada com sucesso!')
        print('-' * 44)

        print('''O que você deseja fazer agora? 
  | [3] - Depósito                      |
  | [4] - Saque                         |
  | [5] - Extrato                       |
  | [0] - Voltar ao menu anterior       |''')
        print('-' * 44)

        submenu = str(input('Escolha o código da opção:'))
        while submenu == '3' or submenu == '4' or submenu == '5':

            if submenu == '3':
                while True:
                    try:
                        CP1.deposita(valor=float(input('Depositar R$ ')))
                        break
                    except ValueError:
                        print('Digite um valor válido!')
                submenu = str(input('Escolha o código da opção:'))

            if submenu == '4':
                while True:
                    try:
                        CP1.saca_poupanca(valor=float(input('Sacar R$ ')))
                        break
                    except ValueError:
                        print('Digite um valor válido!')
                submenu = str(input('Escolha o código da opção:'))

            if submenu == '5':
                print(CP1.extrato())
                submenu = str(input('Escolha o código da opção:'))
            else:
                return False
            return True
    else:
        print('Bye, Bye!')
        return False
    return True


if __name__ == '__main__':
    while menu():
        pass