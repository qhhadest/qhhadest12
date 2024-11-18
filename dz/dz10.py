import sqlite3
import http.client
from datetime import datetime
import re

# URL веб-сайту з погодою
url = "meteofor.com.ua"

# Виконати GET-запит до сайту
conn = http.client.HTTPSConnection(url)
conn.request("GET", "/ru/weather-dnipro-5077/")
response = conn.getresponse()
data = response.read().decode('utf-8')

# Використання регулярних виразів для витягування температури
# Замість BeautifulSoup
temperature_regex = re.search(r'<div class="current-temperature">(\d+(\.\d+)?)°C</div>', data)

# Додати перевірку, чи знайдений збіг
if temperature_regex:
    temperature = float(temperature_regex.group(1))

    # Отримати поточну дату і час
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Підключитися до БД (або створити її, якщо не існує)
    connection = sqlite3.connect("weather_data.sqlite")

    # Створити курсор
    cursor = connection.cursor()

    # Створити таблицю, якщо вона не існує
    cursor.execute('''CREATE TABLE IF NOT EXISTS Weather (
                        datetime TEXT,
                        temperature REAL)''')

    # Вставити дані до таблиці
    cursor.execute("INSERT INTO Weather (datetime, temperature) VALUES (?, ?)", (current_datetime, temperature))

    # Зберегти зміни
    connection.commit()

    # Закрити з'єднання з БД
    connection.close()
else:
    print("Температуру не знайдено на веб-сторінці.")

