import os

def contar_lineas_codigo(archivo):
    with open(archivo, "r") as f:
        lines = f.readlines()

    contador = 0
    for line in lines:
        if not line.strip().startswith("#") and line.strip():
            contador += 1

    return contador

def main():
    archivo = input("Ingrese la ruta de un archivo .py: ")
    archivo = archivo.lower()
    if not archivo.endswith(".py"):
        print("El archivo no es un archivo .py")
        return

    try:
        numero_lineas = contar_lineas_codigo(archivo)
        print(f"El archivo {archivo} tiene {numero_lineas} líneas de código")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe")

if __name__ == "__main__":
    main()