def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle up to nth row.
    """
    triangle = []
    for row in range(1, n + 1):
        c = 1
        current_row = []
        for i in range(1, row + 1):
            print(c, end=" ")
            current_row.append(c)
            c = c * (row - i) // i

        triangle.append(current_row)

    # Print the triangle after the function returns
    for row in triangle:
        print(" ".join(map(str, row)))
    return triangle

n = int(input("Enter the number of rows: "))
result = pascal_triangle(n)
print(result)




