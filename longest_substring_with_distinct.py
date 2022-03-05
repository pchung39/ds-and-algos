
def longest_substring_with_distinct(arr):

    window_start = 0
    max_count = 0
    hashmap = {}

    for window_end in range(len(arr)):

        letter = arr[window_end]

        if letter in hashmap:

            # move window_start to one space after the index found for the letter entry 
            window_start = hashmap[letter] + 1

            # remove entry from hashmap
            del hashmap[letter]
            
        hashmap[letter] = window_end 

        # calculate max_count
        max_count = max(max_count, window_end - window_start + 1)
    
    return max_count


print(longest_substring_with_distinct("aabccbb"))
print(longest_substring_with_distinct("abbbb"))
print(longest_substring_with_distinct("abccde"))