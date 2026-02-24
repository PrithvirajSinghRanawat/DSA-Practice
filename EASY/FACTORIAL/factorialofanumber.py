class Answer:
    def factorial(self, number):
        if number < 0:
            return "Factorial is not defined for negative numbers."

        result = 1 # Factorial of 0 and 1 is 1, and we start multiplying from 2
        for i in range(2, number + 1):
            result *= i # Multiply result by each number from 2 to the given number
        return result
        

a = Answer()
print(f"Factorial of 5 is {a.factorial(5)}")  # Output: 120
print(f"Factorial of 0 is {a.factorial(0)}")  # Output: 1
print(f"Factorial of -3 is {a.factorial(-3)}")  # Output: Factorial is not defined for negative numbers.
print(f"Factorial of 100 is {a.factorial(100)}") # Output: 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000