import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def measure_time(func, n, func_name):
    logging.info(f"Начало вычисления {func_name} для n={n}")
    start_time = time.perf_counter()
    result = func(n)
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    logging.info(f"{func_name} завершена: результат = {result}, время = {elapsed:.9f} секунд")
    return result, elapsed

def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            total += item
    return total

if __name__ == "__main__":
    n = 35

    result_iter, time_iter = measure_time(fibonacci_iterative, n, "Итеративная функция")

    result_rec, time_rec = measure_time(fibonacci_recursive, n, "Рекурсивная функция")

    print("Сравнение времени выполнения:")
    print(f"Итеративно: {time_iter:.6f} сек")
    print(f"Рекурсивно: {time_rec:.6f} сек")
    if time_iter > 0:
        print(f"Рекурсивный вариант медленнее в {time_rec / time_iter:.1f} раз!")


    if result_iter == result_rec:
        print("Результаты совпадают")
    else:
        print("Ошибка: результаты разные")

    test_list = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]
    result_sum = recursive_sum(test_list)
    print(f"\nСумма всех чисел в списке {test_list} = {result_sum}")