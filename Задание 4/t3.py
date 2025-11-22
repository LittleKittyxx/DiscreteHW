def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print("НОД двух чисел (48, 18):", gcd(48, 18))
