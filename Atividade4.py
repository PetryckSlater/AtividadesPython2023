import random

class Jogo:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
        self.valor_dia = {'Segunda-feira': 1, 'Terça-feira': 2, 'Quarta-feira': 3, 'Quinta-feira': 4, 'Sexta-feira': 5}
        self.marcados = {jogador: [] for jogador in jogadores}
        self.pontos = {jogador: 0 for jogador in jogadores}
        self.vencedor = None

    def distribuir_cartas(self):
        dias = self.dias_da_semana.copy()
        random.shuffle(dias)

        for dia in dias:
            jogador = self.jogadores.pop(0)
            self.jogadores.append(jogador)
            self.marcados[jogador].append(dia)

    def calcular_pontos(self):
        for jogador, cartas in self.marcados.items():
            for carta in cartas:
                self.pontos[jogador] += self.valor_dia[carta]

    def encontrar_vencedor(self):
        self.vencedor = max(self.pontos, key=self.pontos.get)

    def exibir_resultados(self):
        for jogador, cartas in self.marcados.items():
            print(jogador + ':', cartas)
            print('Pontos:', self.pontos[jogador])

        print('\n' + self.vencedor + ' venceu com', self.pontos[self.vencedor], 'pontos!')

    def jogar(self):
        self.distribuir_cartas()
        self.calcular_pontos()
        self.encontrar_vencedor()
        self.exibir_resultados()


jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']
jogo = Jogo(jogadores)
jogo.jogar()
