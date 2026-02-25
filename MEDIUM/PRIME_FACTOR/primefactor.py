def prime_factor(num):
    """
    Calculate all the unique prime factors of an integer.
    """
    factors = []
    if num % 2 == 0:
        factors.append(2)
        while num % 2 == 0:
            num //= 2

    i = 3
    while i * i <= num:
        if num % i == 0:
            factors.append(i)
            while num % i == 0:
                num //= i
        i += 1

    if num > 2:
        factors.append(num)
    return factors

num = int(input("Enter an integer: "))
print(prime_factor(num))