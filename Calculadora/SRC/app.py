def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

if __name__ == "__main__":
    while True:
        print("\n--- Calculadora Python ---")
        print("1. Sumar  2. Restar  3. Multiplicar  4. Dividir  5. Salir")
        opcion = input("Elige una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break 

        if opcion in ['1', '2', '3', '4']:
            a = int(input("Primer número: "))
            b = int(input("Segundo número: "))

        if opcion == '1':
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == '2':
            print(f"Resultado: {restar(a, b)}")
        elif opcion == '3':
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == '4':
            print(f"Resultado: {dividir(a, b)}")
    else:
        print("Opción no válida, intenta de nuevo.")