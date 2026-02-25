def catalan_number(num):
    """
    Calculate the nth Catalan number.
    """
    result = 1
    for i in range(2, num + 1):
        result = (result * (4 * i - 2)) // (i + 1) # formula of catalan number
    return result


num = int(input("Enter number: "))

for i in range(num + 1):
    print(f"Catalan({i}) = {catalan_number(i)}")