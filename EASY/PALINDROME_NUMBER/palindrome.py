class Answer:
    def __init__(self, number):
        self.number = number
    
    def is_palindrome(self):
        if self.number < 0 or (self.number % 10 == 0 and self.number != 0):
            return False # Negative numbers and numbers ending with 0 (except 0 itself) cannot be palindromes
        
        original_number = str(self.number) # Convert the number to a string to check for palindrome
        reversed_number = original_number[::-1] # Reverse the string using slicing
        return original_number == reversed_number # Check if the original string is the same as the reversed string
    

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    answer = Answer(number)
    if answer.is_palindrome():
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")