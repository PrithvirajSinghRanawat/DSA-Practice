arr = [1, 0, 99, 23, 0, 1, 2, 0]

def move_zeroes(arr):
    left = 0
    count = 0

    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    arr[:left] = sorted(arr[:left])

    return arr

print(move_zeroes(arr))