import random

class Jogo:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.suits = ['Paus', 'Copas', 'Espadas', 'Ouros']
        self.ranks = ['Ás', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Valete', 'Rainha', 'Rei']
        self.values = {'Ás': 1, 'Dois': 2, 'Três': 3, 'Quatro': 4, 'Cinco': 5, 'Seis': 6, 'Sete': 7, 'Oito': 8, 'Nove': 9, 'Dez': 10, 'Valete': 11, 'Rainha': 12, 'Rei': 13}
        self.cartas_por_jogador = 5
        self.mão = {jogador: [] for jogador in jogadores}
        self.pontos = {jogador: 0 for jogador in jogadores}
        self.vencedor = None

    def embaralhar(self):
        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.deck)

    def distribuir_cartas(self):
        for i in range(self.cartas_por_jogador):
            for jogador in self.jogadores:
                self.mão[jogador].append(self.deck.pop())

    def calcular_pontos(self):
        for jogador, cartas in self.mão.items():
            for carta in cartas:
                rank = carta[0]
                self.pontos[jogador] += self.values[rank]

    def encontrar_vencedor(self):
        self.vencedor = max(self.pontos, key=self.pontos.get)

    def exibir_resultados(self):
        for jogador, cartas in self.mão.items():
            print(jogador + ':', cartas)
            print('Pontos:', self.pontos[jogador])

        print('\n' + self.vencedor + ' venceu com', self.pontos[self.vencedor], 'pontos!')

def jogar(jogadores):
    jogo = Jogo(jogadores)
    jogo.embaralhar()
    jogo.distribuir_cartas()
    jogo.calcular_pontos()
    jogo.encontrar_vencedor()
    jogo.exibir_resultados()

jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']
jogar(jogadores)
