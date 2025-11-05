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


def bubble_sort(arr):
    n = len(arr)
    new_arr = list(arr)
    comparisons = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if new_arr[j] > new_arr[j + 1]:
                new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]
                swapped = True

        if not swapped:
            break

    return new_arr, comparisons


def table(N_fixed=500, num_test_keys=100):
    print(f"Анализ для фиксированного размера массива N = {N_fixed}")

    arr = [random.randint(0, 10000) for _ in range(N_fixed)]

    sorted_arr, sort_comps = bubble_sort(arr)
    print(f"Стоимость сортировки (Bubble Sort): {sort_comps} сравнений")

    test_keys = [random.randint(0, 10000) for _ in range(num_test_keys)]
    total_linear_comps = 0
    total_binary_comps = 0

    for key in test_keys:
        _, linear_c = sequential_search(arr, key)
        total_linear_comps += linear_c

        _, binary_c = binary_search(sorted_arr, key)
        total_binary_comps += binary_c

    avg_linear_comps = total_linear_comps / num_test_keys
    avg_binary_comps = total_binary_comps / num_test_keys

    print(f"Средняя стоимость (1) послед. поиска: {avg_linear_comps:.2f} сравнений")
    print(f"Средняя стоимость (1) двоичного поиска: {avg_binary_comps:.2f} сравнений")

    diff = avg_linear_comps - avg_binary_comps

    if diff <= 0:
        print("\nРезультат: Ошибка. Средний линейный поиск оказался быстрее двоичного.")
        print("Это не должно происходить на больших N. Попробуйте N побольше.")
        return

    K = sort_comps / diff

    print(f"Двоичный поиск (с предварительной O(N^2) сортировкой)")
    print(f"становится эффективнее, чем {int(K) + 1} последовательных поисков.")
    print(
        f"(Расчет: K > {sort_comps} / ({avg_linear_comps:.2f} - {avg_binary_comps:.2f}), т.е. K > {K:.2f})"
    )

table()