

class Pilha(object):
    def __init__(self):        
        self.pilha = []

    def put(self, arg):
        self.pilha.append(arg)
    def pop(self):
        try:
            return self.pilha.pop(-1)
        except IndexError:
            return None
    def view(self):
        try:
            return self.pilha.index(-1)
        except IndexError:
            return None
    def vazio(self):
        return len(self.pilha) == 0
    def __str__(self):
        return str(self.pilha)
