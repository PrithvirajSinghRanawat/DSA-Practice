class Answer:
    def reversedigits(self, number):
        return int(str(number)[::-1]) # Convert the number to a string, reverse it using slicing, and convert it back to an integer.
    
a = Answer()
print(f"Reversedigits (1234) = {a.reversedigits(1234)}") # Output: 4321
print(f"Reversedigits (987654321) = {a.reversedigits(987654321)}") # Output: 123456789
print(f"Reversedigits (1000) = {a.reversedigits(1000)}") # Output: 1 (leading zeros are removed) 