def check_age(age):
    assert age >= 18, "Вам має бути 18 років або більше"
    print("Ви можете використовувати цей сервіс")

def process_list(input_list):
    assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
    print(f"Список містить {len(input_list)} елементів")

try:
    check_age(20)
    check_age(16)
except AssertionError as e:
    print(e)

try:
    process_list([1, 2, 3])
    process_list([1])
except AssertionError as e:
    print(e)

