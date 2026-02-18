import math

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

# 1. Función potencia
def potencia(base, exponente):
    return base ** exponente

# 2. Función raíz cuadrada con manejo de negativos
def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: No se puede calcular la raíz de un número negativo"
    return math.sqrt(numero)

# 3. Función calcular porcentaje
def calcular_porcentaje(porcentaje, total):
    return (porcentaje / 100) * total

def mostrar_menu():
    print("\n--- Calculadora Pro Python ---")
    print("1. Sumar           2. Restar         3. Multiplicar")
    print("4. Dividir         5. Potencia       6. Raíz Cuadrada")
    print("7. Porcentaje      8. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-8): ")

        if opcion == '8':
            print("¡Hasta luego!")
            break 

        # 5. Manejo de errores con try-except
        try:
            if opcion in ['1', '2', '3', '4', '5']:
                a = float(input("Primer número (o base): "))
                b = float(input("Segundo número (o exponente): "))
                
                if opcion == '1': print(f"Resultado: {sumar(a, b)}")
                elif opcion == '2': print(f"Resultado: {restar(a, b)}")
                elif opcion == '3': print(f"Resultado: {multiplicar(a, b)}")
                elif opcion == '4': print(f"Resultado: {dividir(a, b)}")
                elif opcion == '5': print(f"Resultado: {potencia(a, b)}")

            elif opcion == '6':
                n = float(input("Introduce el número: "))
                print(f"Resultado: {raiz_cuadrada(n)}")

            elif opcion == '7':
                p = float(input("Porcentaje a calcular (ej. 20): "))
                t = float(input("Sobre el total de: "))
                print(f"Resultado: {calcular_porcentaje(p, t)}")

            else:
                print("Opción no válida, intenta de nuevo.")
        
        except ValueError:
            print("Error: Por favor, introduce solo valores numéricos.")