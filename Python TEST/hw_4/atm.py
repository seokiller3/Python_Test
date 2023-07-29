"""
Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""


def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    return max(30, min(fee, 600))


def deposit(balance, amount, operations):
    if amount % 50 == 0:
        balance += amount
        operations.append(f"Пополнение: +{amount} у.е.")
    else:
        print("Сумма пополнения должна быть кратной 50 у.е.")
    return balance


def withdraw(balance, amount, operations):
    if amount % 50 == 0:
        if amount <= balance:
            withdrawal_fee = calculate_withdrawal_fee(amount)
            balance -= (amount + withdrawal_fee)
            operations.append(f"Снятие: -{amount} у.е. (включая комиссию {withdrawal_fee} у.е.)")
        else:
            print("Недостаточно средств на счете.")
    else:
        print("Сумма снятия должна быть кратной 50 у.е.")
    return balance


def main():
    balance = 0
    total_operations = 0
    wealth_tax = 0
    operations = []

    while True:
        print("Доступные действия:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            deposit_amount = int(input("Введите сумму для пополнения (кратную 50 у.е.): "))
            balance = deposit(balance, deposit_amount, operations)
            total_operations += 1
            if total_operations % 3 == 0:
                balance *= 1.03
        elif choice == '2':
            withdrawal_amount = int(input("Введите сумму для снятия (кратную 50 у.е.): "))
            balance = withdraw(balance, withdrawal_amount, operations)
            total_operations += 1
            if total_operations % 3 == 0:
                balance *= 1.03
            if balance > 5000000:
                wealth_tax = balance * 0.1
                balance -= wealth_tax
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Повторите попытку.")

        print(f"Текущий баланс: {balance:.2f} у.е.")
        if wealth_tax > 0:
            print(f"Сумма налога на богатство: {wealth_tax:.2f} у.е.")

    print("\nСписок операций:")
    for operation in operations:
        print(operation)

    print("Спасибо за использование банкомата!")


if __name__ == "__main__":
    main()
