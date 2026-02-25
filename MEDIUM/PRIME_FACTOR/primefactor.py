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

num = int(input("Enter a number: "))
factors_list = prime_factor(num)
print("Factors of", num, "are:", factors_list)

# LARGEST PRIME FACTOR OF AN INTEGER.

#     largest_prime_factor = max(factors) if factors else None
#     return largest_prime_factor

# if __name__ == "__main__":
#     num = int(input("Enter a number: "))
#     factors_list = prime_factor(num)
#     print("Largest Prime Factor:", prime_factor(factors_list))