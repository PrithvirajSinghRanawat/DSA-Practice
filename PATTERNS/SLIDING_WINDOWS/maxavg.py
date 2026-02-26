nums = [1, 2, 5, 9, 2, 4, 10, 5, 2, 1]
k = 3

def max_average(nums, k):
    sum_window = sum(nums[:k])
    max_avg = sum_window
    for i in range(k, len(nums)):
        sum_window += nums[i] - nums[i-k]
        max_avg = max(max_avg, sum_window)
                      
    return max_avg / k


print(max_average(nums, k))