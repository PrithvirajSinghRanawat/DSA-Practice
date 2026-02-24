class Answer:
    def __init__(self, number):
        self.number = number

    def to_binary(self):
        if self.number < 0:
            raise ValueError("Only non-negative integers are supported.")
        return f"{self.number:b}"
    

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    answer = Answer(number)
    print(f"The binary representation of {number} is: {answer.to_binary()}")