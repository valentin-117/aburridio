
def sum(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    total = 1
    for numero in lista:
        total *= numero
    return total

numeros = [1, 2, 3, 4]
print(f"La suma de {numeros} es {sum(numeros)}")  # Debería devolver 10
print(f"El producto de {numeros} es {multip(numeros)}")  # Debería devolver 24
