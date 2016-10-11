from StateMachine import *



def isnumber(arg):
    if arg.isdigit():
        return True
    return False

def isalpha(arg):
    if arg.isalpha():
        return True
    return False

def ispoint(arg):
    if arg is '.':
        return True
    return False

def isunderline(arg):
    if arg is '_':
        return True
    return False        


def lexinumber(args):

    q1 = State(name='q1')
    q2 = State(True, 'q2')
    q3 = State(name='q3')
    q4 = State(True, 'q4')
    

    q1q2 = Transition(isnumber, q2)
    q2q2 = Transition(isnumber, q2)    
    q2q3 = Transition(ispoint, q3)
    q3q4 = Transition(isnumber, q4)
    q4q4 = Transition(isnumber, q4)

    q1.addtransition(q1q2)
    q2.addtransition(q2q2)
    q2.addtransition(q2q3)
    q3.addtransition(q3q4)
    q4.addtransition(q4q4)

    listArgs = list(args)

    finalstate = stateMachine(q1, listArgs)

    return finalstate.isfinal()


def lexiident(args):

    q1 = State(name='q1')
    q2 = State(True, 'q2')

    q1q2 = Transition(isalpha, q2)
    q2q2 = Transition(isalpha, q2)
    q2q21 = Transition(isnumber, q2)
    q2q22 = Transition(isunderline, q2)

    q1.addtransition(q1q2)
    q2.addtransition(q2q2)
    q2.addtransition(q2q21)
    q2.addtransition(q2q22)

    listargs = list(args)

    finalstate = stateMachine(q1, listargs)

    return finalstate.isfinal()
