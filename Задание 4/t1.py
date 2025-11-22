def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


print("Сумма цифр (12345):", sum_digits(12345))


def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum_digits(n))


print("Цифровой корень (9876):", digital_root(9876))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Факториал (6):", factorial(6))
