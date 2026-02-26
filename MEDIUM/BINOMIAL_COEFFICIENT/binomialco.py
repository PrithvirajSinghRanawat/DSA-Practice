n = 5
k = 2

def binomialCoefficient(n, k):
    # n cannot be greater than k
    if k > n:
        return 0
    
    # base condition when n and k are equal or k is 0
    if k == 0 or k == n:
        return 1
    
    # Recursive approach to find the binomial coefficient
    # Calculate the binomial coefficient using recursive formula
    return binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1, k)


result = binomialCoefficient(n, k)
print(f"The value of C({n}, {k} is {result})")