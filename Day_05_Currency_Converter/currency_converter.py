
import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if target_currency in data["rates"]:
            return data["rates"][target_currency]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    print("Currency Converter")
    print("------------------")

    base_currency = input("Enter the base currency (e.g., USD): ").upper()
    target_currency = input("Enter the target currency (e.g., EUR): ").upper()
    
    try:
        amount = float(input(f"Enter the amount in {base_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        print(f"Could not get exchange rate for {base_currency} to {target_currency}. Please check currency codes.")

if __name__ == "__main__":
    main()
