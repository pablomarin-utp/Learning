def pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)

    return pares
numeros = [2,5,43,8,546,765,3,6,9]

#paresn = pares(numeros)

def reloj(x):
    while x >= 1:
        x = x - 1

        print(x)

cont = reloj(10)