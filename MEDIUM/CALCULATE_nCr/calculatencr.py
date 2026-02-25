def factorial(num):
    """
    Calculate the factorial of a number
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def calculate_nCr(n, r):
    """
    Function to calculate nCr using the formula: nCr = n! / (r!(n-r)!))
    """
    if r > n:
        return 0
    
    return factorial(n) // (factorial(r) * factorial(n - r))


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
result = calculate_nCr(n, r)
print(f"The result is {result}")