🧮 Calculadora Pro Python
Una aplicación de consola robusta escrita en Python que permite realizar operaciones aritméticas básicas y avanzadas con manejo de errores incorporado.

🚀 Características
El script app.py incluye las siguientes funcionalidades:
    Operaciones Básicas: Suma, resta, multiplicación y división.
    Operaciones Avanzadas: * Potenciación ($a^b$).
        Raíz cuadrada con validación de números negativos.
        Cálculo de porcentajes.
    Robustez:
        Manejo de errores para división por cero.
        Validación de entradas (evita el cierre del programa si el usuario ingresa letras en lugar de números).
        Menú interactivo en bucle.

📁 Estructura del Proyecto
Para que las pruebas unitarias y las importaciones funcionen correctamente, se recomienda la siguiente estructura:

Plaintext

Calculadora/
├── src/
│   ├── __init__.py    # Archivo para definir el módulo
│   └── app.py         # Lógica principal
├── TEST/
│   └── Testing_app.py # Pruebas unitarias
└── README.md          # Documentación

🛠️ Instalación y Uso
    Clonar el repositorio o descargar los archivos:
    Asegúrate de tener Python 3.x instalado.
    
    Ejecutar la calculadora:
    Desde la carpeta raíz, ejecuta:
    
    Bash
    python src/app.py

    Ejecutar las pruebas (Unit Tests):
    
    Si deseas verificar que todas las funciones trabajan correctamente, usa:
    
    Bash
    python -m unittest TEST/Testing_app.py

🧪 Ejemplo de Pruebas Unitarias

    El proyecto está diseñado para ser testeable. Las funciones están separadas de la interfaz de usuario, lo que permite realizar validaciones como:
   Función	         Entrada	Resultado Esperado
   sumar(5, 3)	      5, 3	    8
   dividir(10, 0)     10, 0	    "Error: No se puede..."
   raiz_cuadrada(-4)  -4	    "Error: No se puede..."
    
    📝 Licencia
    Este proyecto es de uso libre con fines educativos.