from ValidadorLexico import *
from StateMachine import *
from Tree import *
from calc_automato import calc
import re


valvar = {}


def valid_ident(arg):
    if arg in valvar.keys():        
        return True
    return False


def validador_expr(args):

    q0 = State(name="q0")
    q1 = State(name="q1")
    q2 = State(name="q2")
    q3 = State(name="q3")
    q4 = State(name="q4")
    q5 = State(name="q5", finalstate=True)

    q0q1 = Transition(lexic_ident, q1)
    q1q2 = Transition(is_atrib_operator, q2)        
    q2q4 = Transition(lexic_number, q4)
    q2q3 = Transition(lexic_ident, q3)
    q3q4 = Transition(valid_ident, q4)
    q4q2 = Transition(is_arithmetic_operator, q2)
    q4q5 = Transition(is_pv, q5)

    q0.addtransition(q0q1)
    q1.addtransition(q1q2)
    q2.addtransition(q2q4)
    q2.addtransition(q2q3)
    q3.addtransition(q3q4)
    q4.addtransition(q4q2)
    q4.addtransition(q4q5)

    listargs = list(args)

    finalstate, recognizedstr = stateMachine(q0, listargs)

    return finalstate.isfinal(), recognizedstr
    
    


if __name__ == '__main__':
    
    print("Iniciando validador de expressoes")
    nlines = 0
    while nlines <= 0:

        try:
            nlines = int(raw_input("Digite a quantidade de variaveis\n"))
            if nlines <= 0:
                print("O valor deve ser maior que 0")
        except ValueError:
            print("Valor Invalido")

    

    matchstr = re.compile("([a-z]+) = ([0-9]+)")

    while len(valvar) < nlines:
        print("Faltam [{}]".format(nlines - len(valvar)))
        attrib = str(raw_input("Digite a atribuicao\n"))
        match = matchstr.match(attrib)
        if match:
            valvar[match.group(1)] = match.group(2)
        else:
            print("expressao invalida\n Tente novamente")
    strexpr = str(raw_input("Digite a expressao\n"))

    arvore_expr = str_expr_to_tree(strexpr)
    printTree(arvore_expr)
    list_expr = tree_to_list(arvore_expr)

    validou, expr = validador_expr(list_expr)

    if validou:
        print("A expressao e valida")

        newlist_expr = [ valvar[x] if x in valvar.keys() else x for x in list_expr]

        print("".join(newlist_expr))

        arvore_right = arvore_expr.getRightChild()
        list_expr = tree_to_list(arvore_right)
        newlist_expr = [ valvar[x] if x in valvar.keys() else x for x in list_expr]
        
        
        valorfinal = calc(newlist_expr)

        arvore_left = arvore_expr.getLeftChild()
        list_expr = tree_to_list(arvore_left)

        print("o valor de %s e %s" %("".join(list_expr), str(valorfinal)))

    else: 
        print("A expressao nao e valida")



        



    pass

        
    
                                 
        
    
    
    
    


     