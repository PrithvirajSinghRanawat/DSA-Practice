# To find the series of the first n numbers in the sequence
from findnthnumber import Answer as fn

class Answer:
    def __init__(self, number):
        self.number = number
    
    def find_series(self, n):
        series = []
        for i in range(1, n + 1):
            nth_number = fn(i).find_nth_number(i)
            series.append(nth_number)
        return series
    
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    answer = Answer(n)
    result = answer.find_series(n)
    print(f"The series of the first {n} numbers in the sequence is: {result}")