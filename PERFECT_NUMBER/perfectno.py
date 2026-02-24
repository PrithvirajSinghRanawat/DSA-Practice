class Answer:
    def __init__(self, number):
        self.number = number
    
    def perfect_number(self):
        sum = 0
        for i in range(1, self.number):
            if self.number % i == 0:
                sum += i
        return sum == self.number
    

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    answer = Answer(number)
    if answer.perfect_number():
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")