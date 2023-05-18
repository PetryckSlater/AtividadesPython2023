class No:
    def __init__(self, carga, prox = None):
        self.carga = carga
        self.prox = prox
    
    def __str__(self):
        if self.prox == None:
            return '%s -> ' % (self.carga)
        else:
            return '%s -> %s' % (self.carga, self.prox)

