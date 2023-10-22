import requests
import datetime

def main():
    # Consultamos la API de CoinDesk
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
    except requests.RequestException:
        print("Error al consultar la API de CoinDesk")
        return

    # Obtenemos el precio actual de Bitcoin
    price = response.json()["bpi"]["USD"]["rate"]

    # Creamos un archivo txt con el formato adecuado
    with open("bitcoin_price.txt", "w") as f:
        f.write("Fecha, Precio\n")
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {price}\n")

if __name__ == "__main__":
    main()