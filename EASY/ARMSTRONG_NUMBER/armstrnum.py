class Answer:
    def __init__(self, number):
        self.number = number

    def is_armstrong(self):
        num_str = str(self.number) # Convert the number to a string to iterate through its digits
        num_digits = len(num_str)
        output = 0
        for digit in num_str:
            output += int(digit) ** num_digits # Raise each digit to the power of the number of digits and add it to the output
        return output == self.number
    

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    answer = Answer(number)
    if answer.is_armstrong():
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")