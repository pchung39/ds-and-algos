def find_subsets(nums):
  # make sure to SORT before executing core logic. this approach only works if it is sorted
  nums.sort()
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for index, currentNumber in enumerate(nums):
    # we will take all existing subsets and insert the current number in them to create 
    # new subset

    if currentNumber == nums[index - 1]:
        continue

    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set1 = list(subsets[i])
      set1.append(currentNumber)
      subsets.append(set1)

  return subsets

def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()