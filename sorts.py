import logging
from datetime import datetime

# Пузырьковая сортировка
logging.basicConfig(level=logging.INFO, filename="my_log.log",filemode="w",  format="%(asctime)s %(levelname)s %(message)s")

time_1 = datetime.now().strftime("%H:%M:%S:%f")
print("Начало bubble sort:",time_1)
k1 = 0
def bubble_sort(nums):
    global k1
    logging.info(f"bubble_sort:{datetime.now().strftime('%H:%M:%S:%f')}")
    swapped = True

    while swapped:
        logging.info(f"Starting the cycle, {nums}")
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                k1 = k1 + 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    logging.info(f"The end of the cycle")
random_list_of_nums = [6, 3, 8, 1, 4]
bubble_sort(random_list_of_nums)
time_2 = datetime.now().strftime("%H:%M:%S:%f")
print("Конец bubble_sort: ",time_2)
print('Разница времени в микросекундах:',int(time_2[-6:]) - int(time_1[-6:]))
print("Результат:", random_list_of_nums)
print("Количество перестановок:", k1)
print()

# Сортировка выборкой
time_3 = datetime.now().strftime("%H:%M:%S:%f")
print('Начало selection_sort',time_3)
k2 = 0
def selection_sort(nums):
    global k2
    logging.info(f"selection_sort:{nums}")
    for i in range(len(nums)):
        logging.info(f"Starting the cycle, {nums}")
        minim = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minim]:
                minim = j
        if minim != i:
            k2 += 1
        nums[i], nums[minim] = nums[minim], nums[i]
        logging.info(f"The end of the cycle")
list_of_nums = [12, 8, 3, 20, 11]
selection_sort(list_of_nums)
time_4 = datetime.now().strftime("%H:%M:%S:%f")
print('Конец selection_sort',time_4)
print('Разница времени в микросекундах:',int(time_4[-6:]) - int(time_3[-6:]))
print("Результат:", list_of_nums)
print("Количество перестановок:", k2)
print()

# Сортировка вставками
time_5 = datetime.now().strftime("%H:%M:%S:%f")
print('Начало insertion_sort',time_5)
k3 = 0
def insertion_sort(nums):
    global k3
    logging.info(f"insertion_sort:{nums}")
    for i in range(1, len(nums)):
        logging.info(f"Starting the cycle, {nums}")
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            k3 += 1
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
        logging.info(f"The end of the cycle")
random_list_of_nums = [10, 15, 20, 2, 5, 9]
insertion_sort(random_list_of_nums)
time_6 = datetime.now().strftime("%H:%M:%S:%f")
print('Конец insertion_sort',time_6)
print('Разница времени в микросекундах:',int(time_6[-6:]) - int(time_5[-6:]))
print("Результат:", random_list_of_nums)
print("Количество сдвигов:", k3)
print()

# Пирамидальная сортировка
k4 = 0
def heapify(nums, heap_size, maxidx):
    global k4
    logging.info(f"heapify:{nums}")
    large = maxidx
    logging.info("Starting the cycle")
    left = (2 * maxidx) + 1
    right = (2 * maxidx) + 2

    if left < heap_size and nums[left] > nums[large]:
        large = left

    if right < heap_size and nums[right] > nums[large]:
        large = right

    if large != maxidx:
        k4 += 1
        nums[maxidx], nums[large] = nums[large], nums[maxidx]
        heapify(nums, heap_size, large)

time_7 = datetime.now().strftime("%H:%M:%S:%f")
print('Начало heap_sort',time_7)
def heap_sort(nums):
    global k4
    logging.info(f"heap_sort:{nums}")
    n = len(nums)
    logging.info("Starting the cycle")
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        k4 += 1
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    logging.info(f"The end of the cycle")
random_list_of_nums = [28, 59, 3, 15, 20]
heap_sort(random_list_of_nums)
time_8 = datetime.now().strftime("%H:%M:%S:%f")
print('Конец heap_sort',time_8)
print('Разница времени в микросекундах:',int(time_8[-6:]) - int(time_7[-6:]))
print("Результат:", random_list_of_nums)
print("Количество перестановок:", k4)
print()

# Сортировка слиянием
k5 = 0
def merge(left_list, right_list):
    global k5
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        k5 += 1
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

time_9 = datetime.now().strftime("%H:%M:%S:%f")
print('Начало merge_sort',time_9)
def merge_sort(nums):
    logging.info(f"merge_sort:{nums}")
    logging.info("Starting the cycle")
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

random_list_of_nums = [281, 243, 901, 234, 494]
random_list_of_nums = merge_sort(random_list_of_nums)
time_10 = datetime.now().strftime("%H:%M:%S:%f")
print('Конец merge_sort',time_10)
print('Разница времени в микросекундах:',int(time_10[-6:]) - int(time_9[-6:]))
print("Результат:", random_list_of_nums)
print("Количество операций слияния:", k5)
print()

# Быстрая сортировка
k6 = 0
def partition(nums, low, high):
    global k6
    logging.info(f"partition:{nums}")
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    logging.info("Starting the cycle")
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        k6 += 1
        nums[i], nums[j] = nums[j], nums[i]

time_11 = datetime.now().strftime("%H:%M:%S:%f")
print('Начало quick_sort',time_11)
def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    logging.info(f"The end of the cycle: {nums}")

random_list_of_nums = [57, 70, 34, 29, 89]
quick_sort(random_list_of_nums)
time_12 = datetime.now().strftime("%H:%M:%S:%f")
print('Конец quick_sort',time_12)
print('Разница времени в микросекундах:',int(time_12[-6:]) - int(time_11[-6:]))
print("Результат:", random_list_of_nums)
print("Количество перестановок:", k6)
print()
print("Количество итераций на различнх сортировках")
print(f"Пузырьковая сортировка: {k1} перестановок")
print(f"Сортировка выборкой: {k2} перестановок")
print(f"Сортировка вставками: {k3} сдвигов")
print(f"Пирамидальная сортировка: {k4} перестановок")
print(f"Сортировка слиянием: {k5} операций слияния")
print(f"Быстрая сортировка: {k6} перестановок")