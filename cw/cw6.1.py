# zad1
users = {
    "Nick": "19-29",
    "James": "24-27",
    "Charlie": "46-47"
}

name = input("Напишіть імя юзера:")
age_group = users.get(name)

try:
    age_group = users[name]
    print(f"Вікова група юзера {name}: {age_group}")
except KeyError:
    print(f"В базі данних такого юзера не знайдено.")

#zad2
try:
    number = int(input("Введіть число: "))
    print(f"Введене число: {number}")
except ValueError:
    print("Error 404: це не число")

#zad3
file_path = input("Введіть шлях до файлу:")
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("Вміст файлу")
        print(content)

except FileNotFoundError:
    print("Error 404: Файл не знайдено.")