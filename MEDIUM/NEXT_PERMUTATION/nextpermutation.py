def next_permutation(arr):
    """
    Finds the next lexicographically greater permutation of a given array.
    """
    n = len(arr)
    
    # Find the largest index i such that arr[i] < arr[i+1].
    i = n - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1

    # If no such index exists, then the permutation is the last one.
    if i == -1:
        arr.reverse()
        return arr
    
    # Find the smallest index j > i such that arr[j] < arr[i].
    j = n - 1
    while j  > i and arr[j] <= arr[i]:
        j -= 1

    # Swap arr[i] and arr[j].
    arr[i], arr[j] = arr[j], arr[i]


    # Reverse the elements after index i + 1.
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr

arr = list(map(int, input("Enter elements of array separated by space : ").split()))
print(f"Next permutation is : {next_permutation(arr)}")