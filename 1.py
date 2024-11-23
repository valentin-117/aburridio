def max(a, b):
    
    if a > b:
        return a
    else:
        return b

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print(f"El mayor número es: {max(num1, num2)}")
