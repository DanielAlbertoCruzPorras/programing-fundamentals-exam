#Exercise 2
import math

def area(a):
    if (math.sqrt(3)/4) * (a ** 2) > 1000:
        #print(f"{(math.sqrt(3)/4) * (a ** 2):.2f}")  # Para verificar si en efecto el area es mayor a 1000
        print("DATOS NO VÁLIDOS")
    else:
        #print(f"El area de ese triángulo es de: {(math.sqrt(3)/4) * (a ** 2):.2f}")  # No piden imprimir el área pero por si a caso...
        return ((math.sqrt(3)/4) * (a ** 2))

# Main
A = float(input("Inserte la longitud del lado del triángulo: "))
Area = area(A)
