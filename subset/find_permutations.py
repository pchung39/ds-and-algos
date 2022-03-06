from collections import deque

def find_permutations(nums):

    result = []
    permutations = deque()
    permutations.append([])

    # iterate through each number in the input array
    for num in nums:
        n = len(permutations)
        # iterate through each item in the result list
        for _ in range(n):
            old_perm = permutations.popleft()
            # iterate through each position in each item 
            for y in range(len(old_perm) + 1):
                new_perm = list(old_perm)
                new_perm.insert(y, num)

                # critical piece, if newly formed perm is not right size, 
                # send back to the queue. 
                if len(new_perm) == len(nums):
                    result.append(new_perm)
                else:
                    permutations.append(new_perm)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()