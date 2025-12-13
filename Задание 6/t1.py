import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def add(self, value):
        heapq.heappush(self.heap, value)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def get_max(self):
        if not self.heap:
            return None
        return max(self.heap)

    def pop_min(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def pop_max(self):
        if not self.heap:
            return None
        max_val = max(self.heap)
        self.heap.remove(max_val)
        heapq.heapify(self.heap)
        return max_val

    def print_heap(self):
        print("Текущая пирамида:", self.heap)


pq = PriorityQueue()

pq.add(10)
pq.add(4)
pq.add(15)

pq.print_heap()

print("Минимум:", pq.get_min())
print("Удален минимум:", pq.pop_min())
print("Максимум:", pq.get_max())
print("Удален максимум:", pq.pop_max())

pq.print_heap()


"""

Текущая пирамида: [4, 10, 15]
Минимум: 4
Удален минимум: 4
Максимум: 15
Удален максимум: 15
Текущая пирамида: [10]

"""
