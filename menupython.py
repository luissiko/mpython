#Universidad del caribe
#Organizaciòn y diseño de computadora
#Alumno:Pedro Luis Pèrez Barahona
#Profesor #Ismael Jimènez Sanchèz
# Definir funciones para realizar las operaciones
#Convertir de binario a decimal
#Convertir de decimal a binario
#Multiplicar
#Dividir
#Sumar
#Restar
#Salir

#Opción Convertir de binario a decimal
def binario_a_decimal(binario):
    decimal = int(binario, 2)
    return decimal
#Opción Convertir de decimal a binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario
#Opción Multiplicar
def multiplicar(a, b):
    return a * b
#Opción Dividir
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"
#Opción Sumar
def sumar(a, b):
    return a + b
#Opción Restar
def restar(a, b):
    return a - b

#Opción Bucle principal del menú
while True:
    print("Menú:")
    print("1. Binario a decimal")
    print("2. Decimal a binario")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar")
    print("6. Restar")
    print("7. Salir")

    # Solicitar al usuario que elija una opción
    opcion = int(input("Seleccione una opción: "))
    #Opción Convertir de binario a decimal
    if opcion == 1:
        binario = input("Ingrese un número binario: ")
        decimal = binario_a_decimal(binario)
        print("El valor decimal es:", decimal)
    #Opción Convertir de decimal a binario
    elif opcion == 2:
        decimal = int(input("Ingrese un número decimal: "))
        binario = decimal_a_binario(decimal)
        print("El valor binario es:", binario)
    #Opción Multiplicar
    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = multiplicar(a, b)
        print("El resultado de la multiplicación es:", resultado)
    #Opción Dividir
    elif opcion == 4:
        a = float(input("Ingrese el dividendo: "))
        b = float(input("Ingrese el divisor: "))
        resultado = dividir(a, b)
        print("El resultado de la división es:", resultado)
    #opcion suma
    elif opcion == 5:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = sumar(a, b)
        print("El resultado de la suma es:", resultado)
        #opcion resta
    elif opcion == 6:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = restar(a, b)
        print("El resultado de la resta es:", resultado)
        #opcion Salir
    elif opcion == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")