class Pessoa:
    def __init__(self, nome="", telefone="", endereco=""):
        self.__endereco = endereco
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    def __str__(self):
        return f"Olá seu nome é {self.nome}, seu endereço é {self.endereco} e seu numero é {self.telefone}"
    
t = Pessoa()
t.nome = 'Lucio Flavio'
t.endereco = 'José lira 396'
t.telefone = '987967014'
print(t)
