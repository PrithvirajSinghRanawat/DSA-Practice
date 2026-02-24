def kth_digit(a, b, k):
    """
    Calculate the k-th digit of a^b (1-indexed from the left).
    """
    axb = a ** b # Calculate a^b

    axb_str = str(axb)
    if k <= 0:
        return -1 # If k is less than or equal to 0, return -1
    if k > len(axb_str):
        return -1 # If k is greater than the number of digits, return -1
    return int(axb_str[k-1]) # Return the k-th digit (1-indexed)
    

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
k = int(input("Enter the value of k: "))
result = kth_digit(a, b, k)
if result == -1:
    print(f"The {k}-th digit does not exist.")
else:
    print(f"The {k}-th digit of {a}^{b} is: {result}")
