def max(a, b, c):

    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

print(f"El mayor número es: {max(num1, num2, num3)}")
