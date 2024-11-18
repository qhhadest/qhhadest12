import json
import urllib.request


class CurrencyConverter:
    def __init__(self):
        self.api_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        self.rate = self.get_usd_exchange_rate()

    def get_usd_exchange_rate(self):
        try:
            with urllib.request.urlopen(self.api_url) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    # Знаходимо курс долара США (код валюти USD)
                    for currency in data:
                        if currency['cc'] == 'USD':
                            return currency['rate']
                    print("Не вдалося знайти курс долара США.")
                    return None
                else:
                    print(f"Помилка при отриманні даних: {response.status}")
                    return None
        except urllib.error.URLError as e:
            print(f"Помилка при отриманні курсу валют: {e.reason}")
            return None

    def convert_uah_to_usd(self, uah_amount):
        if self.rate is None:
            print("Неможливо виконати конвертацію без курсу валют.")
            return None
        return uah_amount / self.rate


if __name__ == "__main__":
    converter = CurrencyConverter()
    if converter.rate:
        print(f"Актуальний курс долара США: {converter.rate:.2f} UAH/USD")
        try:
            uah_amount = float(input("Введіть суму в гривнях: "))
            usd_amount = converter.convert_uah_to_usd(uah_amount)
            if usd_amount is not None:
                print(f"{uah_amount} UAH дорівнює приблизно {usd_amount:.2f} USD.")
        except ValueError:
            print("Будь ласка, введіть коректне числове значення.")
