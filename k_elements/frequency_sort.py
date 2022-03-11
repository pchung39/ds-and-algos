
from heapq import * 

def sort_character_by_frequency(str):

    # first iterate through the str and story frequency in a hash map
    hash_map = {}

    for letter in str:
        
        if letter not in hash_map:
            hash_map[letter] = 1
        else:
            hash_map[letter] += 1
    
    # next create a max heap with the longest character as the root 
    max_heap = []

    # push all of the items in the dictionary into the heap
    for k,v in hash_map.items():
        heappush(max_heap, (v, k))
    print("max heap", max_heap)
    # now reconstruct the string traversing the heap 
    sorted_string = []

    while max_heap: 

        # loop until all items are popped, recall it is in a tuple 
        frequency, char = heappop(max_heap)

        for _ in range(frequency):

            # append letter repeatedly into the sorted_string list 
            sorted_string.append(char)
        
    return ''.join(sorted_string)

def main():

    print("String after sorting characters by frequency: " + \
            sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " + \
            sort_character_by_frequency("abcbab"))


main()