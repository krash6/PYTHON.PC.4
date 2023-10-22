import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error al solicitar el precio de Bitcoin: {e}")
        return None

if __name__ == "__main__":
    while True:
        try:
            n = float(input("Por favor, ingrese la cantidad de bitcoins que posee: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    bitcoin_price = get_bitcoin_price()
    if bitcoin_price is not None:
        cost_in_usd = n * bitcoin_price
        print(f"El costo actual de {n} Bitcoins en USD es: ${cost_in_usd:,.4f}")