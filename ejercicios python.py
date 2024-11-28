# Ejercicio 1
metros = int(input("Ingrese una cantidad en metros: "))
centimetros = metros * 100

print(f"{metros} metros son {centimetros} centímetros.")


# Ejercicio 2
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

edad_10 = edad + 10

print(f"Hola {nombre}, en 10 años tendrás {edad_10} años")


# Ejercicio 3
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area = base * altura / 2

print(f"El area del triángulo es: {area}")


# Ejercicio 4
numero1 = float(input("Ingresa un número: "))
numero2 = float(input("Ingresa otro número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Suma: {suma} Resta: {resta} Multiplicacion: {multiplicacion} Division: {division}")


# Ejercicio 5
precio = float(input("Ingresa el precio del producto: "))

iva = precio * 0.19

print(f"El precio final con IVA es: {precio + iva}")