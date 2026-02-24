class GCD:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_gcd(self):
        if not self.numbers:
            return 0

        gcd_value = self.numbers[0]
        for num in self.numbers[1:]:
            gcd_value = self.compute_gcd(gcd_value, num)

        return gcd_value

    @staticmethod
    def compute_gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    


if __name__ == "__main__":
    numbers = [48, 64, 16]
    gcd_finder = GCD(numbers)
    result = gcd_finder.find_gcd()
    print(f"The GCD of {numbers} is: {result}")