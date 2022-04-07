import sys
from ExpressionTree import *


# funcion para obtener una expresion en orden sufijo
def getTreeFromSufix(expression, swp=0):

    # pila
    stack = []
    for c in expression:
        # Metemos en la pila si la expresion es un simbolo/operando matematico
        if (c == '+' or c == '-' or c == '*' or c == '/'):

            # Buscamos el primer simbolo/operando en la pila
            if not stack:
                raise Exception("Expresion mal formada. (faltan operandos)")

            a = stack.pop()  # primer simbolo/operando

            # Buscamos el segundo simbolo/operando en la pila
            if not stack:
                raise Exception("Expresion mal formada. (faltan operandos)")

            b = stack.pop()  # segundo simbolo/operando

            # Dependiendo del orden en el que recorremos el arbol si es de izquierda a derecha o al reves
            if swp:
                stack.append(ExpressionTree(c, a, b))
            else:
                stack.append(ExpressionTree(c, b, a))

        # si el elemento es un numero se mete en la pila
        else:
            stack.append(ExpressionTree(c))

    tree = stack.pop()

    # Si queda mas de un elemento en la pila
    if stack:
        raise Exception("Expresion mal formada. (sobran operandos)")
    return tree


# funcion para obtener una expresion en orden prefijo haciendo trampita
def getTreeFromPrefix(expression):
    # volteamos la expresion para que sea igual a la de sufijo y aplicamos la funcion
    # que calcula el orden sufijo
    return getTreeFromSufix(expression[::-1], 1)


def verifyActionFormat(action):

    if len(action) == 1 and action[0] == "SALIR":
        return True

    if len(action) < 3:
        return False

    if(action[0] != "EVAL" and action[0] != "MOSTRAR"):
        return False

    if(action[1] != "PRE" and action[1] != "POST"):
        return False

    for c in action[2:]:
        if(not c.isdigit() and c != '+' and c != '-' and c != '/' and c != '*'):
            return False

    return True

# menu


def menu():

    action = [""]
    print("-----BIENVENIDO A TU PROGRAMA PARA CALCULAR EXPRESIONES :D -----")
    print("-----Si desea evaluar una expresion prefija escriba algo de ")
    print("este estilo EVAL PRE + * + 3 4 5 7 -----")
    print("-----Si desea evaluar una expresion postfija escriba algo de")
    print("este estilo EVAL POST 8 3 - 8 4 4 + * + -----")
    print("-----Si solo desea mostrar una expresion prefija MOSTRAR PRE + * + 3 4 5 7")
    print("-----Si solo desea mostrar una expresion prefija MOSTRAR POST 8 3 - 8 4 4 + * +")
    print("-----Si desea salir del programa coloque la palabra SALIR -----")

    while(action[0] != "SALIR"):
        print("Ingrese la  accion que desea realizar :")
        action = sys.stdin.readline()[:-1].split(' ')

        if not verifyActionFormat(action):
            print("Formato invalido")
            continue

        # Salir del programa
        if action[0] == "SALIR":
            break

        tree = None

        if(action[1] == "PRE"):
            tree = getTreeFromPrefix(action[2:])
        else:
            tree = getTreeFromSufix(action[2:])

        if(action[0] == "EVAL"):
            print(tree.evaluate())
        else:
            tree.printInOrder()


if __name__ == "__main__":

    menu()
