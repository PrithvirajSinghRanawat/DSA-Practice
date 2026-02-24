def sqrt_num(number):
    """
    This function calculates the integer part of the square root 
    of a given non-negative integer using binary search.
    """
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if number == 0 or number == 1:
        return number
    
    low = 0
    high = number
    answer = 0
    while low <= high:
        mid = (low + high) // 2 # Calculate the middle point
        square = mid * mid
        if square == number: # If the square of mid is equal to the number, we found the exact square root
            return mid
        elif square < number: # If the square of mid is less than the number, we need to search in the right half
            low = mid + 1
            answer = mid 
        else:                # If the square of mid is greater than the number, we need to search in the left half
            high = mid - 1
    return answer  # Return the largest integer whose square is less than or equal to the number, which is the integer part of the square root.


number = int(input("Enter a number to find its square root: "))
result = sqrt_num(number)
print(f"The square root of {number} is approximately: {result}")