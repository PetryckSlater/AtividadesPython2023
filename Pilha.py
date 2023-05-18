class testpilha:
    def __init__(self):
        self.pilha = [3,4]
        
    def entrada(self, v1):
        self.pilha.append(v1)
        return self.pilha
    def remover(self):
        self.pilha.pop() #Remove o ultimo fila remove o primeiro e o primeiro é sempre marcado na memoria como 0
        return self.pilha
    
    def imprimir(self):
        print(f'{self.pilha}')

t = testpilha()
t.entrada(2)
t.entrada(5)
t.entrada(6)
t.remover()
print(t.imprimir())
