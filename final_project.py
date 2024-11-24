import requests
import sqlite3
from bs4 import BeautifulSoup


# Об’єкт, що працює з базою даних
class DatabaseHandler:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''DROP TABLE IF EXISTS top_songs''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS top_songs (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                artist TEXT NOT NULL)''')
        self.connection.commit()


        self.connection.commit()

    def insert_data(self, title, artist):
        self.cursor.execute('INSERT INTO top_songs (title, artist) VALUES (?, ?)', (title, artist))
        self.connection.commit()

    def song_exists(self, title, artist):
        self.cursor.execute('SELECT COUNT(*) FROM top_songs WHERE title = ? AND artist = ?', (title, artist))
        return self.cursor.fetchone()[0] > 0

    def fetch_data(self):
        self.cursor.execute('SELECT * FROM top_songs')
        return self.cursor.fetchall()
    def fetch_data_paginated(self, limit, offset):
        self.cursor.execute('SELECT * FROM top_songs LIMIT ? OFFSET ?', (limit, offset))
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()


# Об’єкт, що парсить сайти
class WebParser:
    def __init__(self, url):
        self.url = url

    def fetch_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error fetching {self.url}: {response.status_code}")
            return None

    def parse_top_songs(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        songs = []

        # Знаходимо всі елементи, що містять інформацію про пісні
        entries = soup.find_all('div', class_='chart-track')
        for i, entry in enumerate(entries[:50]):  # берем тільки перші 50 пісень
            title = entry.find('div', class_='title').get_text(strip=True)
            artist = entry.find('div', class_='artist').get_text(strip=True)
            songs.append((title, artist))
        return songs


# Об’єкт інтерфейсу користувача
class UserInterface:
    def __init__(self, db_handler, web_parser):
        self.db_handler = db_handler
        self.web_parser = web_parser
        self.popular_songs = [
            ('Song of Freedom', 'ArtistA'),
            ('Echoes of Nature', 'ArtistB'),
            ('Rhythms of the Night', 'ArtistC')
        ]
        self.page_size = 10
    def add_additional_songs(self):
        for title, artist in self.popular_songs:
            self.db_handler.insert_data(title, artist)
        print("Пісні були успішно додані до бази даних.")

    def display_paginated_data(self, page_number):
        offset = (page_number - 1) * self.page_size
        data = self.db_handler.fetch_data_paginated(self.page_size, offset)
        for idx, row in enumerate(data, start=offset + 1):
            print(f"{idx}. {row[1]}")


    def run(self):
        print("Парсинг сайту...")
        html_content = self.web_parser.fetch_content()
        if html_content:
            top_songs = self.web_parser.parse_top_songs(html_content)
            for title, artist in top_songs:
                self.db_handler.insert_data(title, artist)
            print("Дані були успішно збережені в базу даних.")
            self.add_additional_songs()
            print("Виведення збережених даних з бази даних:")
            data = self.db_handler.fetch_data()
            unique_songs = {(row[1], row[2]) for row in data}
            for idx, (title, artist) in enumerate(unique_songs, start=1):
                print(f"{idx}. {title}")

            self.display_paginated_data(1)


if __name__ == '__main__':
    db_handler = DatabaseHandler('top_songs.db')
    web_parser = WebParser('https://www.shazam.com/ru-ru/charts/top-200/world')
    ui = UserInterface(db_handler, web_parser)
    ui.run()
    db_handler.close_connection()
