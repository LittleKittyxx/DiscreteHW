import time
from t1 import pow_naive, pow_fast
from t2 import dlog_bruteforce, dlog_shanks
from e import diffie_hellman


def run_tests():
    print("ВОЗВЕДЕНИЕ В СТЕПЕНЬ\n")

    a, n, mod = 5, 100000, 1000000007

    start = time.time()
    _, c1 = pow_naive(a, n, mod)
    t1 = time.time() - start

    start = time.time()
    _, c2 = pow_fast(a, n, mod)
    t2 = time.time() - start

    print("Метод\t\tУмножения\tВремя")
    print(f"Наивный\t\t{c1}\t\t{t1:.6f}")
    print(f"Быстрый\t\t{c2}\t\t{t2:.6f}")

    print("\nДИСКРЕТНЫЙ ЛОГАРИФМ\n")

    a, x, mod = 2, 1234, 10007
    b, _ = pow_fast(a, x, mod)

    start = time.time()
    _, c3 = dlog_bruteforce(a, b, mod)
    t3 = time.time() - start

    start = time.time()
    _, c4 = dlog_shanks(a, b, mod)
    t4 = time.time() - start

    print("Метод\t\tУмножения\tВремя")
    print(f"Перебор\t\t{c3}\t\t{t3:.6f}")
    print(f"Шэнкс\t\t{c4}\t\t{t4:.6f}")

    print("\nДИФФИ — ХЕЛЛМАН\n")

    p = 10007
    g = 5
    a = 123
    b = 456

    k1, k2 = diffie_hellman(p, g, a, b)
    print("Ключ 1:", k1)
    print("Ключ 2:", k2)


if __name__ == "__main__":
    run_tests()


"""

ВОЗВЕДЕНИЕ В СТЕПЕНЬ

Метод           Умножения       Время
Наивный         100000          0.007178
Быстрый         23              0.000010

ДИСКРЕТНЫЙ ЛОГАРИФМ

Метод           Умножения       Время
Перебор         1234            0.000085
Шэнкс           124             0.000036

ДИФФИ — ХЕЛЛМАН

Ключ 1: 7227
Ключ 2: 7227

"""
