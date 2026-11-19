import math

a = float(input("Введіть перший катет (a): "))
b = float(input("Введіть другий катет (b): "))

if a > 0 and b > 0:

    gamma = math.radians(90)

    c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(gamma))

    sin_alpha = (a * math.sin(gamma)) / c
    sin_beta = (b * math.sin(gamma)) / c

    if 0 < sin_alpha < 1 and 0 < sin_beta < 1:
        alpha = math.degrees(math.asin(sin_alpha))
        beta = math.degrees(math.asin(sin_beta))

        if math.isclose(alpha + beta + 90, 180.0):
            p = a + b + c
            print(f"Трикутник існує (кути: {alpha:.1f}°, {beta:.1f}°, 90.0°).")
            print(f"Гіпотенуза (за т. косинусів): {c:.2f}")
            print(f"Периметр трикутника: {p:.2f}")
        else:
            print("Трикутник із такими кутами не існує.")
    else:
        print("Трикутник не існує (некоректні значення синусів кутів).")
else:
    print("Помилка: катети повинні бути додатними числами.")