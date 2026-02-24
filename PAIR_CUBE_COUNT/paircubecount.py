class Answer:

    def count_pairs(self, number):
        count = 0
        for a in range(1, number + 1): # We can start from 1 since 0^3 is 0 and won't contribute to the count
            for b in range(number + 1): # We can start from 0 since b can be 0 and still contribute to the count
                if a**3 + b**3 == number: # Check if the sum of cubes equals the given number
                    count += 1 # Increment the count if a valid pair is found
        return count


a = Answer()
print(f"Number of pairs for 9 is {a.count_pairs(9)}")
print(f"Number of pairs for 28 is {a.count_pairs(28)}")