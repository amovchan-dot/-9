num = int(input("Введіть двоцифрове число: "))


abs_num = abs(num)

if 10 <= abs_num <= 99:
    tens = abs_num // 10
    units = abs_num % 10
    digit_sum = tens + units
    digit_prod = tens * units

    print(f"Десятків: {tens}")
    print(f"Одиниць: {units}")
    print(f"Сума цифр: {digit_sum}")
    print(f"Добуток цифр: {digit_prod}")
else:
    print("Помилка: введене число не є двоцифровим.")