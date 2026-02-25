import urllib.request
import json


def get_rates(base):
    url = f"https://open.er-api.com/v6/latest/{base}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
    if data.get("result") != "success":
        return None
    return data["rates"]


def convert():
    print("=" * 50)
    print("          CURRENCY CONVERTER")
    print("=" * 50)

    common = ["USD", "EUR", "GBP", "ZAR", "JPY", "AUD", "CAD", "CHF", "CNY", "INR"]
    print("\nCommon currencies: " + ", ".join(common))

    while True:
        from_currency = input("\nFrom currency (e.g. USD): ").strip().upper()
        to_currency = input("To currency (e.g. ZAR): ").strip().upper()

        try:
            amount = float(input(f"Amount in {from_currency}: "))
        except ValueError:
            print("Invalid amount.")
            continue

        print("\nFetching live rates...")
        try:
            rates = get_rates(from_currency)
            if not rates:
                print("Could not fetch rates. Try again.")
                continue
            if to_currency not in rates:
                print(f"Currency '{to_currency}' not found.")
                continue

            result = amount * rates[to_currency]
            print("\n" + "=" * 50)
            print(f"  {amount:,.2f} {from_currency} = {result:,.2f} {to_currency}")
            print(f"  Rate: 1 {from_currency} = {rates[to_currency]} {to_currency}")
            print("=" * 50)

        except Exception as e:
            print(f"Error: {e}")

        again = input("\nConvert again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    convert()
