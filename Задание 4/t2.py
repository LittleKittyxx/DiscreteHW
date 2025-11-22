def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")


print("От 1 до N:", end=" ")
print_1_to_n(5)


def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)


print("\nОт N до 1:", end=" ")
print_n_to_1(5)


def print_even(n):
    if n == 0:
        return
    print_even(n - 1)
    if n % 2 == 0:
        print(n, end=" ")


print("\nЧётные числа:", end=" ")
print_even(10)
