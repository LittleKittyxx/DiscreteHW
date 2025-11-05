import random

nums = sorted(random.randint(1, 99) for _ in range(10))


def binary_search(sorted_arr, key):
    comparisons = 0
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        guess = sorted_arr[mid]

        if guess == key:
            return mid, comparisons
        elif guess > key:
            high = mid - 1
        else:
            low = mid + 1

    return -1, comparisons


print("Список чисел:", nums)
value = int(input("Введите число: "))
found, tries = binary_search(nums, value)
print(f"Найдено ли число: {found}, количество итераций: {tries}")
