def es_vocal(caracter):

    vocales = "aeiouAEIOU"
    if len(caracter) == 1 and caracter in vocales:
        return True
    return False

caracter = input("Ingresa un carácter: ")

if es_vocal(caracter):
    print(f"'{caracter}' es una vocal.")
else:
    print(f"'{caracter}' no es una vocal.")
