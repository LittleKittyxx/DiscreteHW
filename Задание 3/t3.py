from t1 import measure_function_performance


def gcd_common_divisors(a: int, b: int) -> int:
    divisors = [d for d in range(1, min(a, b) + 1) if a % d == 0 and b % d == 0]
    return divisors[-1] if divisors else 1


print(f"Массивом\n{measure_function_performance(gcd_common_divisors)}\n")


def gcd_iterative(a: int, b: int) -> int:
    res = 1
    limit = min(a, b)
    i = 1
    while i <= limit:
        if a % i == 0 and b % i == 0:
            res = i
        i += 1
    return res


print(f"От 1 до min(M, N)\n{measure_function_performance(gcd_iterative)}\n")


def gcd_reverse_scan(a: int, b: int) -> int:
    for candidate in range(min(a, b), 0, -1):
        if a % candidate == 0 and b % candidate == 0:
            return candidate
    return 1


print(f"От min(M, N) до 1\n{measure_function_performance(gcd_reverse_scan)}\n")


def gcd_euclid_alt(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


print(f"Алгоритм Евклида\n{measure_function_performance(gcd_euclid_alt)}\n")
