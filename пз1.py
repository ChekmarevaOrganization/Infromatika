# 1. Задание 1
print("Привет! Добро пожаловать, Алекс!")

# 2. Задание 2
name = input("Как тебя зовут? ")
print(f"Привет, {name}!")

# 3. Задание 3
print("\nЗадание 3: Сумма двух чисел")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print(f"Сумма {a} + {b} = {a + b}")

# 4. Задание 4
print("\nЗадание 4: Арифметические операции")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0:
    print(f"{a} / {b} = {a / b}")
    print(f"Целочисленное деление: {a} // {b} = {a // b}")
    print(f"Остаток от деления: {a} % {b} = {a % b}")
else:
    print("Деление на ноль невозможно!")
print(f"Возведение в степень: {a} ** {b} = {a ** b}")

# 5. Задание 5
print("\nЗадание 5: Чётное или нечётное?")
num = int(input("Введите целое число: "))
if num % 2 == 0:
    print(f"Число {num} — чётное")
else:
    print(f"Число {num} — нечётное")

# 6. Задание 6
print("\n--- Задание 6: Знак числа ---")
x = int(input("Введите число: "))
if x > 0:
    print(f"Число {x} — положительное")
elif x < 0:
    print(f"Число {x} — отрицательное")
else:
    print("Число равно нулю")

# 7. Задание 7
print("\nЗадание 7: Таблица умножения")
n = int(input("Введите число для таблицы умножения: "))
print(f"Таблица умножения для {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 8. Задание 8
print("\nЗадание 8: Факториал")
def factorial(x):
    if x < 0:
        return None
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

m = int(input("Введите число для вычисления факториала: "))
if m < 0:
    print("Факториал отрицательного числа не определён.")
else:
    print(f"{m}! = {factorial(m)}")

# 9. Задание 9
print("\nЗадание 9: Простое число?")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

p = int(input("Введите число для проверки на простоту: "))
if is_prime(p):
    print(f"Число {p} — простое")
else:
    print(f"Число {p} — составное")

# 10. Задание 10
print("\nЗадание 10: Минимум и максимум из трёх чисел")
x1 = float(input("Введите первое число: "))
x2 = float(input("Введите второе число: "))
x3 = float(input("Введите третье число: "))

minimum = min(x1, x2, x3)
maximum = max(x1, x2, x3)

print(f"Наименьшее число: {minimum}")
print(f"Наибольшее число: {maximum}")
