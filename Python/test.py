from math import sqrt


def is_square(n):
    if n < 0:
        return False
    return (True if sqrt(n) % 1 == 0 else False)


print(is_square(0))
