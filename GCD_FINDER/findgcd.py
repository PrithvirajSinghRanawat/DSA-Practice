
from math import gcd


class Answer:
    def gcd(self, num1, num2):
        if num1 == 0:
            return num2
        if num2 == 0:
            return num1
        if num1 == num2:
            return num1
        
        if num1 > num2:
            return gcd(num1 - num2, num2)
        return gcd(num1, num2 - num1)
    

a = Answer()
print("The GCD of 48 and 18 is:", a.gcd(48, 18))
print("The GCD of 56 and 98 is:", a.gcd(56, 98))