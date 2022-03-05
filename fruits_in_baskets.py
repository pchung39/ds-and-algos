
def fruits_in_baskets(arr):

    # strat: sliding window
    window_start = 0
    max_length = 0
    fruit_hash = {}

    # iterate through all entries 
    for window_end in range(len(arr)):

        fruit = arr[window_end]

        # determine if in fruit_hash
        if fruit not in fruit_hash:
            fruit_hash[fruit] = 1
        else:
            fruit_hash[fruit] += 1
        
        # lets calculate if there is more than 2 distinct fruits
        # shrink window until only two distinct fruits 
        while len(fruit_hash) > 2:

            window_start_fruit = arr[window_start]
            del fruit_hash[window_start_fruit]
            window_start += 1
    
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


print(fruits_in_baskets(['A', 'B', 'C', 'A', 'C']))
print(fruits_in_baskets(['A', 'B', 'C', 'B', 'B', 'C']))

