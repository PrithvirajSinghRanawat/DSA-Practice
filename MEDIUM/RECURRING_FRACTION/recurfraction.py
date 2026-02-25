def recurring_fraction(num, deno):  # Function to find recurring decimal pattern in a fraction
    """
    This function finds if the fraction has a recurring sequence.
    """
    if deno == 0:  # Handle division by zero case
        return "Undefined"

    integer_part = num // deno  # Extract the integer part
    remainder = num % deno  # Get the remainder for decimal calculation

    if remainder == 0:  # Check if the fraction is a terminating decimal
        return str(integer_part)

    seen = {}  # Dictionary to track seen remainders and their positions
    decimals = []  # List to store decimal digits

    while remainder != 0:  # Continue until remainder becomes zero or a pattern is found
        if remainder in seen:  # Check if this remainder appeared before (indicates recursion)
            start = seen[remainder]  # Get starting position of recurring sequence
            non_repeat = "".join(decimals[:start])  # Extract non-repeating part
            repeat = "".join(decimals[start:])  # Extract repeating part
            decimal_form = f"{integer_part}.{non_repeat}({repeat})"  # Format with recurring notation
            return decimal_form, repeat

        seen[remainder] = len(decimals)  # Store the position where this remainder first appeared
        remainder *= 10  # Multiply remainder by 10 for long division
        digit = remainder // deno  # Calculate the next digit
        decimals.append(str(digit))  # Add digit to decimal sequence
        remainder %= deno  # Update remainder for next iteration

    
    decimal_form = f"{integer_part}." + "".join(decimals)  # Format as regular decimal if no recursion
    return decimal_form, None


num = int(input("Enter numerator: "))  # Get numerator input from user
deno = int(input("Enter denominator: "))  # Get denominator input from user

decimal_result, recurring_seq = recurring_fraction(num, deno)  # Call function to find recurring decimal

print("Decimal form:", decimal_result)  # Display the decimal representation

if recurring_seq:  # Check if a recurring sequence was found
    print("Recurring sequence is", recurring_seq)  # Display the repeating part
else:  # If no recurring sequence
    print("No recurring sequence")  # Indicate it's a terminating decimal