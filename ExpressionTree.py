# Classe que implementa un arbol
class ExpressionTree:

    # Inicializacion del arbol , recibe un simbolo matematico y dos hijos
    def __init__(self, expr, left=None, right=None):

        self.expr = expr
        self.left = left
        self.right = right

    # Funcion que imprime el arbol en  In order
    def printInOrder(self, endl=1):

        # variables creadas para simplificar nuestras condiciones
        div = self.expr == '/'
        subt = self.expr == '-'
        prec = self.expr == '*' or div
        op = prec or self.expr == '+' or subt

        # Bajamos recursivamente por el subarbol izquierdo
        if self.left != None:

            noprec = (self.left.expr == '+' or self.left.expr == '-')

            # SE colocan parentesis de ser necesario
            if prec and noprec:
                print("(", end="")

            self.left.printInOrder(0)

            # SE colocan parentesis de ser necesario
            if prec and noprec:
                print(")", end="")

        # si el nodo actual es un op se imprimen espacios
        if op:
            print(" ", end="")

        # Se imprime el nodo actual
        print(str(self.expr), end="")

        # si el nodo actual es un op se imprimen espacios
        if op:
            print(" ", end="")

        # Continuamos con el sub arbol derecho
        if self.right != None:

            # variables creadas para simplificar nuestras condiciones
            noprec = self.right.expr == '+' or self.right.expr == '-'
            rprec = self.right.expr == '*' or self.right.expr == '/'

            # SE colocan parentesis de ser necesario
            if (prec and noprec) or (subt and noprec) or (div and rprec):
                print("(", end="")

            self.right.printInOrder(0)

            # SE colocan parentesis de ser necesario
            if (prec and noprec) or (subt and noprec) or (div and rprec):
                print(")", end="")

        if(endl):
            print()

    # funcion que evalua la expresion que represnta el arbol
    def evaluate(self):

        # Verificaciones necesarias para los tipos de operaciones

        if(self.expr == '+'):
            return int(self.left.evaluate()) + int(self.right.evaluate())
        elif(self.expr == '*'):
            return int(self.left.evaluate()) * int(self.right.evaluate())
        elif(self.expr == '-'):
            return int(self.left.evaluate()) - int(self.right.evaluate())
        elif(self.expr == '/'):
            return int(self.left.evaluate()) // int(self.right.evaluate())
        else:
            return int(self.expr)
