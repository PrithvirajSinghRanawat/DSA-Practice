s = "abc"

def power_set(s):
    """
    Calculate the power set of a given string s.
    """
    n = len(s)
    result = []
    total = 2**n # Total number of subsets

    for num in range(total):
        subset = []
        temp = num
        for i in range(n):
            # Check whether current position should include the character
            if temp % 2 == 1:
                subset.append(s[i])
            temp //= 2
        result.append("".join(subset))
    return result

print(power_set(s))