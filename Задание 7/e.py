from t1 import pow_fast


def diffie_hellman(p, g, a, b):
    A, _ = pow_fast(g, a, p)
    B, _ = pow_fast(g, b, p)

    key1, _ = pow_fast(B, a, p)
    key2, _ = pow_fast(A, b, p)

    return key1, key2
