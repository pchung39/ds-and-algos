def duplicate_number(arr):

    i = 0

    while i < len(arr):
        # that the range is 1 to n, not 0 to n.
        if arr[i] != i + 1:
            j = arr[i] - 1
        
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 
            # crucial piece of puzzle, if arr[i] == arr[j] then the correct value is already in the correct position
            # therefore the current number is the duplicate
            else:
                return arr[i]
        else:
            i += 1
    
    return -1

print(duplicate_number([1, 4, 4, 3, 2]))
print(duplicate_number([2, 1, 3, 3, 5, 4]))