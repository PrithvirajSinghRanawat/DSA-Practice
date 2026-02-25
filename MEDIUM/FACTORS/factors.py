def factors(num):
    """
    Calculate and generate all the factors of a positive number.
    """
    factors_list = []
    for i in range(1, num + 1):
        if (num % i) == 0:
            factors_list.append(i)
    return sorted(factors_list)


num = int(input("Enter a positive number: "))
print("Factors of", num, "are:", factors(num))