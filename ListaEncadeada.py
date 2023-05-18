from No import No 

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
    
    def inserir_valor_no_inicio(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo 
        else:
            novo.prox = self.cabeca
            self.cabeca = novo

    def inserir_valor_no_final(self, valor):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo 
        else:
            self.cauda.prox = novo
            self.cauda = novo
    
    def remover_do_inicio(self):
        if self.cabeca is None:
            print('A lista esta vazia vacilão.')
        if self.cabeca == self.cauda:
          self.cabeca = self.cauda = None
        else:
          self.cabeca = self.cabeca.prox

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual = self.cabeca
            while atual.prox is not self.cauda:
                atual = atual.prox
            self.cauda = atual
            atual.prox = None

class ListaEncadeadaEstendida(ListaEncadeada):
    def _init_(self):
        super()._init_()
    
    def pares(self):
        listapar = []
        par = self.cabeca
        while par != None:
            if par.carga % 2 == 0:
                listapar.append(par.carga)
            par = par.prox
        return listapar
    
    def impares(self):
        listaimpar = []
        impa = self.cabeca
        while impa != None:
            if impa.carga % 2 != 0:
                listaimpar.append(impa.carga)
            impa = impa.prox
        return listaimpar
    
    # def buscar_pos(self, valor):
    #     atual = self.cabeca
    #     pos = 0
    #     while atual != None:
    #         if atual.carga == valor:
    #             return pos
    #         atual = atual.prox
    #         pos += 1
    #     return -1
    #Retirei o buscar por que não ta funcionando direito não to conseguindo aplicar a logica

    def inserir_pos(self, pos, valor):
        novo = No(valor)
        atual = self.cabeca
        pos_atual = 0
        if pos == 0:
            self.inserir_valor_no_inicio(valor)
            return
        while atual != None:
            if pos_atual == pos - 1:
                novo.prox = atual.prox
                atual.prox = novo
                if novo.prox == None:
                    self.cauda = novo
                return
            atual = atual.prox
            pos_atual += 1

    def remover_de_posicao(self, pos):
        atual = self.cabeca
        pos_atual = 0
        if pos == 0:
            self.remover_do_inicio()
            return
        while atual != None:
            if pos_atual == pos - 1:
                if atual.prox == None:
                    self.remover_do_final()
                    return
                else:
                    atual.prox = atual.prox.prox
                    return
            atual = atual.prox
            pos_atual += 1

    def remover_ocorrencias(self, valor):
        atual = self.cabeca
        while atual != None and atual.carga == valor:
            self.cabeca = atual.prox
            atual = self.cabeca
        while atual != None:
            while atual.prox != None and atual.prox.carga == valor:
                atual.prox = atual.prox.prox
            atual = atual.prox
        if self.cabeca == None:
            self.cauda = None
class ListaUtls:
    @staticmethod
    def clonar(lista):
        NovaLista = ListaEncadeada()
        no_atual = lista.cabeca
        while no_atual is not None:
            NovaLista.inserir_valor_no_final(no_atual.carga)
            no_atual = no_atual.prox
        return NovaLista
    #AEEEE FUNCIONAAAAAAAAAAA

    @staticmethod
    def inverter(lista):
        ListaInvertida = ListaEncadeada()
        no_atual = lista.cabeca 
        if no_atual == lista.cauda:
            print("Lista Vazia.")
            return
        else:
            while no_atual is not None:
                ListaInvertida.inserir_valor_no_inicio(no_atual.carga)
                no_atual = no_atual.prox
            return ListaInvertida
            
        


lista1 = ListaEncadeada()
lista1.inserir_valor_no_final(1)
lista1.inserir_valor_no_inicio(4)
lista1.inserir_valor_no_inicio(6)
lista1.inserir_valor_no_inicio(3)
lista_clone = ListaUtls.clonar(lista1)
lista_invertida = ListaUtls.inverter(lista1)

print("Lista:", lista1.cabeca)
print("Lista clonada:", lista_clone.cabeca)
print("Lista invertida: ", lista_invertida.cabeca)
# lista.inserir_pos(2, 300)
# lista.remover_de_posicao(1)
# print("Lista de pares: ",lista.pares())
# print("Lista:", lista.cabeca)
# print("Lista de Impares: ",lista.impares())

