"""
Создайте модуль и напишите в нём функцию,
которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может
существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует
Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def is_leap_year(year):
    """Проверяет, является ли год високосным."""
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def is_valid_date(date_str):
    """Проверяет, является ли дата допустимой."""
    try:
        day, month, year = map(int, date_str.split('.'))
        if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1:
            return False

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if is_leap_year(year):
            days_in_month[2] = 29

        return day <= days_in_month[month]

    except ValueError:
        return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python date_validator.py <date>")
    else:
        date = sys.argv[1]
        if is_valid_date(date):
            print("Дата допустима.")
        else:
            print("Дата недопустима.")
