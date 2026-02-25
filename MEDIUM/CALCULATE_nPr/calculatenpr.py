def factorial(num):
    """
    This function calculates the factorial of a given integer.
    """
    result = 1
    for i in range(2, num+1):
        result *= i 
    return result
    

def calculate_nPr(n, r):
    """
    Calculate the value of nPr, when n and r are given integers.
    Args:
        n (int): The total number of items.
        r (int): The number of items to choose.
    """
    return factorial(n) // factorial(n-r) 
    


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
print(f"The value of nPr is {calculate_nPr(n, r)}")