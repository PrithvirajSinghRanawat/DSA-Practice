class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumrange(self, i, j):
        return self.prefix[j + 1] - self.prefix[i]


a = Solution([-2, 1, -3, 4])
print(a.sumrange(0, 2))