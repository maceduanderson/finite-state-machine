from StateMachine import *
from ValidadorLexico import lexic_number
from pilha import Pilha


val = 0

def is_number(arg, stack):
    finalstate, recognizedstr = lexic_number(arg)
    if finalstate:
        stack.put(float(arg))
        return True
    return False

def is_arith_low_priority(arg, stack):
    if arg in ["+", "-"]:
        stack.put(arg)
        return True
    return False

def calc_stack(arg, stack):
    finalstate, recognizedstr = lexic_number(arg)
    if finalstate:                
        auxarg = float(arg)    
        if not stack.vazio():        
            operator = stack.pop()
            auxarg2 = stack.pop()
            if operator is "*":
                val = (auxarg2 * auxarg)
            if operator is "/":
                val = (auxarg2 / auxarg)
            if operator is "+":
                val = (auxarg2 + auxarg)
            if operator is "-":
                val = (auxarg2 - auxarg)
            stack.put(val)                        
        return True
    return False

def is_arith_high_priority(arg, stack):
    if arg in ["*", "/"]:
        stack.put(arg)        
        return True
    return False

def is_pv(arg, stack):
    if arg is ";":
        global val
        while not stack.vazio():        
            auxarg = stack.pop()    
            operator = stack.pop()
            auxarg2 = stack.pop()
            if operator is "*":
                val = val + (auxarg2 * auxarg)          
            if operator is "/":
                val = val + (auxarg2 / auxarg)
            if operator is "+":
                val = val + (auxarg2 + auxarg)
            if operator is "-":
                val = val + (auxarg2 - auxarg)
        return True
    return False


def calc(arg):

    q1 = StackState(name="q1")
    q2 = StackState(name="q2")
    q3 = StackState(name="q3", finalstate=True)
    
    q1q1 = Transition(is_number, q1)
    q1q12 = Transition(is_arith_low_priority, q1)
    q1q2 = Transition(is_arith_high_priority, q2)
    q2q1 = Transition(calc_stack, q1)
    q1q3 = Transition(is_pv, q3)    
    
    q1.addtransition(q1q1)
    q1.addtransition(q1q12)
    q1.addtransition(q1q2)
    q2.addtransition(q2q1)
    q1.addtransition(q1q3)

    finalstate, recognizedstr = stateMachine(q1, arg)
    if finalstate.isfinal():
        return val
    return False

