
def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 3, 8]
lista_c = [7, 9, 10]

print(superposicion(lista_a, lista_b))  # Debería devolver True (tienen el 3 en común)
print(superposicion(lista_a, lista_c))  # Debería devolver False (no tienen elementos en común)
