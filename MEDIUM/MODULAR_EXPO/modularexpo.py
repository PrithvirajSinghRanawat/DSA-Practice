def modular_exponentiation(x, n, M):
    """
    Function to find the modular exponentiation.    
    """
# EASY SOLUTION:
#     return (pow(x, n, M)) % M

# print(modular_exponentiation(2, 6, 10))


    result = 1
    while n >= 1:
        if n % 2 == 1: # If n is odd, then we need to multiply x with itself (raised to the power of half of n). If n is even, then we can divide n by 2 and square x. We continue this process until n becomes 0.
            result = (result * x) % M
            n -= 1
        else:
            x = (x*x) % M
            n //= 2
    return result

x = int(input("Enter the base number (x): "))
n = int(input("Enter the exponent (n): "))
M = int(input("Enter the modulus (M): "))

print(modular_exponentiation(x, n, M))