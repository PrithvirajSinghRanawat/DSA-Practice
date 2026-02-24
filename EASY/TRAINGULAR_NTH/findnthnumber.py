class Answer:
    def __init__(self, number):
        self.number = number
    
    def find_nth_number(self, n):
        value = 0
        for i in range(1, n + 1): 
            value += i
        return value
    

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    answer = Answer(n)
    result = answer.find_nth_number(n)
    print(f"The {n}th number in the sequence is: {result}")