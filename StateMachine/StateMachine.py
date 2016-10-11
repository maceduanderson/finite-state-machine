# Autor : Anderson Macedo

class State(object):
    def __init__(self, finalstate=False, name="noname"):
        self.name = name #apenas para logging
        self.finalstate = finalstate
        self.transitions = list()

    def addtransition(self, transition):
        self.transitions.append(transition)
    
    #executa todas as transicoes para o dado argumento. caso contrario reorna vazio.
    def nextstate(self, transarg):
        for transition in self.transitions:
            if transition.functrans(transarg):
                return transition.nextstate                
        return State(name='lixo') 
        
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
        

# arg1 : estado inicial
# arg2 : lista com os elementos da entrada
def stateMachine(initialstate, inputarg):

    print "Iniciando maquina de estados"
    print "estado inicial = [%s]"%(initialstate)
    print("Palavra = " + str(inputarg))
    currstate = initialstate;
    laststate = None
    while currstate:
        laststate = currstate
        chr = None
        try:
            chr = inputarg.pop(0)
        except IndexError:
            print("fim da palavra")        
            return laststate
        currstate = currstate.nextstate(chr)
        print " [%s] ---------> [%s] input[%s]"%(laststate, currstate, chr)        
    return laststate
