import heapq


def heap_sort(arr):
    heap = []
    sorted_arr = []

    for x in arr:
        heapq.heappush(heap, x)

    print(f"Пирамида построена: {heap}")

    while heap:
        min_val = heapq.heappop(heap)
        sorted_arr.append(min_val)

    return sorted_arr


data = [12, 1, 5, 9, 3, 7]
print("Исходный массив:", data)
result = heap_sort(data)
print("Отсортированный массив:", result)


""" 

Исходный массив: [12, 1, 5, 9, 3, 7]
Пирамида построена: [1, 3, 5, 12, 9, 7]
Отсортированный массив: [1, 3, 5, 7, 9, 12] 

"""