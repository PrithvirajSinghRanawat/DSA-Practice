def to_decimal(numerator, denominator):
    """
    Converts a fraction given by numerator and denominator into its decimal representation.
    If the decimal representation is repeating, the repeating part is enclosed in parentheses.
    """
    if numerator == 0:
        return 0
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.") # Handle division by zero case
    
    result = "-" if (numerator < 0) ^ (denominator < 0) else "" # Determine the sign of the result, using XOR to check if one of them is negative

    numerator, denominator = abs(numerator), abs(denominator)
    
    result += str(numerator // denominator) # Append the integer part of the division to the result
    remainder = numerator % denominator # Calculate the initial remainder after extracting the integer part
    if remainder == 0:
        return result
    result += "." # Append the decimal point to the result if there is a remainder
    decimal_map = {}
    while remainder != 0: 
        if remainder in decimal_map: # Check if the current remainder has been seen before, indicating a repeating decimal
            result = result[:decimal_map[remainder]] + "(" + result[decimal_map[remainder]:] + ")" # Enclose the repeating part of the decimal in parentheses
            break
        decimal_map[remainder] = len(result)
        remainder *= 10 # Multiply the remainder by 10 to get the next digit in the decimal representation
        result += str(remainder // denominator) # Append the next digit of the decimal representation to the result
        remainder %= denominator # Update the remainder for the next iteration
    return result


numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
decimal_representation = to_decimal(numerator, denominator)
print(f"The decimal representation of {numerator}/{denominator} is: {decimal_representation}")