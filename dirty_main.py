from application.salary import *
from application.db.people import *
from main import *


if __name__ == "__main__":
    print(f"Запустили модуль dirty_main напрямую \n")
    calculate_salary()
    get_employees()
    tast_one()
    task_three()
    task_four()

    print(f"Закончили модуль dirty_main напрямую \n")
    print(f"Плохая практика написания кода, а именно вызов функций или классов методом * из других модулей \n")