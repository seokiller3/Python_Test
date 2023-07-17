number = int(input("Введите целое число от 1 до 100000: "))

if number <= 1:
    print("Число должно быть больше 1")
elif number > 100000:
    print("Число должно быть меньше 100000")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} - простое число")
    else:
        print(f"{number} - составное число")
