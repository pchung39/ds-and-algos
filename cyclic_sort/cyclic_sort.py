    def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        # store value in position in its own variable 
        j = nums[i] - 1

        # if i and j are not equal, it means that the right value is not in the position
        # note that this step continues to happen until the correct value is in the right position
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums


def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()