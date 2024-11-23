def longitud(elemento):

    contador = 0
    for _ in elemento:
        contador += 1
    return contador

# Ejemplo de uso con una cadena
cadena = input("Ingresa una cadena: ")
print(f"La longitud de la cadena es: {longitud(cadena)}")

# Ejemplo de uso con una lista
lista = [1, 2, 3, 4, ]
print(f"La longitud de la lista es: {longitud(lista)}")
