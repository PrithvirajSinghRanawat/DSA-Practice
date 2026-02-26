heights = [2, 1, 12, 8, 2, 4, 16, 3]

def maximum_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        min_height = min(heights[left], heights[right])
        area = min_height * width

        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(maximum_area(heights))