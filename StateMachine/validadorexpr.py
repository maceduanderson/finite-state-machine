from ValidadorLexico import *
from StateMachine import *
from Tree import *
from calc_automato import calc
import re





def fromfile():
    matchstr = re.compile("([a-z]+) = (\d+\.*\d*)")
    valvar = {}
    try:
        fd = open("exprdef.txt", "r")
        lines = []
        lines = fd.readlines()
        for i in range(0, len(lines)):
            if lines[i] == "\n":
                lines[i+1] = lines[i+1][:-1]
                return lines[i+1], valvar
            attrib = lines[i]
            match = matchstr.match(attrib)
            if match:
               valvar[match.group(1)] = match.group(2)
            else:
                print("Erro Ao processar arquivo")
                raise SystemExit                   
    except IOError:
        print("Arquivo exprdef.txt nao encontrando. Informe os dados pelo console.")
        return None, None


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
    q3q2 = Transition(is_arithmetic_operator, q4)
    q4q2 = Transition(is_arithmetic_operator, q2)
    q4q5 = Transition(is_pv, q5)

    q0.addtransition(q0q1)
    q1.addtransition(q1q2)
    q2.addtransition(q2q4)
    q2.addtransition(q2q3)
    q3.addtransition(q3q2)
    q4.addtransition(q4q2)
    q4.addtransition(q4q5)

    listargs = list(args)

    finalstate, recognizedstr = stateMachine(q0, listargs)

    return finalstate.isfinal(), recognizedstr
    

if __name__ == '__main__':
    
    print("Iniciando validador de expressoes")
    nlines = 0
    

    strexpr, valvar = fromfile()

    if strexpr == None:
        matchstr = re.compile("([a-z]+) = (\d+\.*\d*)")
        while nlines <= 0:
            try:
                nlines = int(raw_input("Digite a quantidade de variaveis\n"))
                if nlines <= 0:
                    print("O valor deve ser maior que 0")
            except ValueError:
                print("Valor Invalido")    
        while len(valvar) < nlines:
            print("Faltam [{}]".format(nlines - len(valvar)))
            attrib = str(raw_input("Digite a atribuicao\n"))
            match = matchstr.match(attrib)
            if match:
                valvar[match.group(1)] = match.group(2)
            else:
                print("atribuicao invalida\n Tente novamente")

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

        
    
                                 
        
    
    
    
    


     