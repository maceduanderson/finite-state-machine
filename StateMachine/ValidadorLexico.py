from StateMachine import *



def is_number(arg):
    if arg.isdigit():
        return True
    return False

def is_alpha(arg):
    if arg.isalpha():
        return True
    return False

def is_point(arg):
    if arg is '.':
        return True
    return False

def is_underline(arg):
    if arg is '_':
        return True
    return False        

def is_arithmetic_operator(arg):
    if arg in ['*', '/', '+', '-']:
        return True
    return False 

def is_atrib_operator(arg):
    if arg is '=':
        return True
    return False
def is_pv(arg):
    if arg is ';':
        return True
    return False

def lexic_number(args):

    q1 = State(name='q1')
    q2 = State(True, 'q2')
    q3 = State(name='q3')
    q4 = State(True, 'q4')
    

    q1q2 = Transition(is_number, q2)
    q2q2 = Transition(is_number, q2)    
    q2q3 = Transition(is_point, q3)
    q3q4 = Transition(is_number, q4)
    q4q4 = Transition(is_number, q4)

    q1.addtransition(q1q2)
    q2.addtransition(q2q2)
    q2.addtransition(q2q3)
    q3.addtransition(q3q4)
    q4.addtransition(q4q4)

    listargs = list(args)

    finalstate, recognizedstr = stateMachine(q1, listargs)

    return finalstate.isfinal(), recognizedstr


def lexic_ident(args):

    q1 = State(name='q1')
    q2 = State(True, 'q2')

    q1q2 = Transition(is_alpha, q2)
    q2q2 = Transition(is_alpha, q2)
    q2q21 = Transition(is_number, q2)
    q2q22 = Transition(is_underline, q2)

    q1.addtransition(q1q2)
    q2.addtransition(q2q2)
    q2.addtransition(q2q21)
    q2.addtransition(q2q22)

    
    listargs = list(args)

    finalstate, recognizedstr = stateMachine(q1, listargs)

    return finalstate.isfinal(), recognizedstr
