import os

def guardar_tabla(numero):
    with open(f"tabla-{numero}.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{numero} x {i} = {numero * i}\n")

def leer_tabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            tabla = archivo.readlines()
        return tabla
    except FileNotFoundError:
        return "El archivo no existe"

def mostrar_linea(numero, linea):
    try:
        tabla = leer_tabla(numero)
        return tabla[linea - 1]
    except FileNotFoundError:
        return "El archivo no existe"

def menu():
    opcion = 0
    while opcion != 3:
        print("1. Guardar tabla")
        print("2. Leer tabla")
        print("3. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla(numero)
        elif opcion == 2:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            tabla = leer_tabla(numero)
            for linea in tabla:
                print(linea)
        elif opcion == 3:
            print("Hasta luego")

if __name__ == "__main__":
    menu()