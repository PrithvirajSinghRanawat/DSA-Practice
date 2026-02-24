class Answer:
    def __init__(self, number):
        self.number = number

    def digital_root(self):
        num = self.number
        while num >= 10:
            num = sum(int(digit) for digit in str(num)) # Sum the digits of the number, and repeat until we get a single digit
        return num
    
        # if self.number == 0: 
        #     return 0
        # return 1 + (self.number - 1) % 9 # Alternative formula for digital root
    

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    answer = Answer(number)
    result = answer.digital_root()
    print(f"The digital root of {number} is: {result}")