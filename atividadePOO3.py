class Elevador:
    andar_atual = 0
    def __init__(self, andar_total=0, capacidade=0, total=0):
        self.__andar_total = andar_total
        self.__capacidade = capacidade
        self.__total = total
    
    @property
    def andar_total(self):
        return self.__andar_total
    
    @andar_total.setter
    def andar_total(self, andar):
        self.__andar_total = andar

    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade
    
    @property
    def total(self):
        return self.__total
    
    def addpessoa(self, pessoa):
        self.pessoa = pessoa
        self.add = self.pessoa + self.__total
        self.atual = self.add
        if self.add > self.__capacidade:
            print("Desculpe elevador cheio")
            return
        else:
            self.add + self.__capacidade
    
    def removpessoa(self, sair=0):
        self.saida = sair
        self.removendo = self.saida - self.__capacidade
        if self.__total == 0:
            print("Esta vazio")
            return
        else:
            self.removendo - self.__total
        
    def subir(self):
        if self.andar_atual > self.__andar_total:
            print("Desculpe, não existem mais andares.")
            __class__.andar_atual = self.__andar_total
        else:
            __class__.andar_atual +=1

    def descer(self):
        if self.andar_atual > self.__andar_total:
            print("Desculpe, não existem mais andares.")
            __class__.andar_atual = 0
        else:
            __class__.andar_atual -=1
        
    def imprimir(self):
        print('Andar atual: ', __class__.andar_atual)
        print('Andar total: ', self.__capacidade)
        print('total de pessoas: ', self.atual)
        print('Capacidade: ', self.__capacidade)

t = Elevador(10, 10)
t.addpessoa(10)
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.subir()
t.imprimir()


