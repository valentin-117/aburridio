
def es_palindromo(cadena):
    # Convertimos la cadena a minúsculas y eliminamos espacios
    cadena = cadena.replace(" ", "").lower()
    # Comparamos la cadena con su inversa
    return cadena == cadena[::-1]

print(es_palindromo("radar"))  # Debería devolver True
print(es_palindromo("hola"))   # Debería devolver False
print(es_palindromo("anita lava la tina"))  # Debería devolver True
