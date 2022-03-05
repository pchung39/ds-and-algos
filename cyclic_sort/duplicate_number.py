def duplicate_number(arr):

    i = 0

    while i < len(arr):
        if arr[i] != i + 1:
            j = arr[i] - 1
        
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 
            else:
                return arr[i]
        else:
            i += 1
    
    return -1

print(duplicate_number([1, 4, 4, 3, 2]))
print(duplicate_number([2, 1, 3, 3, 5, 4]))