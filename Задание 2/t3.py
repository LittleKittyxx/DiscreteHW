import random


def sequential_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons

    return -1, comparisons


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


def table():
    print(f"{'Размер (N)':<15} | {'Практич. послед.':<30} | {'Практич. двоич.':<30}")
    print("-" * 79)

    for N in range(20, 501, 20):
        arr = [random.randint(0, N * 10) for _ in range(N)]

        key = random.randint(0, N * 10)

        _, linear_comps = sequential_search(arr, key)

        sorted_arr = sorted(arr)
        _, binary_comps = binary_search(sorted_arr, key)

        print(f"{N:<15} | {linear_comps:<30} | {binary_comps:<30}")


table()
