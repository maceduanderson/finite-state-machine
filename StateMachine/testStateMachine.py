# Autor : Anderson Macedo
import unittest
from StateMachine import *




class Test_testStateMachine(unittest.TestCase):

    def setUp(self):
              
       iszero = lambda chr: chr is '0' #define uma funcao que valida se char == 1
       isone = lambda chr: chr is '1' #define uma funcao que valida se char == 0
       
       
       #Automato finito que reconhece linguagens que terminam em 1 ex: 001, 010101, 1.
       #Alfabeto[0,1]
       #Conjunto de estados[q0, q1]
       #Estado final[q1]
       #Estado inicial[q0]       
       self.stateinitial = State(name="q0")
       self.stateone = State(finalstate=True, name="q1")              
       self.stateinitial.addtransition(Transition(isone, self.stateone))
       self.stateinitial.addtransition(Transition(iszero, self.stateinitial))
       self.stateone.addtransition(Transition(iszero, self.stateinitial))
       self.stateone.addtransition(Transition(isone, self.stateone))
       

    def test_limites(self):
        matchstring = list('1')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertTrue(finalstate.isfinal())

        matchstring = list('0')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertFalse(finalstate.isfinal())

    def test_null(self):        
        matchstring = list()
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertFalse(finalstate.isfinal())

    def teste_linguagem_valida(self):
        matchstring = list('1')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertTrue(finalstate.isfinal())

        matchstring = list('000001')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertTrue(finalstate.isfinal())

        matchstring = list('010101111')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertTrue(finalstate.isfinal())

    def teste_linguagem_invalida(self):
        matchstring = list('0')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertFalse(finalstate.isfinal())

        matchstring = list('1111110')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertFalse(finalstate.isfinal())

        matchstring = list('1010101100')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertFalse(finalstate.isfinal())

if __name__ == '__main__':
    unittest.main()
