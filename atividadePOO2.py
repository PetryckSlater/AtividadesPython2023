class Jogador:
    def __init__(self, nome='', data_nasc=0, nacionalidade="", altura="", peso=""):
        self.__nome = nome
        self.__data_nasc = data_nasc
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso
        
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property  
    def data_nasc(self):
        return self.__data_nasc
    @data_nasc.setter
    def data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade
    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
    
    def calculo_de_idade(self):
        return 2023 - self.__data_nasc
    
    def imprimir_dados(self):
        print(f"Nome: {self.__nome}")
        print(f"Data de nascimento: {self.__data_nasc}")
        print(f"Nacionalidade: {self.__nacionalidade}")
        print(f"Altura: {self.__altura}")
        print(f"Peso: {self.__peso}")
        print("A idade do jogador é de: ",self.calculo_de_idade())
        print('Tempo para se aposentar como atacante: ', 35 - self.calculo_de_idade())
        print('Tempo para se aposentar como Meio Campista: ', 35 - self.calculo_de_idade())
        print('Tempo para se aposentar como defesa: ', 40 - self.calculo_de_idade())
jogador1 = Jogador(nome="Neymar", data_nasc=1992, nacionalidade="Brasileiro", altura="1,75", peso="68kg")
jogador1.imprimir_dados()
