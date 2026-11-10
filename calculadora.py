
print("===== CALCULADORA =====")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Selecciona una opción (1-4): "))

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

else:
    print("Opción no válida")
