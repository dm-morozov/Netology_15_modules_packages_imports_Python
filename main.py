from pathlib import Path
from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from faker import Faker

def tast_one():
    print(f"\n Задание номер 1 и 2: \n")
    calculate_salary()
    get_employees()

def task_three():
    print(f"\n Задание номер 3: \n")
    current_datetime = datetime.today()
    formatted_date = current_datetime.strftime("%Y-%B-%d")
    formatted_time = current_datetime.strftime("%H:%M")
    print(f"Сегодня: {formatted_date}\nМестное время: {formatted_time}")

def task_four():
    print(f"\n Задание номер 4: \n")
    path = Path(".").absolute()
    print("Выводим абсолютный путь к текущей директории:", path)

    fake = Faker()
    print("\n Рандомное имя:", fake.name(), "\n")
    print("\n Рандомный адрес:", fake.address(), "\n")
    print("\n Рандомный текст:\n", fake.text(), "\n")

if __name__ == "__main__":

    tast_one()

    task_three()

    task_four()

if __name__ == "main":
    print(f"Код котрый мы запустили из стороннего модуля \n")
    print("Код расположенный внутри модуля:", __name__, "\n")
    