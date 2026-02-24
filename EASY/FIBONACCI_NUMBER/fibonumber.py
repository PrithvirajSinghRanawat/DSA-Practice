class Answer:
    def __init__(self, number):
        self.number = number
    
    def fibonacci(self, n=None): # Allowing n to be passed as an argument for flexibility, but defaulting to self.number
        if n is None: 
            n = self.number

        if n < 0: # Fibonacci is not defined for negative numbers
            raise ValueError("Fibonacci is not defined for negative numbers.")

        if n <= 1:
            return n

        a, b = 0, 1 # Starting values for Fibonacci sequence
        for _ in range(2, n + 1):
            a, b = b, a + b # Update a to b and b to a + b (the next Fibonacci number)
        return b
        
if __name__ == "__main__":
    number = int(input("Enter the Fibonacci number to calculate: "))
    answer = Answer(number)
    print(f"The {number}th Fibonacci number is: {answer.fibonacci()}")
