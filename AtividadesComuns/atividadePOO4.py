
class ContaBancaria:
    def __init__(self, numero, saldo=0.0):
        self.__numero = numero
        self.__saldo = saldo

    def Saque(self, retirada):
        assert TypeError, "Não foi possivel realizar o deposito, ERRO de digitação."
        assert retirada < self.saldo, "Saque Invalido."
        self.retirada = retirada
        self.saldo -= self.retirada
        
    def Deposito(self, depositar):
        assert TypeError, "Não foi possivel realizar o deposito, ERRO de digitação."
        assert depositar < 0, "Deposito Invalido."
        self.depositar = depositar
        self.saldo += self.depositar
        
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
        

    def __str__(self):
        return f"""
        Numero da conta: {str(self.__numero)} 
        Saldo da Conta: {str(self.__saldo)}
        """
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, saldo, taxajuros=0.16):
        super().__init__(numero, saldo)
        self.__taxajuros = taxajuros
    @property
    def taxajuros(self):
        return self.__taxajuros
    
    def rendimento_poupanca(self):
        return self.saldo + (self.saldo * self.taxajuros)
    
    def __str__(self):
        return f"""
        Saldo apos rendimento: {self.rendimento_poupanca()}
        """
    
class ContaCorrente(ContaBancaria):
    def __init__(self, numero, saldo, limite_cheque_especial):
        super().__init__(numero, saldo)
        self.__limite_cheque_especial = limite_cheque_especial
    @property
    def limite_cheque_especial(self):
        return self.__limite_cheque_especial
    @limite_cheque_especial.setter
    def limite_cheque_especial(self, limite_cheque_especial):
        assert limite_cheque_especial < 1000, "Valor limite excedido."
        self.__limite_cheque_especial = limite_cheque_especial
    def __str__(self):
        continha =  super().__str__()
        return f"""
        {continha}Cheque especial: {self.__limite_cheque_especial}
        """
        
if __name__ =='__main__':
    numero_conta = str(input("Digite o numero da sua conta: "))
    valorart = 1000
    Contabank = ContaBancaria(numero_conta, valorart)
    Contpoupa = ContaPoupanca(Contabank.numero, Contabank.saldo)
    verifica = len(numero_conta)
    if verifica != 7:
        print("dados invalidos.")
    else:
        print("""
        Digite 1 para saque;
        Digite 2 para deposito;
        Digite 3 para Acessar sua poupança;
        Digite 4 para acessar seu cheque especial; 
        Digite qualquer coisa para sair.""")
        Op = int(input("Opção: "))
        if Op == 1:
            try:
                print("Quanto você deseja sacar? ")
                valorsaq = float(input('Valor: '))
                Contabank.Saque(valorsaq)
                print(Contabank)
            except IndexError as e:
                print(e)
        elif Op == 2:
            try:
                print("Quanto você deseja depositar? ")
                valordepo = float(input('Valor: '))
                Contabank.Deposito(valordepo)
                print(Contabank)
            except IndexError as e:
                print(e)
        elif Op == 3:
            try:
                print("Rendimento possivel da poupança! ")
                print(Contpoupa)
            except IndexError as e:
                print(e)
        elif Op == 4:
            try:
                print("Qual valor do seu cheque especial? ")
                valorcheque = float(input("Digite: "))
                ContCorre = ContaCorrente(Contabank.numero, Contabank.saldo, valorcheque)
                print(ContCorre)
            except IndexError as e:
                print(e)
        else:
            exit
    
            

        
            
