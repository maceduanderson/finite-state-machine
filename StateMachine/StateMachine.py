# Autor : Anderson Macedo
from pilha import Pilha

class State(object):
    def __init__(self, finalstate=False, name="noname"):
        self.name = name #apenas para logging
        self.finalstate = finalstate
        self.transitions = list()
        self.trash = False

    def addtransition(self, transition):
        self.transitions.append(transition)
    
    #executa todas as transicoes para o dado argumento. caso contrario reorna vazio.
    def nextstate(self, transarg):
        for transition in self.transitions:
            if transition.functrans(transarg):
                return transition.nextstate                
        
        lixo = State(name='lixo')
        lixo.trash = True
        return lixo
    
    def islixo(self):
        return self.trash    
    def isfinal(self):
        return self.finalstate
    def __str__(self):
        return self.name

# arg1 : referencia para funcao. A funcao deve receber apenas 1 argumento e retornar um booleano
# arg2 : um objeto State(). 
class Transition(object):
    def __init__(self, functrans, nextState):
        self.functrans = functrans
        self.nextstate = nextState
        
class StackState(State):
    def nextstate(self, transarg, stack):
        for transition in self.transitions:
            if transition.functrans(transarg, stack):
                return transition.nextstate                
        
        lixo = State(name='lixo')
        lixo.trash = True
        return lixo

# arg1 : estado inicial
# arg2 : lista com os elementos da entrada
def stateMachine(initialstate, inputarg):

    print "Iniciando maquina de estados"
    print "estado inicial = [%s]"%(initialstate)
    print("Palavra = " + "".join(inputarg))
    currstate = initialstate;
    laststate = None
    recognizedstr = list()
    stack = Pilha()
    while currstate:
        laststate = currstate
        chr = None
        try:
            chr = inputarg.pop(0)
        except IndexError:
            print("fim da palavra")        
            return laststate, "".join(recognizedstr)
        if type(currstate) == State:             
            currstate = currstate.nextstate(chr)
        else:
            currstate = currstate.nextstate(chr, stack)
            print("Estado da pilha")
            print(stack)               
        if currstate.islixo():            
            return laststate, "".join(recognizedstr)
        print " [%s] ---------> [%s] input[%s]"%(laststate, currstate, chr)
        recognizedstr.append(chr)        
    return laststate, "".join(recognizedstr)
