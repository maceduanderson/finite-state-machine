import logging
class State(object):
    def __init__(self, finalstate=False, name="noname"):
        self.name = name #apenas para logging
        self.finalstate = finalstate
        self.transitions = list()

    def addtransition(self, transition):
        self.transitions.append(transition)

    def nextstate(self, transarg):
        for transition in self.transitions:
            if transition.functrans(transarg):
                return transition.nextstate 
        return None
    def isfinal(self):
        return self.finalstate

class Transition(object):
    def __init__(self, functrans, nextState):
        self.functrans = functrans
        self.nextstate = nextState
        


def stateMachine(initialstate, inputarg):

    print("Iniciando maquina de estados")
    print("estado inicial = ", initialstate.name)
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
        print("Proximo estado = ", currstate.name)
        print("Palavra = " + str(inputarg))
    return laststate