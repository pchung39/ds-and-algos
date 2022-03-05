def cyclic_missing_number(nums):

    # use a cyclic sort to iterate through numbers
    # need to find the missing number 

    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    # find the first number missing from its index, that will be our required number
    print(nums)
    for i in range(n):
        if nums[i] != i:
            return i

    return n

print(cyclic_missing_number([4, 0, 3, 1]))
print(cyclic_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))