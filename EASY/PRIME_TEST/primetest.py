class Answer:
    def isPrime(self, number):
        if number < 2:
            return False # 0 and 1 are not prime numbers
        for i in range(2, int(number**0.5) + 1): # Check for factors from 2 to the square root of the number
            if number % i == 0:
                return False # If a factor is found, the number is not prime
        return True # If no factors are found, the number is prime
    

a = Answer()
print(f"Is Prime (2) = {a.isPrime(2)}") # Output: True
print(f"Is Prime (3) = {a.isPrime(3)}") # Output: True
print(f"Is Prime (4) = {a.isPrime(4)}") # Output: False