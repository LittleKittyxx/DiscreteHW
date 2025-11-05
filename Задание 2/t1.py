import random

nums = [random.randint(1, 99) for _ in range(10)]


def sequential_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    
    return -1, comparisons


print("Список чисел:", nums)
user_input = int(input("Введите число: "))
pos, steps = sequential_search(nums, user_input)
print(f"Индекс: {pos}, количество итераций: {steps}")
