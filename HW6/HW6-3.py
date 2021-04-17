def is_prime(value):
    if value == 1:
        return False
    d = 2
    while d * d <= value and value % d != 0:
        d += 1
    return d * d > value
