class Answer:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)
    
    def lcm(self, a, b):
        return (a // self.gcd(a, b) * b)
    

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    answer = Answer(num1, num2)
    print(f"The LCM of {num1} and {num2} is: {answer.lcm(num1, num2)}")