import zipfile

def main():
    # Solicitamos al usuario la ruta de la imagen a comprimir
    imagen = input("Ingrese la ruta de la imagen a comprimir: ")

    # Corregimos la ruta de la imagen
    if imagen[1] == ":":
        imagen = "/mnt" + imagen

    # Creamos un archivo zip con el nombre de la imagen
    with zipfile.ZipFile(imagen + ".zip", "w") as zip_file:
        zip_file.write(imagen)

if __name__ == "__main__":
    main()
