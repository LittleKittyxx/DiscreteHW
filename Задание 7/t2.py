import math
from t1 import pow_fast


def dlog_bruteforce(a, b, mod):
    mult_count = 0
    cur = 1

    for x in range(mod):
        if cur == b:
            return x, mult_count
        cur = (cur * a) % mod
        mult_count += 1

    return None, mult_count


def dlog_shanks(a, b, mod):
    m = int(math.sqrt(mod)) + 1
    mult_count = 0

    baby_steps = {}
    cur = 1
    for j in range(m):
        baby_steps[cur] = j
        cur = (cur * a) % mod
        mult_count += 1

    a_inv_m, cnt = pow_fast(pow(a, -1, mod), m, mod)
    mult_count += cnt

    cur = b
    for i in range(m):
        if cur in baby_steps:
            return i * m + baby_steps[cur], mult_count
        cur = (cur * a_inv_m) % mod
        mult_count += 1

    return None, mult_count
