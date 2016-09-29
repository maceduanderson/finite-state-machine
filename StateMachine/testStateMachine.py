# Autor : Anderson Macedo
import unittest
from StateMachine import *



class Test_testStateMachine(unittest.TestCase):

    def setUp(self):
       
       
       iszero = lambda chr: chr is '0'
       isone = lambda chr: chr is '1'
       
       self.stateinitial = State(name="q0")
       self.stateone = State(finalstate=True, name="q1")
              
       self.stateinitial.addtransition(Transition(isone, self.stateone))
       self.stateinitial.addtransition(Transition(iszero, self.stateinitial))
       self.stateone.addtransition(Transition(iszero, self.stateinitial))
       self.stateone.addtransition(Transition(isone, self.stateone))
       

    def test_A(self):
        matchstring = list('01010101')
        finalstate = stateMachine(self.stateinitial, matchstring)
        self.assertTrue(finalstate.isfinal)

if __name__ == '__main__':
    unittest.main()
