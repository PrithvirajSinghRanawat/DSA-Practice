class Answer:
    def sumofdigits(self, number): 
        sum = 0
        # Loop through each digit in the number, convert it to an integer, and add it to the sum
        for i in str(number): # Convert the number to a string to iterate through each digit
            sum += int(i) # Convert the digit back to an integer and add it to the sum
        return sum 
    
a = Answer()
print(f"Sumofdigits (123) 1 + 2 + 3 = {a.sumofdigits(123)}") # Output: 6 (1 + 2 + 3 = 6)
print(f"Sumofdigits (456) 4 + 5 + 6 = {a.sumofdigits(456)}") # Output: 15 (4 + 5 + 6 = 15)