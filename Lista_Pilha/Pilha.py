from No import No 

class Pilha:
    def __init__(self):
        self.topo = None
        
    def is_empty(self):
        return self.topo is None
    
    def push(self, valor):
        no = No(valor)
        no.prox = self.topo
        self.topo = no
    
    def pop(self):
        assert self.topo != None, "A pilha ta vazia!"
        elemento_remover = self.topo
        self.topo = self.topo.prox
    
pilha = Pilha()
pilha.push(50)
pilha.push(20)
pilha.push(30)
pilha.push(10)
print(pilha.topo)
pilha.pop()
print(pilha.topo)


