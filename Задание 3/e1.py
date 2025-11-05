from t1 import measure_function_performance


def lcm(m: int, n: int) -> int:
    common_divisors = []

    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            common_divisors.append(i)

    gcd_value = max(common_divisors)

    return m * n // gcd_value


print(f"Массивом\n{measure_function_performance(lcm)}\n")


def lcm_scan(a: int, b: int) -> int:
    step = max(a, b)
    current = step
    while current <= a * b:
        if current % a == 0 and current % b == 0:
            return current
        current += step
    return a * b


print(f"От max(M, N) до M*N\n{measure_function_performance(lcm_scan)}\n")


def gcd_euclid_alt(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm_via_gcd(a: int, b: int) -> int:
    gcd_val = gcd_euclid_alt(a, b)
    return abs(a * b) // gcd_val if gcd_val else 0


print(f"Через НОД Евклида\n{measure_function_performance(lcm_via_gcd)}\n")
