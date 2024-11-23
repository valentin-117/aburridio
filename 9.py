
def generar_n_caracteres(n, caracter):
    resultado = ""
    for _ in range(n):
        resultado += caracter
    return resultado

print(generar_n_caracteres(5, "x"))  # Devuelve "xxxx"
