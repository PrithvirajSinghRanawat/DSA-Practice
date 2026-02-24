def is_prime(x):
    """
    Check if a number x is prime. 
    A prime number is a natural number greater than 1 
    that cannot be formed by multiplying two smaller natural numbers.
    """
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1): # Check for factors from 2 to the square root of x
        if x % i == 0: # If x is divisible by any of these numbers, it is not prime
            return False
    return True


def divisors(numbers):
    """
    Return a list of numbers that have exactly three divisors. 
    For the number to have exactly three divisors, 
    it must be a perfect square of a prime number.
    """
    result = []
    for n in numbers:
        sqrt_x = int(n**0.5) # Calculate the integer square root of n
        if sqrt_x * sqrt_x == n and is_prime(sqrt_x): # Check if n is a perfect square and if its square root is prime
            result.append(n)
    return result


divisors_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = divisors(divisors_list)
print(result)
