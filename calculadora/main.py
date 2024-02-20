

def suma():
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa el segundo valor: "))
    suma = valor1 + valor2
    print("******" * 5)
    print(f" Suma de {valor1} + {valor2} = {suma}")
    print("******" * 5)

def resta():
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa el segundo valor: "))
    resta = valor1 - valor2
    print("******" * 5)
    print(f" Resta de {valor1} - {valor2} = {resta}")
    print("******" * 5)

def multiplicacion():
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa el segundo valor: "))
    multiplicacion = valor1 * valor2
    print("******" * 5)
    print(f" Multiplicación de {valor1} - {valor2} = {multiplicacion}")
    print("******" * 5)

def division():
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa el segundo valor: "))
    division = valor1 / valor2
    print("******" * 5)
    print(f" Multiplicación de {valor1} / {valor2} = {division}")
    print("******" * 5)

def potencia():
    valor1 = int(input("Ingresa el primer valor: "))
    valor2 = int(input("Ingresa la potencia "))
    potencia = valor1 ** valor2
    print("******" * 5)
    print(f" Potencia de {valor1} ** {valor2} = {potencia}")
    print("******" * 5)

def propina():
    total = float(input("Ingresa el total de la cuenta: "))
    porcentaje = int(input("Ingresa el porcentaje (%) que deseas dejar: "))
    total_porcentaje = porcentaje / 100
    propina = total * total_porcentaje 
    print("******" * 5)
    print(f" Propina del {porcentaje}% de {total} = {propina}")
    print("******" * 5)

def main ():
    opcion = 0

    while opcion != 7:
        print("******" * 5)
        print("Calculadora")
        print("******" * 5)
        print("Selecciona la operacion que desees realizar.")
        print('1.- Suma.')
        print('2.- Resta.')
        print('3.- Multiplicación.')
        print('4.- División.')
        print('5.- Potencia.')
        print('6.- Propina.')
        print('7.- Salir.')

        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()
        elif opcion == 5:
            potencia()
        elif opcion == 6:
            propina()
        else:
            print("Hasta luego.")

main()