# Carolina Rivas 13-11209
alpha = 5
beta = 7
limite = alpha * beta

# Parte a
# Una subrutina recursiva que calcule F α,β para los valores de α y β obtenidos con las
# fórmulas mencionadas anteriormente. Esta implementación debe ser una traducción
# directa de la fórmula resultante a código.


def F5_7(n):
    if 0 <= n < limite:
        return n
    else:
        contador = 0
        contador += F5_7(n - 7)
        contador += F5_7(n - 14)
        contador += F5_7(n - 21)
        contador += F5_7(n - 28)
        contador += F5_7(n - 35)
        return contador

# Parte b
# Una subrutina recursiva de cola que calcule F α,β .


def F57_1(n):
    if 0 <= n < limite:
        return n
    else:
        return sum([F57_1(n-beta*i) for i in range(1, alpha+1)])

# Parte c
# La conversión de la subrutina anterior a una versión iterativa, mostrando claramente
# cuáles componentes de la implementación recursiva corresponden a cuáles otras de la
# implementación iterativa.


def F57_2(n):
    if 0 <= n < limite:
        return n
    else:
        acumulador = 0
        for i in range(1, alpha + 1):
            valor = n - beta * i
            if 0 <= valor < limite:
                acumulador += valor
        return acumulador


print("A")
print(F5_7(36))
print("B")
print(F57_1(37))
print("C")
print(F57_2(37))
