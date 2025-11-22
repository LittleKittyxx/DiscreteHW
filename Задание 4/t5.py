import time
from t4 import fib_recursive, fib_memo, fib_iter_array, fib_iter_on_fly


def experiment():
    n_values = [10, 20, 30, 35, 40]
    print("=== Эксперименты с Фибоначчи ===")

    for func in [fib_recursive, fib_memo, fib_iter_array, fib_iter_on_fly]:
        print(f"\nТест функции: {func.__name__}")
        for n in n_values:
            start = time.time()
            try:
                result = func(n)
                elapsed = time.time() - start
                print(f"n={n:2d} -> {result:>10d}, время = {elapsed:.6f} сек")
            except RecursionError:
                print(f"n={n:2d} -> Слишком глубокая рекурсия")
                break

experiment()