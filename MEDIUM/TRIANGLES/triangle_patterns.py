def right_triangle(n):
    """
    Returns a right triangle based pattern.
    """
    for i in range(1, n + 1):
        print("* " * i)
    

def inverted_right_triangle(n):
    """
    Returns an inverted right triangle based pattern.
    """
    for i in range(n, 0, -1):
        print("* " * i)


def left_aligned_triangle(n):
    """
    Returns a left aligned triangle based pattern.
    """
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)
    

def pyramid(n):
    """
    Returns a pyramid based pattern.
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (i))
    

def inverted_pyramid(n):
    """
    Returns an inverted pyramid based pattern.
    """
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * (i))
    

def diamond(n):
    """
    Returns a diamond based pattern.
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (i))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * (i))
    

def number_triangle(n):
    """
    Returns a numbered right angle triangle.
    """
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print (j, end = " ")
        print()
    

def repeated_number_triangle(n):
    """
    Returns a repeated numbered right angle triangle.
    """
    for i in range(1, n + 1):
        print ((str(i) + " ") * i) 
    

def floyd_triangle(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
    

# floyd_triangle(5)
# repeated_number_triangle(5)
# number_triangle(5)
# diamond(5)
# inverted_pyramid(5)
# pyramid(5)
# left_aligned_triangle(5)
# inverted_right_triangle(5)
# right_triangle(5)