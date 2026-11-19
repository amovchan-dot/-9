import math

area = float(input("Введіть площу квадрата: "))

if area > 0:
    a = math.sqrt(area)
    perimeter = 4 * a
    print(f"Периметр квадрата: {perimeter:.2f}")
else:
    print("Площа повинна бути додатною!")