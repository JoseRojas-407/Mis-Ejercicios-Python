
print("===== CALCULADORA =====")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")

opcion = int(input("Selecciona una opción (1-5): "))

if opcion == 1:
    print("Resultado:", num1 + num2)

elif opcion == 2:
    print("Resultado:", num1 - num2)

elif opcion == 3:
    print("Resultado:", num1 * num2)

elif opcion == 4:
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero")

elif opcion == 5:
    print("Resultado:", num1 ** num2)

else:
    print("Opción no válida")
