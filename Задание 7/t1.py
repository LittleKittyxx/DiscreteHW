def pow_naive(a, n, mod):
    mult_count = 0
    result = 1
    for _ in range(n):
        result = (result * a) % mod
        mult_count += 1
    return result, mult_count


def pow_fast(a, n, mod):
    mult_count = 0
    result = 1
    a %= mod

    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod
            mult_count += 1
        a = (a * a) % mod
        mult_count += 1
        n //= 2

    return result, mult_count
