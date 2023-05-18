class Raça:

    def __init__(self, nome, raca, ativ=0):
        self.nome = nome
        self.raca = raca
        self.idade = 0
        self.info = None

    def Idade(self, idade):
        self.idade = idade
        return idade
    
    def atividades(self, ativ):
        self.ativ = ativ
        if ativ == None or int or float:
            print('Este campo foi preechido de maneira errada!')
        else:
            return ativ
    #Saida das informações!
    def saida(self):
        self.info = []
        self.info = self.nome, self.raca
        if self.info == None:
            return print('Animal sem nome!')
        else:
            return print(f'O nome do animal é: {self.info[0]}','\n', f'E seu sobre nome é: {self.info[1]}')
            


g = Raça(input('Digite the name: '), input('digite outro name: '))
print(f'O animal tem a idade de: {g.Idade(10)}')
print(f"O animal pratica a atividade de: {g.atividades('Dança')}")
print(g.saida())