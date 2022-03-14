from heapq import *

def find_sum_of_elements(nums, k1, k2):

    # k1th smallest and k2th smallest, can interpret as positions in the array 

    nums.sort()

    sum = 0
    for x in range(k1, k2 - 1):

        sum += nums[x]
    
    return sum

def main():

    print("Sum of all numbers between k1 and k2 smallest numbers: " + \
            str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " + \
            str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))




main()