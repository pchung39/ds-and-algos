def find_all_duplicates(nums):

    # # variables
    # i = 0 

    # # number range is 1 to n
    # # boundaries
    # while i < len(arr) - 1:
        
    #     # store value in position in variable for later
    #     curr_value = arr[i] - 1

    #     # check if the value in the i position is in the correct place
    #     if arr[i] != arr[curr_value]:
    #         arr[i], arr[curr_value] = arr[curr_value], arr[i]
    #         # if no, swap 
    #     else:
    #         i += 1

    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    duplicateNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


def main():

    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()