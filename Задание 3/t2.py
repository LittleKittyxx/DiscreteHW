from t1 import measure_function_performance


def is_prime_basic(num: int) -> bool:
    if num < 2:
        return False
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True


print(f"От 2 до N\n{measure_function_performance(is_prime_basic)}\n")


def is_prime_odd(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    step = 3
    while step < num:
        if num % step == 0:
            return False
        step += 2
    return True


print(f"От 2 до N четные\n{measure_function_performance(is_prime_odd)}\n")


def is_prime_sqrt(num: int) -> bool:
    if num < 2:
        return False
    limit = int(num**0.5) + 1
    for divisor in range(2, limit):
        if num % divisor == 0:
            return False
    return True


print(f"От 2 до sqrt(N)\n{measure_function_performance(is_prime_sqrt)}\n")


def is_prime_sqrt_odd(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    border = int(num**0.5) + 1
    for divisor in range(3, border, 2):
        if num % divisor == 0:
            return False
    return True


print(f"От 2 до sqrt(N) четные\n{measure_function_performance(is_prime_sqrt_odd)}\n")
