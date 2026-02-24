class Answer:
    def isPowerOfAnother(self, num, base):
        if num <= 1 or base <= 1: #check if num and base are greater than 1
            return False

        power = 1
        while power < num: #keep multiplying the base until power is greater than or equal to num
            power *= base 

        return power == num #check if power is equal to num, if it is then num is a power of base, otherwise it is not.
    

a = Answer()
print(f"Is 16 a power of 2? = {a.isPowerOfAnother(16, 2)}") # True, because 2^4 = 16
print(f"Is 27 a power of 3? = {a.isPowerOfAnother(27, 3)}") # True, because 3^3 = 27
print(f"Is 10 a power of 2? = {a.isPowerOfAnother(10, 2)}") # False, because 10^3 = 8 and 10^4 = 16, so 10 is not a power of 2